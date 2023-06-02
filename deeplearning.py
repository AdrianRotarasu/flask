import numpy as np
import matplotlib.pyplot as plt
import pytesseract as pt
from PIL import Image, ImageFilter
from ultralytics import YOLO
import base64
from io import BytesIO

#rf = Roboflow(api_key="Bv81WfXp2nY9ZIi2UdH6")
#project = rf.workspace().project("vehicle-registartion-plate-finder")
#modelRf = project.version(2).model
modelYolov8 = YOLO('./yolov8v2.pt')






def modify(file_stream):
    image = Image.open(file_stream)
    results = modelYolov8(image)
    cods = results[0].boxes.xyxy
    img = np.array(image)
    image.load()
    
    for cord in cods:
        xmin, ymin,xmax,  ymax = map(int, cord)  # Convert Tensor values to integers
        
        crop = image.crop((xmin, ymin, xmax, ymax))
        image.paste(crop.filter(ImageFilter.GaussianBlur(20)), (xmin, ymin))

    return image

