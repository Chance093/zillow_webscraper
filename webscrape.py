from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_zillow(url):
    # Create the driver instance
    driver = webdriver.Chrome()

    try:
        driver.get(url)
        driver.implicitly_wait(0.5)

        properties = driver.find_elements(By.CSS_SELECTOR, ".kgwlbT")
        property_list = []

        for property in properties:
            print(property)
    finally:
        driver.quit()
