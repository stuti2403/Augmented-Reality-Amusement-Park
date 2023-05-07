import cv2
from glyphfunctions import *
from glyphdatabase import *
 
class Glyphs:
     
    QUADRILATERAL_POINTS = 4
    BLACK_THRESHOLD = 120
    WHITE_THRESHOLD = 155
 
    def detect(self, image):
 
        glyphs = []
 
        # Stage 1: Detect edges in image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5), 0)
        edges = cv2.Canny(gray, 100, 200)
 
        # Stage 2: Find contours
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
 
        for contour in contours:
 
            # Stage 3: Shape check
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.01*perimeter, True)
            print('length of approx')
            print(len(approx))
 
            if len(approx) == self.QUADRILATERAL_POINTS:
                print("in if of glyphs.py")
 
                # Stage 4: Perspective warping
                topdown_quad = get_topdown_quad(gray, approx.reshape(4, 2))
                print("top down quad is")
                print(topdown_quad)
                print("rows in topdown quad")
                print(topdown_quad.shape[0])
                print("columns in topdown quad")
                print(topdown_quad.shape[1])
                print("here it iss")
                rows=topdown_quad.shape[0]
                columns=topdown_quad.shape[1]
                mul1=rows*5
                mul2=columns*5
                div1=mul1 // 100
                print("div1 is")
                print(div1)
                div2=mul2 // 100
                print("div2 is")
                print(div2)
                print("array value is")
                print(topdown_quad[div1,div2])
 
                # Stage 5: Border check
                if topdown_quad[div1,div2] > self.BLACK_THRESHOLD: continue
 
                # Stage 6: Match glyph pattern
                print("in step 6")
                print("********************")
                glyph_pattern = get_glyph_pattern(topdown_quad, self.BLACK_THRESHOLD, self.WHITE_THRESHOLD)
                print("get glyph patter returned, now match pattern")
                glyph_found, _, glyph_name = match_glyph_pattern(glyph_pattern)
                print("glyph found and name")
                print(glyph_found)
                print(glyph_name)
 
                if glyph_found:
 
                    # Stage 7: Get rotation and translation vectors
                    rvecs, tvecs = get_vectors(image, approx.reshape(4, 2))
                    print("rvec and tvec")
                    print(rvecs)
                    print(tvecs)
                    glyphs.append([rvecs, tvecs, glyph_name])
                    print("new glyphs are")
                    print(glyphs)
 
        return glyphs