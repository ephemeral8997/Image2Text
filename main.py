import pytesseract
from PIL import Image
import os


def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return f"Error processing {image_path}: {str(e)}"


image_folder = "images"
output_file = "extracted_text.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for filename in os.listdir(image_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp")):
            image_path = os.path.join(image_folder, filename)
            text = extract_text_from_image(image_path)
            f.write(f"--- {filename} ---\n")
            f.write(text + "\n\n")
            print(f"Processed: {filename}")
