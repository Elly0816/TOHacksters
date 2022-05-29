import numpy as np
import cv2
import os

class BlurFace:
    """This blurs certain coordinates from images in a file.
    It takes 2 parameters upon instantiation: coordinates and the name of the folder containing
    the images.
    Each coordinate should be sent as an array of arrays containing the top-left [x0, y1]
    and the bottom-right [x1, y0] corners of the detected face.
    The folder should contain as many images as coordinates passed through.
    The module writes the blurred images back into the folder with the string 'blur_' prepended
    to the original name of the corresponding image in the folder."""
    def __init__(self, coordinates, folder_name):
        self.coordinates: [int] = coordinates
        self.folder_name: str = folder_name
        self.anonymize_face_pixelate()

    def anonymize_face_pixelate(self, blocks=10):
        # find the coordinates sent on the image
        for image, coordinate in zip(os.listdir(self.folder_name), self.coordinates):
            img = cv2.imread(os.path.join(self.folder_name,image))
            #Coordinates should be sent as [[x0, y1], [x1, y0]]
            startY = coordinate[1][1]
            endY = coordinate[0][1]
            startX = coordinate[0][0]
            endX = coordinate[1][0]
            #Get the height and width of the region of interest (roi)
            (h, w) = endY-startY, endX-startX
            # Linearly spaced integers starting from the bottom left coordinate of the image to the top right coordinate
            xSteps = np.linspace(startX, w, blocks+1, dtype='int')
            ySteps = np.linspace(startY, h, blocks + 1, dtype='int')
            # loop over blocks in y and x
            for i in range(1, len(ySteps)):
                for j in range(1, len(xSteps)):
                    startX = xSteps[j -1]
                    startY = ySteps[i -1]
                    endX = xSteps[j]
                    endY = ySteps[i]
                    roi = img[startY:endY, startX:endX]
                    # Changes the rgb value to an average of the local region of interest
                    (R, G, B) = [int(x) for x in cv2.mean(roi)[:3]]
                    cv2.rectangle(img, (startX, startY), (endX, endY),
                                  (R, G, B), -1)
            # Writes the image back to the folder with blur_ prepended
            cv2.imwrite(os.path.join(self.folder_name, f"blur_{image}"), img)


blur = BlurFace(coordinates=[[[125, 400], [125, 400]], [[100, 350], [100, 350]]], folder_name='./images')
print(blur)


