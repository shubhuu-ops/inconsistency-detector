from src.extract import extract_text_and_images
from src.ocr import ocr_images
from src.analyze import analyze_slides

def main():
    pptx_path = "data/sample_deck.pptx"
    image_output_dir = "data/images"

    slides_data = extract_text_and_images(pptx_path, image_output_dir)

    for slide in slides_data:
        if slide["images"]:
            ocr_results = ocr_images(slide["images"])
            slide["ocr_texts"] = [res["text"] for res in ocr_results]
        else:
            slide["ocr_texts"] = []

    analysis_result = analyze_slides(slides_data)

    print("\n=== Inconsistency Report ===\n")
    print(analysis_result)

if __name__ == "__main__":
    main()
