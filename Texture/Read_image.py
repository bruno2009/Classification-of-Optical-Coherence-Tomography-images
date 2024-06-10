import cv2
import os

def ReadData(path, extension = '.jpg'):
    image_list = []
    for file in os.listdir(path):
        if file.endswith(extension):
            fullpath = os.path.join(path, file)
            # print(fullpath)
            image = cv2.imread(fullpath)
            image_list.append(image)
    return image_list
