import base64
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.print_page_options import PrintOptions
from config.settings import PDF_SAVE_PATH

def save_pdf(driver):
    # wait for the admit card to load
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.TAG_NAME, "table"))
    )

    print_options = PrintOptions()
    print_options.page_ranges = ["1"]

    pdf_base64 = driver.print_page(print_options)
    pdf_bytes = base64.b64decode(pdf_base64)
    try:
        with open(PDF_SAVE_PATH, "wb") as f:
            f.write(pdf_bytes)
        print(f"Saved admit card successfully at: {PDF_SAVE_PATH}")
    except Exception as e:
        print(f"Error saving PDF: {e}")