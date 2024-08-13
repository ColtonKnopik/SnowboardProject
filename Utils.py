from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
import time


def createbrowser():
    try:
        browser = webdriver.Chrome()
    except Exception as e:
        print("WebDriver initialization failed:", e)
        exit()

    return browser

def click_element_with_retry(browser, element_xpath, retries=1, delay=1):
    for attempt in range(retries):
        try:
            element = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, element_xpath))
            )
            element.click()
            return True
        except (StaleElementReferenceException, TimeoutException) as e:
            print(f"Exception caught: {e}. Retrying {attempt + 1}/{retries}...")
            time.sleep(delay)
    print(f"Failed to click element after {retries} retries.")
    return False