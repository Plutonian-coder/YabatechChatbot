import pytesseract
from PIL import Image
import requests

def get_dummy_response(prompt):
    """Get a response from the dummyjson API."""
    try:
        response = requests.get(f"https://dummyjson.com/todos/search?q={prompt}")
        data = response.json()

        # Safely check if any result was found
        if data.get('todos') and len(data['todos']) > 0:
            return data['todos'][0].get('todo', "No todo text found.")
        else:
            return "No matching results found."

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
