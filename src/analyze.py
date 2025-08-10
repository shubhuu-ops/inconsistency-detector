from src.llm_client import get_gemini_response

def analyze_slides(slides_data):
    all_text = []
    for slide in slides_data:
        combined_text = "\n".join(slide["texts"] + slide.get("ocr_texts", []))
        all_text.append(f"Slide {slide['slide_number']}:\n{combined_text}")

    prompt = (
        "You are an expert fact checker. The following are slides from a presentation. "
        "Identify factual, logical, numerical, or timeline inconsistencies between slides. "
        "For each issue, clearly mention the slide numbers involved and the problem.\n\n"
        + "\n\n".join(all_text)
    )

    return get_gemini_response(prompt)
