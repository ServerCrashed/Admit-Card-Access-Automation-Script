from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config import settings

def get_driver():
    options = Options()
    if settings.BROWSER_PATH:
        options.binary_location = settings.BROWSER_PATH
    service = Service(settings.DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    return driver