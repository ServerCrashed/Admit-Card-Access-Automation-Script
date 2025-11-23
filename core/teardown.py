def teardown(driver):
    try:
        all_handles = driver.window_handles
        for handle in all_handles:
            driver.switch_to.window(handle)
            driver.close()

        driver.quit()
    except:
        print("Encountered problem closing browser, kindly close it manually.\n")