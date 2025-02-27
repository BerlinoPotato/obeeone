import json
import random
import os
from jsonvalues import values




input_file_path = "source/json/All Shirt Features.json"
print(input_file_path)
with open(input_file_path, "r") as f:
    original_data = json.load(f)

# Folder for generated JSON files
output_folder = "output/json"
os.makedirs(output_folder, exist_ok=True)

# Number of variations to generate
num_files = 5  

for i in range(num_files):
    # Deep copy to prevent modifications to the original data
    new_data = json.loads(json.dumps(original_data))

    # Modify OrderLineDetail values
    for order in new_data["Order"]:
        for order_line in order["OrderLine"]:
            for detail in order_line["OrderLineDetail"]:
                ref_name = detail["ref"]
                if ref_name in values:
                    detail["val"] = random.choice(values[ref_name])  # Replace with a random value

    # Save new JSON file
    output_path = os.path.join(output_folder, f"shirt_config_{i+1}.json")
    with open(output_path, "w") as out_f:
        json.dump(new_data, out_f, indent=4)

    print(f"Generated: {output_path}")
