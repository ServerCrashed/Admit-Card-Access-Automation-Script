from core import *
from pages import *

def main():
    driver = get_driver()
    try:
        # 1. Login
        login(driver)
    
        # 2. Switch tabs
        switch(driver)
    
        # 3. Fill Feedback form
        # Comment out if already filled
        fill_feedback_form(driver)
    
        # 4. Save PDF
        save_pdf(driver)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.implicitly_wait(1)
        teardown(driver)

if __name__ == "__main__":
    main()