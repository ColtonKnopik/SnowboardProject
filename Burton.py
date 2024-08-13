from webscraper import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from SQLFunctions import *
from Utils import createbrowser, click_element_with_retry

print("Burton Initiated")
browser = createbrowser()
url = 'https://www.burton.com/us/en/c/mens-snowboards'
browser.get(url)


def CloseCookie():
    #Close the cookies popup
    try:
        cookie_popup = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'onetrust-banner-sdk'))
        )

        accept_button = WebDriverWait(cookie_popup, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
        )
        accept_button.click()
    except Exception as e:
        print("Cookie consent popup not found or could not be dismissed:", e)


def CloseEmail():
    #Close Email
    try:
        popup = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.preloaded_lightbox'))
        )

        close_button = WebDriverWait(popup, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.sidebar-iframe-close'))
        )
        close_button.click()
    except Exception as e:
        print("Email popup not found or could not be dismissed:", e)


def loadButton():
    try:
        load_popup_xpath = '//*[@id="catalog-app"]/div/div[5]/section/div[2]/section'
        load_button_xpath = '//*[@id="catalog-app"]/div/div[5]/section/div[2]/section/a'

        load_popup = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, load_popup_xpath))
        )

        # Attempt to click the load button with retries
        if click_element_with_retry(browser, load_button_xpath):
            print("Load button clicked successfully.")
        else:
            print("Failed to click the load button.")

        # Additional click attempt
        if click_element_with_retry(browser, load_button_xpath):
            print("Load button clicked successfully.")
        else:
            print("Failed to click the load button.")

        # Continue with the rest of your function
    except TimeoutException:
        print("Failed to locate elements within the given time.")


def ClickBoard(i):
    # Clicks on the snowboard to get tech and length details
    try:
        while True:
            snowboard_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//*[@id="catalog-app"]/div/div[5]/section/div[2]/article[{i}]'))
            )
            snowboard_button.click()
            print(f'Snowboard {i} Clicked\n')

            try:
                # Check if the page is redirected to the snowboard page
                WebDriverWait(browser, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'product-buy-block-wrapper'))
                )
                # If the redirection is successful, break the loop
                break
            except Exception as e:
                print(f'Page did not redirect for snowboard {i}, clicking the button again', e)

    except Exception as e:
        print(f'Snowboard button {i} was not found:', e)


def TechSpecsButton():
    # Open Tech Specs
    try:
        while True:
            techButton = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="-Tech Specs"]/dt/button'))
            )

            browser.execute_script("arguments[0].scrollIntoView(true);", techButton)

            try:
                browser.execute_script("arguments[0].click();", techButton)

                specsDetails = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'accordion-item-details'))
                )
                # If details are found, break the loop
                break
            except Exception as e:
                print('Details not found, clicking the button again', e)

    except Exception as e:
        print('Tech Specs button not found', e)


def getTitle():
    title_element = browser.find_element(By.XPATH, '//*[@id="catalog-app"]/div/div/section[1]/aside/div[1]/h1')
    return title_element.text.strip()


def getPrice():
    try:

        sale_price_element = browser.find_element(By.CLASS_NAME, 'sale-price')
        sale_price = sale_price_element.text
        if sale_price:
            return sale_price
        else:
            raise NoSuchElementException

    except NoSuchElementException:
        price_element = browser.find_element(By.CLASS_NAME, 'standard-price')
        priceText = price_element.text.strip().replace('$', '').replace(',', '')
        return priceText


def getBend():
    bendXpath = f'//*[@id="-Tech Specs"]/dd/div/ul/li[1]/ul/li'
    specsele = browser.find_element(By.XPATH, bendXpath)
    return specsele.text.strip()


def getFlex():
    flexXpath = f'//*[@id="-Tech Specs"]/dd/div/ul/li[3]/ul/li'
    specsele = browser.find_element(By.XPATH, flexXpath)
    return specsele.text.strip()


def getShape():
    shapeXpath = f'//*[@id="-Tech Specs"]/dd/div/ul/li[2]/ul/li'
    specsele = browser.find_element(By.XPATH, shapeXpath)
    return specsele.text.strip()


def insertsizes(snowboard_id):
    try:
        variant_swatch = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'variant-swatch-scroll-pane'))
        )

        size_spans = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.variant-swatch-scroll-pane .text-b3-standard'))
        )
        for size_span in size_spans:
            size_text = size_span.text.strip()
            size_url = size_span.find_element(By.XPATH, '..').get_attribute('href')
            insert_length_data(snowboard_id, size_text, getPrice(), size_url)

    except Exception as e:
        print(f"Error: {e}")


def burtonmain():
    CloseCookie()
    CloseEmail()
    loadButton()
    product_cards = browser.find_elements(By.CLASS_NAME, 'product-card')
    i = 2
    for _ in product_cards:
        ClickBoard(i)
        TechSpecsButton()
        snowboard_id = insert_spec_to_db(getTitle(), 'Burton', getBend(), getFlex(), getShape())
        insertsizes(snowboard_id)
        browser.back()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//*[@id="catalog-app"]/div/div[5]/section/div[2]/article[{i}]')))
        i = i + 1
