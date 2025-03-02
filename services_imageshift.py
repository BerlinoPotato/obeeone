import os
from PIL import Image
import glob

# List of image names to search for (you can modify this list with your exact image names)


# Function to crop and add pixels to the image
def modify_image(image_path, ipPxlsLeft=0, ipPxlsRght=0):
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Get the current size of the image
            width, height = img.size
            
            # Crop 5 pixels from the right (reduce width)
            img_cropped = img.crop((0, 0, width + ipPxlsRght, height))
            
            # Create a new blank image with extra 7 pixels on the left
            new_width = width + ipPxlsRght + ipPxlsLeft
            new_img = Image.new('RGBA', (new_width, height), (255, 255, 255, 0))
            
            # Paste the cropped image onto the new blank image starting at (7, 0)
            new_img.paste(img_cropped, (ipPxlsLeft, 0))
            
            # # Save the modified image in the same folder with _mod prefix
            # modified_image_path = os.path.splitext(image_path)[0] + '_mod.png'
            # new_img.save(modified_image_path)
            # print(f"Saved modified image: {modified_image_path}")
            
            
            
            
            # Get the filename without '_origin'
            filename = os.path.basename(image_path)
            if '_origin' in filename:
                # Remove '_origin' from the filename
                new_filename = filename.replace('_origin', '')
                modified_image_path = os.path.join(os.path.dirname(image_path), new_filename)
                new_img.save(modified_image_path)
                print(f"Saved modified image: {modified_image_path}")
            else:
                print(f"No '_origin' found in filename: {filename}")
            
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# Function to search for images in directories starting from root
def search_and_modify_images(ipRootDirectory, ipListImageName, ipPxlsLeft, ipPxlsRght):
    
    
    
    for dirpath, dirnames, filenames in os.walk(ipRootDirectory):  # Change the '/' if needed
        for filename in filenames:
            # Check if the file is a PNG and if it's in the list of image names
            if filename.endswith('.png') and filename in ipListImageName:
                image_path = os.path.join(dirpath, filename)
                print(f"Found image: {image_path}")
                modify_image(image_path, ipPxlsLeft, ipPxlsRght)

# Start the process

# lv_pxls_mod_left = 3
# lv_pxls_mod_rght = -3
# lv_LstImage = ['cuffed short sleeve_origin.png', 'short sleeve_origin.png']  # Add your image names here
# lv_RootDir = 'previewimages\shellfabrics'
# search_and_modify_images(lv_RootDir, lv_LstImage, lv_pxls_mod_left, lv_pxls_mod_rght)


lv_pxls_mod_left = -4
lv_pxls_mod_rght = 4
lv_LstImage = ['xxxxx.png', 'banded_origin.png']  # Add your image names here
lv_RootDir = 'previewimages\shellfabrics'
search_and_modify_images(lv_RootDir, lv_LstImage, lv_pxls_mod_left, lv_pxls_mod_rght)