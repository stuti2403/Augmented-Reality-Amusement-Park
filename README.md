# Augmented-Reality-Amusement-Park
A computer Graphics Project that overlays 3D model of an Amusement Park onto a Glyph in real-time using Augmented Reality. 

## :innocent: About the Project
The project uses Blender for making 3D Modelof an amusement park, OpenGl for Glyph Detection on web camera feed and concepts of Augmented Reality for overlaying the model onto a glyph pattern. This way, when one visits the park for the first time, they can simply scan their tickets and looking at the map, plan their visit accordingly. The overlaying has also been made sensitive to rotation. In other words, as the glyph is rotated, the layout of the 3D model is also rotated accordingly.

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
 <img src="https://github.com/stuti2403/Augmented-Reality-Amusement-Park/blob/main/glyph_01.png"/>
 
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 
 On detecting the glyph, the code overlays the 3D model onto it as shown below. Also, as the glyph is rotated, the overlay of the model onto it is also rotated accordingly, as shown below: 
  <img src="https://github.com/stuti2403/Augmented-Reality-Amusement-Park/blob/main/output1.png"/>
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

<img src="https://github.com/stuti2403/Augmented-Reality-Amusement-Park/blob/main/output2.png"/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://github.com/stuti2403/Augmented-Reality-Amusement-Park/blob/main/output3.png"/>
 
 



