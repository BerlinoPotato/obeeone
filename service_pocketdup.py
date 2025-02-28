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

    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    cropped_img = flipped_img.crop((3, 0, flipped_img.width, flipped_img.height))
    new_width = cropped_img.width + 3
    new_img = Image.new("RGBA", (new_width, cropped_img.height), (255, 255, 255, 0))
    new_img.paste(cropped_img, (0, 0))
    new_img.save(target_path)

    print(f"Processed, flipped, cropped, and saved: {target_path}")
    
    
        
    #     todo move image up

    # # Load image
    # img = Image.open("your_image.png")

    # # Step 1: Crop 5 pixels off the top
    # cropped_img = img.crop((0, 5, img.width, img.height))

    # # Step 2: Create new canvas (original width, extra 5 pixels at bottom)
    # new_height = cropped_img.height + 5
    # new_img = Image.new("RGBA", (cropped_img.width, new_height), (255, 255, 255, 0))  # Transparent bottom

    # # Step 3: Paste cropped image onto new canvas
    # new_img.paste(cropped_img, (0, 0))

    # # Save result
    # new_img.save("cropped_and_extended.png")
    # new_img.show()

    
    

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



root_folder = f"{gv_previewimages}/{gv_shellfabrics}"  # Change this to your actual root path
process_all_pocket_main(root_folder)

