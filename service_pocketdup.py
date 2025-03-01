import os
from PIL import Image
from globalvar import *
from services import *
from services_removecolor import *

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

    # After saving to sub folder, perform "lift" and save to pocket_sub2
    lift_and_save(target_path, os.path.join(os.path.dirname(target_path), "..", gv_fldr_pocket_sub2, os.path.basename(target_path)))

def lift_and_save(source_path, target_path):
    """Remove 5 pixels from top, add 5 transparent pixels to bottom."""
    img = Image.open(source_path)
    
    lv_liftValue = 8
    
    if 'main' in source_path:
        lv_liftValue = 5

    # Crop 5px from the top
    lifted_img = img.crop((0, lv_liftValue, img.width, img.height))

    # Create new image with 5 extra pixels at the bottom
    final_img = Image.new("RGBA", (lifted_img.width, lifted_img.height + lv_liftValue), (255, 255, 255, 0))
    final_img.paste(lifted_img, (0, 0))

    # Ensure target folder exists
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    # Save result
    final_img.save(target_path)
    print(f"Lifted and saved to: {target_path}")

def process_all_pocket_main(base_folder):
    """Walk through all folders recursively, process images inside any 'pocket main' folder."""
    for root, dirs, files in os.walk(base_folder):
        if os.path.basename(root).lower() == gv_fldr_pocket_main:
            parent_folder = os.path.dirname(root)

            pocket_sub_path = os.path.join(parent_folder, gv_fldr_pocket_sub)
            pocket_main2_path = os.path.join(parent_folder, gv_fldr_pocket_main2)
            pocket_sub2_path = os.path.join(parent_folder, gv_fldr_pocket_sub2)

            # Ensure both "2" folders exist
            os.makedirs(pocket_sub_path, exist_ok=True)
            os.makedirs(pocket_main2_path, exist_ok=True)
            os.makedirs(pocket_sub2_path, exist_ok=True)

            for filename in files:
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    source_path = os.path.join(root, filename)
                    target_sub_path = os.path.join(pocket_sub_path, filename)
                    target_main2_path = os.path.join(pocket_main2_path, filename)

                    # Process and save to pocket_sub
                    process_and_save(source_path, target_sub_path)

                    # Also "lift" and save directly to pocket_main2
                    lift_and_save(source_path, target_main2_path)

root_folder = f"{gv_previewimages}/{gv_shellfabrics}"  # Your actual root path
process_all_pocket_main(root_folder)
