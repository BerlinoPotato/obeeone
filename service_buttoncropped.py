import cv2
import numpy as np
import os
from PIL import Image

# Paths
# ipSourceFile = 'source/New Button Image/AGASSIZ TT2742.png'
# output_folder = 'output/buttonray'


def cropButton(ipFileName, ipCenter, ipAxes, ipRotation):
    
    lv_inputfile = f'source/New Button Image/{ipFileName}'
    output_folder = 'output/buttonray'
    os.makedirs(output_folder, exist_ok=True)

    # Load image
    img = cv2.imread(lv_inputfile)

    # Example: Define circular crop (this can be dynamic if you want to auto-detect)
    # ipCenter = (2882, 1941)
    # radius = 250
    # ipAxes = (250, 239) 

    # Create mask
    mask = np.zeros_like(img, dtype=np.uint8)
    # cv2.circle(mask, center, radius, (255, 255, 255), -1)
    cv2.ellipse(mask, ipCenter, ipAxes, angle=0, startAngle=0, endAngle=360, color=(255, 255, 255), thickness=-1)
    # Apply mask
    # rounded_button = cv2.bitwise_and(img, mask)
    oval_button = cv2.bitwise_and(img, mask)

    # Crop to bounding box around circle

    x, y = ipCenter
    cropped = oval_button[y-ipAxes[1]:y+ipAxes[1], x-ipAxes[0]:x+ipAxes[0]]
    cropped_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
    
    
    pil_image = Image.fromarray(cropped_rgb)
    rotated_image = pil_image.rotate(ipRotation, expand=True)

        # Prepare output path
    original_filename = os.path.basename(lv_inputfile)
    filename_without_ext, _ = os.path.splitext(original_filename)
    output_path = os.path.join(output_folder, f'{filename_without_ext}.png')

    # Save rotated image
    rotated_image.save(output_path)

    # Show rotated image
    rotated_image.show()
    
# cropButton('AGASSIZ TT2742.png',(2882, 1941),(250, 239) , -11 )    
# cropButton('AGASSIZ XT100.png', (3047, 2045), (328, 315) , -2)
# cropButton('AGASSIZ XT105.png', (3124, 2040), (322, 311) , -5)
# cropButton('JUCE SD SATIN TT1438.png', (3119, 2067), (313, 302) , -3)
# cropButton('JUCE SD SATIN TT1659.png', (3005, 2015), (313, 305) , -7)
# cropButton('JUCE SD SATIN TT2010.png', (3012, 2113), (325, 310) , -12)
cropButton('PARIGI TT1438.png', (3012, 2113), (325, 310) , -12)
