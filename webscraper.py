from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time

def Burton(browser):
    print("Burton Initiated")
    url = 'https://www.burton.com/us/en/c/mens-snowboards'
    browser.get(url)

    try:
        cookie_popup = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'onetrust-banner-sdk'))
        )

        accept_button = WebDriverWait(cookie_popup, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
        )
        print("")
        accept_button.click()
    except Exception as e:
            print("Cookie consent popup not found or could not be dismissed:", e)


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


    wait = WebDriverWait(browser, 10)


    for i in range(1,8):
            title_xpath = f"//*[@id='tns1']/div[{i}]/div/article/figure/div/figcaption/a[1]/h2"
            sale_price_xpath = f"//*[@id='tns1']/div[{i}]/div/article/figure/div/figcaption/a[1]/div/span[2]"
            standard_price_xpath = f"//*[@id='tns1']/div[{i}]/div/article/figure/div/figcaption/a[1]/div/span[1]"

            title_element = browser.find_element(By.XPATH,title_xpath)
            title_text = title_element.get_attribute('innerHTML')

            sale_element = browser.find_element(By.XPATH, sale_price_xpath)
            sale_text = sale_element.get_attribute('innerHTML')

            standard_price_element = browser.find_element(By.XPATH, standard_price_xpath)
            standard_price_text = standard_price_element.get_attribute('innerHTML')

            print(f"Snowboard {i}:")
            print(title_text  + "\nStandard Price: " + standard_price_text + "\nSale Price: " + sale_text + "\n")

def burtonTest(browser):
    print("Burton Initiated")
    url = 'https://www.burton.com/us/en/c/mens-snowboards'
    browser.get(url)


#Close Cookies
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





#Click on the Snowboard
    try:
        snowboard_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="catalog-app"]/div/div[5]/section/div[2]/article[2]/figure/div/figcaption/a[1]'))
        )
        snowboard_button.click()
    except Exception as e:
        print('Snowboard button was not found:', e)


#Open Tech Specs
    try:
        techButton = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="-Tech Specs"]/dt/button'))
        )
        time.sleep(1)
        techButton.click()

    except Exception as e:
        print('Tech Specs button not found', e)



#Print Specs

    title_element = browser.find_element(By.XPATH, '//*[@id="catalog-app"]/div/div/section[1]/aside/div[1]/h1')
    print('Title:\n' + title_element.text + '\n')

    price_element = browser.find_element(By.XPATH, '//*[@id="catalog-app"]/div/div/section[1]/aside/div[2]/div[1]/span')
    print('Price:\n' + price_element.text + '\n')

    time.sleep(1)

    for i in range(1, 4):
        specsXpath = f'//*[@id="-Tech Specs"]/dd/div/ul/li[{i}]'
        specsele = browser.find_element(By.XPATH, specsXpath)
        print(specsele.text + '\n')






#Sizes


    try:
            # Wait for the variant swatch scroll pane to be present
        variant_swatch = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'variant-swatch-scroll-pane'))
    )

    # Find all span elements with the specific class within the variant swatch scroll pane
        size_spans = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.variant-swatch-scroll-pane .text-b3-standard'))
    )

    # Print the number of size elements found
        print(f"Number of size elements found: {len(size_spans)}")

    # Loop through each span tag to extract size and URL
        for size_span in size_spans:
            size_text = size_span.text.strip()
            size_url = size_span.find_element(By.XPATH, '..').get_attribute('href')
            print(f"Size: {size_text}, URL: {size_url}")
    

    except Exception as e:
        print(f"Error: {e}")























def main():
    try:
        browser = webdriver.Chrome()
    except Exception as e:
        print("WebDriver initialization failed:", e)
        exit()

    #Burton(browser)
    burtonTest(browser)

    browser.quit()




main()
