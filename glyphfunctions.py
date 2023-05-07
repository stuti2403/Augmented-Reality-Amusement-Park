import cv2
import numpy as np
 
def order_points(points):
 
    s = points.sum(axis=1)
    diff = np.diff(points, axis=1)
     
    ordered_points = np.zeros((4,2), dtype="float32")
 
    ordered_points[0] = points[np.argmin(s)]
    ordered_points[2] = points[np.argmax(s)]
    ordered_points[1] = points[np.argmin(diff)]
    ordered_points[3] = points[np.argmax(diff)]
    print("ordered points are")
    print(ordered_points)
 
    return ordered_points
 
def max_width_height(points):
 
    (tl, tr, br, bl) = points
 
    top_width = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    bottom_width = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    max_width = max(int(top_width), int(bottom_width))
 
    left_height = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    right_height = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    max_height = max(int(left_height), int(right_height))
 
    return (max_width,max_height)
 
def topdown_points(max_width, max_height):
    return np.array([
        [0, 0],
        [max_width-1, 0],
        [max_width-1, max_height-1],
        [0, max_height-1]], dtype="float32")
 
def get_topdown_quad(image, src):
    # src and dst points
    src = order_points(src)
 
    (max_width,max_height) = max_width_height(src)
    print("max width of src")
    print(max_width)
    print("max height of src")
    print(max_height)
    dst = topdown_points(max_width, max_height)
  
    # warp perspective
    matrix = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(image, matrix, max_width_height(src))
 
    # return top-down quad
    return warped
 
def get_glyph_pattern(image, black_threshold, white_threshold):
    print("in get glyph pattern")
    # collect pixel from each cell (left to right, top to bottom)
    cells = []
     
    cell_half_width = int(round(image.shape[1] / 10.0))
    cell_half_height = int(round(image.shape[0] / 10.0))
    print("cell half width")
    print(cell_half_width)
    print("cell half height")
    print(cell_half_height)

    row1 = cell_half_height*3
    row2 = cell_half_height*5
    row3 = cell_half_height*7
    col1 = cell_half_width*3
    col2 = cell_half_width*5
    col3 = cell_half_width*7
    print("before appending")
    cells.append(image[row1, col1])
    cells.append(image[row1, col2])
    cells.append(image[row1, col3])
    cells.append(image[row2, col1])
    cells.append(image[row2, col2])
    cells.append(image[row2, col3])
    print("apendded row2,col3")
    cells.append(image[row3, col1])
    cells.append(image[row3, col2])
    cells.append(image[row3, col3])
    print("cells are before for")
    print(cells)
    # threshold pixels to either black or white
    for idx, val in enumerate(cells):
        if val < black_threshold:
            cells[idx] = 0
        elif val > white_threshold:
            cells[idx] = 1
        else:
            return None
    print("cells of get glyph pattern are")
    print(cells)
    return cells
 
def get_vectors(image, points):
     
    # order points
    points = order_points(points)
 
    # load calibration data
    with np.load('webcam_calibration_ouput.npz') as X:
        mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]
   
    # set up criteria, image, points and axis
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    imgp = np.array(points, dtype="float32")
 
    objp = np.array([[0.,0.,0.],[1.,0.,0.],
                        [1.,1.,0.],[0.,1.,0.]], dtype="float32")  
 
    # calculate rotation and translation vectors
    cv2.cornerSubPix(gray,imgp,(11,11),(-1,-1),criteria)
    print("before rensac")
    retval, rvecs, tvecs, inliers= cv2.solvePnPRansac(objp, imgp, mtx, dist)
    print("after rensac")
    print("rvecs are")
    print(rvecs)
    print(tvecs)
 
    return rvecs, tvecs
