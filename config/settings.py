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

# Replace with codes, sections and faculty names
SUBJECT_MAPPING = {
    os.getenv("S1") : [os.getenv("S1S"), os.getenv("S1F") ],
    os.getenv("S2") : [os.getenv("S2S"), os.getenv("S2F") ],
    os.getenv("S3") : [os.getenv("S3S"), os.getenv("S3F") ],
    os.getenv("S4") : [os.getenv("S4S"), os.getenv("S4F") ],
    os.getenv("S5") : [os.getenv("S5S"), os.getenv("S5F") ],
    os.getenv("S6") : [os.getenv("S6S"), os.getenv("S6F") ],
    os.getenv("S7") : [os.getenv("S7S"), os.getenv("S7F") ],
    os.getenv("S8") : [os.getenv("S8S"), os.getenv("S8F") ]
}

if not ROLL or not PASSWORD:
    raise ValueError("Missing credentials! Did you setup your .env file?")