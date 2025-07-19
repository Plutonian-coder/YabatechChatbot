import openai
import os
from dotenv import load_dotenv
import pytesseract
from PIL import Image

load_dotenv()

def load_api_key():
    """Load the OpenAI API key from .env."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file.")
    openai.api_key = api_key

def get_openai_response(prompt):
    """Get a response from the OpenAI API."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def process_image_with_ocr(image_file):
    """Process an image with OCR to extract text."""
    try:
        image = Image.open(image_file)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"An error occurred during OCR: {e}"
