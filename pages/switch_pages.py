from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def switch(driver):
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