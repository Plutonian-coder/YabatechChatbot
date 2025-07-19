import pytesseract
from PIL import Image
import requests

def get_dummy_response(prompt):
    """Get a response from the dummyjson API."""
    try:
        response = requests.get(f"https://dummyjson.com/todos/search?q={prompt}")
        data = response.json()
        if data['todos']:
            return data['todos'][0]['todo']
        else:
            return "I'm not sure how to respond to that."
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
