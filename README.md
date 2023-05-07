# Augmented-Reality-Amusement-Park
A computer Graphics Project that overlays 3D model of an Amusement Park onto a Glyph in real-time using Augmented Reality. 

## :innocent: About the Project
The project uses Blender for making 3D Modelof an amusement park, OpenGl for Glyph Detection on web camera feed and concepts of Augmented Reality for overlaying the model onto a glyph pattern. This way, when one visits the park for the first time, they can simply scan their tickets and looking at the map, plan their visit accordingly.

## :warning: TechStack/framework used

- [OpenGl] (https://www.opengl.org/)
- [OpenCV](https://opencv.org/)
- [Python](https://www.python.org/)


## Use cases of the project
This project can be used for real-time overlaying of maps and blueprints onto cards and tickets. Example include overlaying maps of a city's metro stations onto the respective travel cards, which, on being scanned by an individual's mobile camera would detect glyphs and perform augmeted reality overlays in real-time. This would cease the need to google the railway maps and plan one's journey.

## Working
## Making the 3D model on Blender:
The conveyer belt used in this project is made at home using spare parts like an old spare motor, a broken headphone's headband, a bed table and some empty medicine bottles for the wheels of the conveyer belt.
  <img src="https://github.com/Navtegh/Real-Time-Custom-Object-Detection-and-Counting-on-bespoke-conveyer-belt/blob/main/IMG_1.jpg"/>
 

## Training the model on custom dataset:
To train the model, run the file train_yolov8_model_on_custom_data.ipynb, and download the trained model.

## Testing and counting objects on the conveyer belt:
To count objects, run the file objdet.py and start the conveyer belt. The category of object and its count starts appearing on screen as the object moves on the conveyer belt.







https://user-images.githubusercontent.com/25746677/227775801-e7a99bc3-509b-4d37-895f-bbf516abf8f4.mp4


