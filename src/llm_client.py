from google import genai

def get_gemini_response(prompt):
    client = genai.Client()  # Uses GEMINI_API_KEY from env
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
