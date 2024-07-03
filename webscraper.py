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


    def ClickBoard(i):
        # Clicks on the snowboard to get tech and length details
        try:
            while True:
                snowboard_button = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f'//*[@id="catalog-app"]/div/div[5]/section/div[2]/article[{i}]'))
                )
                time.sleep(1)
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




    def PrintSpecs():
        #Print this boards specs
        title_element = browser.find_element(By.XPATH, '//*[@id="catalog-app"]/div/div/section[1]/aside/div[1]/h1')                   #
        print('------------------------------------------------------------------------------------------------------------------------\n')
        print('\nTitle:\n' + title_element.text + '\n')

        try:

            sale_price_element = browser.find_element(By.CLASS_NAME, 'sale-price')
            sale_price = sale_price_element.text
            if sale_price:
                print('Sale Price:\n' + sale_price + '\n')
            else:
                raise NoSuchElementException 

        except NoSuchElementException:
            price_element = browser.find_element(By.CLASS_NAME, 'standard-price')
            print('Price:\n' + price_element.text + '\n')

        
        bendXpath = f'//*[@id="-Tech Specs"]/dd/div/ul/li[1]/ul/li'
        specsele = browser.find_element(By.XPATH, bendXpath)
        print("Bend: \n" + specsele.text + '\n')


        flexXpath = f'//*[@id="-Tech Specs"]/dd/div/ul/li[3]/ul/li'
        specsele = browser.find_element(By.XPATH, flexXpath)
        print("Flex: \n" + specsele.text + '\n')


        shapeXpath = f'//*[@id="-Tech Specs"]/dd/div/ul/li[2]/ul/li'
        specsele = browser.find_element(By.XPATH, shapeXpath)
        print("Shape: \n" + specsele.text + '\n')



    def PrintSizes():
        #Prints all available lengths and URL's to the boards
        
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

    CloseCookie()
    CloseEmail()


    load_popup = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="catalog-app"]/div/div[5]/section/div[2]/section')))
    load_button = WebDriverWait(load_popup, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="catalog-app"]/div/div[5]/section/div[2]/section/a'))
    )
    load_button.click()
    print('load button clicked')
    load_button.click()
    print('load button clicked again')


    product_cards = browser.find_elements(By.CLASS_NAME, 'product-card')

    i = 2
    for card in product_cards:
        ClickBoard(i)
        TechSpecsButton()
        PrintSpecs()
        PrintSizes()
        browser.back()
        WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="catalog-app"]/div/div[5]/section/div[2]/article[{i}]')))
        i = i + 1

def main():
    try:
        browser = webdriver.Chrome()
    except Exception as e:
        print("WebDriver initialization failed:", e)
        exit()

    Burton(browser)
    browser.quit()

main()
