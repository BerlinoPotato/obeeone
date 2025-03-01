from globalvar import *
from PIL import Image
import os
from datetime import datetime, timedelta
from random import randint

def saveCanvas(ipObjCanvas, ipOutputFolder, ipFilename):
    os.makedirs(ipOutputFolder, exist_ok=True)
    
    if ipFilename.endswith(".png"):
        lv_filename = ipFilename
    else:
        lv_filename = f'{lv_filename}.png'
    
    lv_outputFile = os.path.join(ipOutputFolder, lv_filename)
    ipObjCanvas.save(lv_outputFile)

def create_trims(ipSourceFolder, ipTargetFolder, ipFileName, ipPositions, ipFctResize, ipRotation=[0,0,0]):
        
    image_files = [f for f in os.listdir(ipSourceFolder)]
    image_files.sort()
    
    positions= ipPositions
    
    for img_file in image_files:
        img_path = os.path.join(ipSourceFolder, img_file)
        
        obj = Image.open(img_path).convert("RGBA")
        new_width = int(obj.width * (ipFctResize / 100))
        new_height = int(obj.height * (ipFctResize / 100))
        obj = obj.resize((new_width, new_height))

        canvas = Image.new("RGBA", gv_ImageSize, (255, 255, 255, 0))

        for i, pos in enumerate(positions):
            
            rotated_obj = obj.rotate(ipRotation[i], expand=True)  # Rotate 0, 90, 180 degrees
            canvas.paste(rotated_obj, pos, rotated_obj)  # Paste with transparency

        # saveCanvas(canvas, ipTargetFolder, f'{ipFileName}_{img_file}')

        saveCanvas(canvas, ipTargetFolder, f'{img_file}')