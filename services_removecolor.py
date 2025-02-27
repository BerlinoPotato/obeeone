import os
import cv2
import numpy as np

from collections        import Counter
from PIL                import Image
from sklearn.cluster    import KMeans



def detect_dominant_color_v01(image):
    """
    Detects the most dominant color tone in an image and returns "black", "green", or "red".
    """
    img_array = np.array(image)  # Convert image to NumPy array
    r, g, b, _ = img_array.reshape(-1, 4).T  # Extract RGB values (ignore Alpha)

    # Count occurrences of color categories
    color_counts = Counter()

    for i in range(len(r)):
        if r[i] < 50 and g[i] < 50 and b[i] < 50:
            color_counts["black"] += 1
        elif g[i] > r[i] + 50 and g[i] > b[i] + 50:
            color_counts["green"] += 1
        elif r[i] > g[i] + 50 and r[i] > b[i] + 50:
            color_counts["red"] += 1

    if not color_counts:
        return None  # No dominant color detected

    # Return the most frequent color
    return max(color_counts, key=color_counts.get)


def detect_dominant_color(image):
    """
    Detects the most dominant color tone in an image and returns "black", "green", or "red".
    """
    img_array = np.array(image)  # Convert image to NumPy array
    r, g, b, _ = img_array.reshape(-1, 4).T  # Extract RGB values (ignore Alpha)

    # Count occurrences of color categories
    color_counts = Counter()

    for i in range(len(r)):
        if r[i] < 60 and g[i] < 60 and b[i] < 60:  # Strict black detection
            color_counts["black"] += 1
        elif g[i] > r[i] * 1.3 and g[i] > b[i] * 1.3 and g[i] > 80:  # Improved green detection
            color_counts["green"] += 1
        elif r[i] > g[i] * 1.3 and r[i] > b[i] * 1.3 and r[i] > 80:  # Improved red detection
            color_counts["red"] += 1

    if not color_counts:
        return None  # No dominant color detected

    return max(color_counts, key=color_counts.get)


def remove_color_tone_pixels(image_path, output_path):
    """
    Detects the dominant color tone in an image, removes it, and saves the result.
    """
    img = Image.open(image_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size

    # dominant_color = detect_dominant_color(img)
    dominant_color = classify_color(get_dominant_color(image_path))

    
    if dominant_color is None:
        # print(f"Skipping {image_path} (no dominant color detected)")
        return
    
    # print(f"Processing {image_path} (removing {dominant_color})")

    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]

            if dominant_color.lower() == "black" and r < 50 and g < 50 and b < 50:
                pixels[x, y] = (0, 0, 0, 0)  # Transparent
            elif dominant_color.lower() == "green" and g > r + 50 and g > b + 50:
                pixels[x, y] = (0, 0, 0, 0)  # Transparent
            elif dominant_color.lower() == "red" and r > g + 50 and r > b + 50:
                pixels[x, y] = (0, 0, 0, 0)  # Transparent

    img.save(output_path, format="PNG")

def process_folder(input_folder, output_folder):
    """
    Processes all PNG images in the input folder and saves the modified images in the output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            
            
            output_path = os.path.join(output_folder, filename)
            remove_color_tone_pixels(input_path, output_path)
            
            # # print(input_path)
            # lv_dominantColor = get_dominant_color(input_path)
            # print(lv_dominantColor)
            # print(classify_color(get_dominant_color(input_path)))

COLOR_MAP = {
    "Black": np.array([0, 0, 0]),
    "Green": np.array([0, 255, 0]),
    "Red": np.array([255, 0, 0])
}

def get_dominant_color(image_path, k=3):
    """Extracts the dominant color from a PNG image while ignoring transparent pixels."""
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)  # Load image with alpha channel
    
    if image.shape[2] == 4:  # Check if image has an alpha channel
        # Extract RGB and Alpha channels
        rgba = image[:, :, :3]  # RGB channels
        alpha = image[:, :, 3]   # Alpha channel

        # Keep only opaque pixels (alpha > 0)
        pixels = rgba[alpha > 0].reshape(-1, 3)

    else:
        # If no alpha channel, use the entire image
        pixels = image.reshape(-1, 3)

    # If there are no opaque pixels, return a default color
    if len(pixels) == 0:
        return np.array([0, 0, 0])  # Default to black if all pixels are transparent

    # Apply KMeans clustering to find dominant color
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    dominant_color = colors[labels[np.argmax(counts)]]

    return dominant_color

def classify_color(dominant_color):
    """Classifies the dominant color as Black, Green, or Red based on the closest match."""
    min_distance = float('inf')
    best_match = None
    
    for color_name, ref_color in COLOR_MAP.items():
        distance = np.linalg.norm(dominant_color - ref_color)  # Euclidean distance
        if distance < min_distance:
            min_distance = distance
            best_match = color_name

    return best_match