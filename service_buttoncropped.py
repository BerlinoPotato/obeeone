import cv2
import numpy as np
import os
from PIL import Image, ImageDraw

def cropButton(ipFileName, ipCenter, ipAxes, ipRotation):
    # Paths
    input_folder = 'source/New Button Image'
    output_folder = 'output/buttonray'
    os.makedirs(output_folder, exist_ok=True)

    lv_inputfile = os.path.join(input_folder, ipFileName)

    img = cv2.imread(lv_inputfile, cv2.IMREAD_UNCHANGED)
    if img.shape[2] == 3:  # No alpha channel, add one
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    cv2.ellipse(mask, ipCenter, ipAxes, angle=0, startAngle=0, endAngle=360, color=255, thickness=-1)

    # Apply mask to alpha channel (transparency outside oval)
    img[:, :, 3] = mask

    # Crop to oval bounding box (tight crop to oval size BEFORE rotation)
    x, y = ipCenter
    cropped = img[y-ipAxes[1]:y+ipAxes[1], x-ipAxes[0]:x+ipAxes[0]]
    cropped_pil = Image.fromarray(cv2.cvtColor(cropped, cv2.COLOR_BGRA2RGBA))
    rotated_image = cropped_pil.rotate(ipRotation, expand=True)
    rotated_np = np.array(rotated_image)

    alpha_channel = rotated_np[:, :, 3]
    non_transparent_pixels = np.where(alpha_channel > 0)

    if non_transparent_pixels[0].size > 0 and non_transparent_pixels[1].size > 0:
        min_y = np.min(non_transparent_pixels[0])
        max_y = np.max(non_transparent_pixels[0])
        min_x = np.min(non_transparent_pixels[1])
        max_x = np.max(non_transparent_pixels[1])

        cropped_rotated_np = rotated_np[min_y:max_y+1, min_x:max_x+1]
        final_image = Image.fromarray(cropped_rotated_np)

    else:
        final_image = rotated_image  # Fallback (should never happen)

    filename_without_ext, _ = os.path.splitext(ipFileName)
    output_path = os.path.join(output_folder, f'{filename_without_ext}.png')
    final_image.save(output_path, format='PNG')

    # Show final result (optional)
    # final_image.show()

def button_resize(ipTargetSize):    
    input_folder = 'output/buttonray'
    
    target_size = (ipTargetSize, ipTargetSize)  # (width, height)

    # Create output folder if it does not exist
    output_folder = 'output/buttonray_resize'
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all images in the folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Open and resize image
            with Image.open(input_path) as img:
                resized_img = img.resize(target_size, Image.LANCZOS)

                # Save resized image
                resized_img.save(output_path)




def ButtonholeCreation(ipFileName, holeRelativeCenters=None, holeSize=(78, 69)):
    input_folder = 'output/buttonray_resize'
    output_folder = 'output/buttonray_resize_holes'
    os.makedirs(output_folder, exist_ok=True)

    # Default hole positions if not provided
    if holeRelativeCenters is None:
        holeRelativeCenters = [(187, 197), (312, 197), (187, 327), (312, 327)]

    # Paths
    input_path = os.path.join(input_folder, ipFileName)
    output_path = os.path.join(output_folder, ipFileName)

    # Load image (must already be RGBA with transparency)
    img = Image.open(input_path).convert('RGBA')
    img_np = np.array(img)

    # Punch transparent holes into alpha channel
    for cx, cy in holeRelativeCenters:
        hw, hh = holeSize[0] // 2, holeSize[1] // 2

        # Create elliptical mask for each hole
        y, x = np.ogrid[:img_np.shape[0], :img_np.shape[1]]
        mask = ((x - cx)**2 / hw**2 + (y - cy)**2 / hh**2) <= 1

        # Set alpha to 0 inside the holes (make them fully transparent)
        img_np[mask, 3] = 0


    img_with_holes = Image.fromarray(img_np)


    img_with_holes.save(output_path, format='PNG')

    # img_with_holes.show()










# cropButton('AGASSIZ TT2742.png',(2882, 1941),(250, 239) , -11 )    
# cropButton('AGASSIZ XT100.png', (3047, 2045), (328, 315) , -2)
# cropButton('AGASSIZ XT105.png', (3124, 2040), (322, 311) , -5)
# cropButton('JUCE SD SATIN TT1438.png', (3119, 2067), (313, 302) , -3)
# cropButton('JUCE SD SATIN TT1659.png', (3005, 2015), (313, 305) , -7)
# cropButton('JUCE SD SATIN TT2010.png', (3012, 2113), (325, 310) , -12)
# cropButton('PARIGI TT1438.png', (2944, 2027), (297, 278) , -3)
# cropButton('PARIGI TT1448.png', (3044, 2015), (327, 308) , -2)
# cropButton('PARIGI TT1659.png', (2957, 2132), (295, 275) , -5)
# cropButton('PARIGI TT2010.png', (2983, 1963), (300, 283) , -2)
# cropButton('QUITO TT1438.png', (2950, 1985), (285, 263) , -8)
# cropButton('QUITO TT1659.png', (2890, 2102), (367, 362) , 2)
# cropButton('QUITO TT2010.png', (3038, 2056), (314, 309) , -1)
# cropButton('SORAVA TT1438.png', (2948, 2050), (321, 308) , -4)
# cropButton('SORAVA TT1448.png', (2982, 2079), (313, 305) , -1)

# button_resize(500)    


# ButtonholeCreation('AGASSIZ TT2742.png')     #   DEFAULT      , [(187, 197), (312, 197), (187, 327), (312, 327)], (78, 69))
# ButtonholeCreation('AGASSIZ XT100.png')
# ButtonholeCreation('AGASSIZ XT105.png', [(189, 195), (314, 195), (189, 320), (314, 320)],   (78, 69))
# ButtonholeCreation('JUCE SD SATIN TT1438.png', [(187, 197), (303, 197), (187, 323), (303, 323)], (78, 69))
# ButtonholeCreation('JUCE SD SATIN TT1659.png', [(190, 203), (309, 203), (190, 315), (309, 315)], (70, 69))
# ButtonholeCreation('JUCE SD SATIN TT2010.png')
# ButtonholeCreation('PARIGI TT1438.png', [(195, 210), (308, 210), (195, 323), (308, 322)], (75, 69))
# ButtonholeCreation('PARIGI TT1448.png', [(194, 213), (312, 213), (194, 327), (312, 327)], (78, 72))
# ButtonholeCreation('PARIGI TT1659.png', [(187, 207), (309, 207), (187, 322), (309, 322)], (76, 69))
# ButtonholeCreation('PARIGI TT2010.png', [(190, 207), (308, 207), (190, 318), (308, 318)], (74, 69))
# ButtonholeCreation('QUITO TT1438.png', [(187, 197), (312, 197), (187, 327), (312, 327)], (76, 63))
# ButtonholeCreation('QUITO TT1659.png', [(195, 193), (316, 193), (195, 314), (316, 314)], (78, 72))
# ButtonholeCreation('QUITO TT2010.png', [(190, 197), (312, 197), (190, 309), (312, 309)], (78, 69))
# ButtonholeCreation('SORAVA TT1438.png', [(197, 205), (305, 205), (197, 312), (305, 312)], (75, 69))
ButtonholeCreation('SORAVA TT1448.png' , [(195, 215), (312, 215), (195, 320), (312, 320)], (78, 63))

   