import os
from dotenv import load_dotenv

# Load variables from .env file into the system
load_dotenv()

# Access them securely
BROWSER_PATH = os.getenv("BROWSER_PATH")
DRIVER_PATH = os.getenv("DRIVER_PATH")
ROLL = os.getenv("ROLL")
PASSWORD = os.getenv("PASSWORD")
PDF_SAVE_PATH = os.getenv("PDF_SAVE_PATH")
subject_section_faculty_map = os.getenv("subject_section_faculty_map")

if not ROLL or not PASSWORD:
    raise ValueError("Missing credentials! Did you setup your .env file?")