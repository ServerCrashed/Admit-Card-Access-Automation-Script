from selenium.webdriver.common.by import By
from config.settings import *

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
