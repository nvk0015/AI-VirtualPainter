# AI-VirtualPainter

This project was created as a part of Hand Tracking course from CV Zone. 
The main goal of this project is to create a AI enabled painting tool which allows us to paint different colors on the display using Python, and OpenCV, Mediapipe packages. 
Hands module from the Google's Mediapipe was used to detect landmarks on hand, and simple math to calculate the distances, identify fingers, and draw accross the display. 

# HandTrackingModule.py
This module was developed with an intention to reuse accross several applications. It contains few methods to find the hands, position of landmarks, to check if the finers are up, and also to calculate distances accross several detected lanmarks. 
These fucntions can be further reused accross numerous applications depending on our need. Till date Virtual Painter, and Volume control using gestures are the applications pushed to this repository. There are several other applications taught in the CVzone's Hand Tracking course.

# VolumeControl.py

This script uses the written HandTackingModule and also a windows audio control from the following repo - https://github.com/AndreMiras/pycaw, also the numpy and opencv packages.

The workflow of this script is:
1. Access the web cam Opencv to perform operations of each frame of the video.
2. Detect the min and max volume, and range using the above mentioned package.
3. Use the Handtracking module to detect the landmarks, min and max distance accross the desired lanmarks (finger tips of index, thumb in our use case).
4. Interpret the distrances across the desired landmarks with the detected audio range.
5. Control the audio with variations in the landmark distances.
6. 

# VirtualPainter.py

This script uses the Handtracking module to detect the fingers, and then its position to draw on video frames and save it as an image file. It further gives us flexibility to select different colors from the listed options. 

At first Canvas - https://www.canva.com/ was used to design different image templates to use them as background in the later stages of the software development. The image templates are saved to images folder. 

The algorithm is described below.
1. Use the handtracking module to detect the landmarks, their position and track them across the frames of input video. 
2. Use the opencv videocapture module to read in the video, and perform further operations on each frame od the video.
3. Write dow the landmarks of desired keypoints across the frames into seperate lists (we use two fingers, index finfer tip, middle finger tip in our use case).
4. The algorithm has two modes - Drawing mode (when index finger tip alone is upwards), Selection mode (when both the finger tips are pointed upwards).
5. Further based on the position of the landmark in selection mode, if the landmarks reaches to selection area in the template the background templates change relative to their distance ranges of available colors (Red, green, blue, eraser templates in our use case). 
6. In the drawing mode, the painter draws across the postions of the landmark using opencv, and writes it to drive when broken out of the loop. 
![AI-VirtualPainter Demo](https://user-images.githubusercontent.com/61786557/143735675-3edfe783-4525-439b-9331-ca40ea7a6cb4.gif)


