import base64
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.print_page_options import PrintOptions
from config.settings import *


def initialize():
    options = Options()
    options.binary_location = BROWSER_PATH
    service = Service(DRIVER_PATH)
    web_driver = webdriver.Chrome(options=options, service=service)
    return web_driver

def login(driver):
    driver.get("https://reg.exam.dtu.ac.in/student/login")
    driver.implicitly_wait(0.5)
    if driver.title == "Privacy error":
        advanced_button = driver.find_element(by=By.ID, value="details-button")
        advanced_button.click()
        proceed_button = driver.find_element(by=By.ID, value="proceed-link")
        proceed_button.click()

    roll = driver.find_element(by=By.NAME, value="roll_no")
    roll.send_keys(ROLL)

    password = driver.find_element(by=By.NAME, value="password")
    password.send_keys(PASSWORD)

    driver.find_element(by=By.CSS_SELECTOR, value="button[type=\"submit\"]").click()

def switch_tabs(driver):
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a h3"))
    )
    original_window_handle = driver.current_window_handle

    admit_card_buttons = driver.find_elements(by=By.CSS_SELECTOR, value='a h3')
    if len(admit_card_buttons) > 1:
        admit_card_button = admit_card_buttons[1]
    else:
        admit_card_button = admit_card_buttons[0]
    admit_card_button.click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window_handle:
            driver.switch_to.window(window_handle)
            break

def fill_feedback_form(driver):
    # fill sections
    for subject in subject_section_faculty_map:
        section_textbox = driver.find_element(by=By.CSS_SELECTOR, value=f'input[name="subjects[{subject}][section]"]')
        if section_textbox:
            section_textbox.send_keys(subject_section_faculty_map[subject][0])

    # fill faculty names
    for subject in subject_section_faculty_map:
        faculty_textbox = driver.find_element(by=By.CSS_SELECTOR, value=f'input[name="subjects[{subject}][faculty]"]')
        if faculty_textbox:
            faculty_textbox.send_keys(subject_section_faculty_map[subject][1])

    # select rating
    for subject in subject_section_faculty_map:
        for i in range(1, 20):
            rating = driver.find_element(by=By.CSS_SELECTOR,
                                         value=f"select[id=\"q{subject}_i{i}\"] option[value=\"5\"]")
            rating.click()

    # submit feedback
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    feedback_button = driver.find_element(by=By.CSS_SELECTOR, value="button[type=\"submit\"]")
    feedback_button.submit()

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

def teardown(driver):
    try:
        driver.close()
        driver.close()
        driver.quit()
    except:
        print("Encountered problem closing browser, kindly close it manually.\n")

driver = initialize()
login(driver)
switch_tabs(driver)
# fill_feedback_form(driver)
save_pdf(driver)
teardown(driver)


