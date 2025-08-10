import pytesseract
from PIL import Image

# Uncomment and set this if Tesseract is not in your PATH:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_images(image_paths):
    results = []
    for image_path in image_paths:
        try:
            text = pytesseract.image_to_string(Image.open(image_path))
            results.append({"image": image_path, "text": text.strip()})
        except Exception as e:
            results.append({"image": image_path, "text": "", "error": str(e)})
    return results

if __name__ == "__main__":
    test_images = ["data/images/slide1_1.png"]
    print(ocr_images(test_images))
