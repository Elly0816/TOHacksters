**FaceBlock**

Web app that blurs requested faces in a folder of images.


**face_blur.py**


the file face_blur.py contains a class that takes 2 positional arguments: coordinates and folder

The coordinates parameter is a list of arrays that contain coordinates in an image.

The folder parameter is the name of a folder as a string.

The FaceBlur class writes images with those coordinates blurred in the folder passed to it with the 'blur_'  prepended to the original name of that image in the folder.