# Augmented-Reality-Amusement-Park
A computer Graphics Project that overlays 3D model of an Amusement Park onto a Glyph in real-time using Augmented Reality. 

## :innocent: About the Project
The project uses Blender for making 3D Modelof an amusement park, OpenGl for Glyph Detection on web camera feed and concepts of Augmented Reality for overlaying the model onto a glyph pattern. This way, when one visits the park for the first time, they can simply scan their tickets and looking at the map, plan their visit accordingly.

## :warning: TechStack/framework used

- [OpenGL](https://www.opengl.org/)
- [OpenCV](https://opencv.org/)
- [Python](https://www.python.org/)


## Use cases of the project
This project can be used for real-time overlaying of maps and blueprints onto cards and tickets. Example include overlaying maps of a city's metro stations onto the respective travel cards, which, on being scanned by an individual's mobile camera would detect glyphs and perform augmeted reality overlays in real-time. This would cease the need to google the railway maps and plan one's journey.

## Working
## Making the 3D model on Blender:
The 3D model of amusement park is built on Blender and exported as a combination of a .obj file and a .mtl file for use in OpenGL. 
  <img src="https://github.com/stuti2403/Augmented-Reality-Amusement-Park/blob/main/blender%20model.png"/>
 

## Glyph Creation and Detection followed by Overlaying on OpenGL:
The glyph used looks like this. It is simply printed on a paper and kept in front of the web camera for detection:







https://user-images.githubusercontent.com/25746677/227775801-e7a99bc3-509b-4d37-895f-bbf516abf8f4.mp4


