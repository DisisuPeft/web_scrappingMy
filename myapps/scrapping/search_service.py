import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def search_products_links(search_term):
    chrome_options = Options()
    chrome_options.headless = True
    shops = ["amazon", "ebay", "bestbuy", "walmart", "sams", "aliexpress", "doto", "elektra"] #esto puede ser algo en la base de datos
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(f"https://www.google.com/search?q={search_term}+buy&hl=es")

        links = set()
        results = driver.find_elements(By.XPATH, "//a[@href]")
        # print(results)
        for result in results:
            href = result.get_attribute("href")
            # print(href)

            if any(keyword in href for keyword in shops) or ".mx" in href:
                if "google.com" not in href and "google.com.mx" not in href:
                    links.add(href)  #
            if len(links) >= 30:
                break

        return links
    finally:
        driver.quit()



def prices_products(products):
    chrome_options = Options()
    chrome_options.headless = True
    # shops = ["amazon", "ebay", "bestbuy", "walmart", "sams", "aliexpress", "doto", "elektra"] #esto puede ser algo en la base de datos
    driver = webdriver.Chrome(options=chrome_options)
    prices = []
    # print(products)
    try:
        for product in products:
        # print(product['url'])
            driver.get(f"{product['url']}")
            time.sleep(3)
            results = driver.find_elements(By.XPATH, "//*[contains(@class,'price') and contains(text(), '$')]")
            for result in results:
                if re.search(r'\$\d+(\.\d{2)?', result.text):
                    prices.append({
                        'price': result.text.strip(),
                        'URLs_id': product['id']
                    })
                    break
    finally:
        driver.quit()

    return prices