from selenium.webdriver.common.by import By
from config.settings import *

def fill_feedback_form(driver):
    # fill sections
    for subject in SUBJECT_MAPPING:
        section_textbox = driver.find_element(by=By.CSS_SELECTOR, value=f'input[name="subjects[{subject}][section]"]')
        if section_textbox:
            section_textbox.send_keys(SUBJECT_MAPPING[subject][0])

    # fill faculty names
    for subject in SUBJECT_MAPPING:
        faculty_textbox = driver.find_element(by=By.CSS_SELECTOR, value=f'input[name="subjects[{subject}][faculty]"]')
        if faculty_textbox:
            faculty_textbox.send_keys(SUBJECT_MAPPING[subject][1])

    # select rating
    for subject in SUBJECT_MAPPING:
        for i in range(1, 20):
            rating = driver.find_element(by=By.CSS_SELECTOR,
                                         value=f"select[id=\"q{subject}_i{i}\"] option[value=\"5\"]")
            rating.click()

    # submit feedback
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    feedback_button = driver.find_element(by=By.CSS_SELECTOR, value="button[type=\"submit\"]")
    feedback_button.submit()