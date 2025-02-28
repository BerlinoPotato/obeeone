import os
from PIL import Image
from globalvar import *
from services import *
from services_removecolor import *


import os
from PIL import Image

def process_and_save(source_path, target_path):
    """Open image, flip horizontally, crop 3px from left, add 3px to right, and save."""
    img = Image.open(source_path)

    # Flip horizontally
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

    # Crop 3 pixels from the new left (which was originally the right)
    cropped_img = flipped_img.crop((3, 0, flipped_img.width, flipped_img.height))

    # Create new canvas with 3 extra pixels on the right
    new_width = cropped_img.width + 3
    new_img = Image.new("RGBA", (new_width, cropped_img.height), (255, 255, 255, 0))

    # Paste cropped image onto the new canvas
    new_img.paste(cropped_img, (0, 0))

    # Save the processed image
    new_img.save(target_path)

    print(f"Processed, flipped, cropped, and saved: {target_path}")

def process_all_pocket_main(base_folder):
    """Walk through all folders recursively, process images inside any 'pocket main' folder."""
    for root, dirs, files in os.walk(base_folder):
        if os.path.basename(root).lower() == "pocket main":
            parent_folder = os.path.dirname(root)
            pocket_two_path = os.path.join(parent_folder, "pocket two3")

            if not os.path.exists(pocket_two_path):
                os.makedirs(pocket_two_path)

            for filename in files:
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    source_path = os.path.join(root, filename)
                    target_path = os.path.join(pocket_two_path, filename)

                    process_and_save(source_path, target_path)

# Set root folder (this is the folder where it will start searching for 'pocket main')
root_folder = f"{gv_previewimages}/{gv_shellfabrics}"  # Change this to your actual root path

process_all_pocket_main(root_folder)

print("Finished processing all 'pocket main' folders.")
