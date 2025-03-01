import os

def rename_files_in_folder(folder_path):
    # First, handle the main file renames
    keyword_mapping = {
        'cutaway': 'mitered with flap',
        'pleat': 'pleated mitered with flap',
        'western': 'western'
    }

    pocket_sequence = [
        'mitered',
        'round',
        'square',
        'v-shaped',
        'mitered button through'
    ]

    pocket_index = 0

    # List all files (sorted to ensure order is stable)
    files = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

    for filename in files:
        old_path = os.path.join(folder_path, filename)

        lower_filename = filename.lower()

        # Step 1 - Rename main files (cutaway, pleat, western)
        renamed = False
        for keyword, new_name in keyword_mapping.items():
            if keyword in lower_filename:
                extension = os.path.splitext(filename)[1]
                new_filename = f'{new_name}{extension}'
                new_path = os.path.join(folder_path, new_filename)
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} → {new_filename}')
                renamed = True
                break  # Only rename once for main files

        if renamed:
            continue  # Skip pocket logic if this was a main file

        # Step 2 - Rename pocket files sequentially
        if 'pocket' in lower_filename and pocket_index < len(pocket_sequence):
            extension = os.path.splitext(filename)[1]
            new_filename = f'{pocket_sequence[pocket_index]}{extension}'
            pocket_index += 1
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f'Renamed pocket: {filename} → {new_filename}')

# Example usage
rename_files_in_folder("tmp/pocket main")  # Replace with your folder path
