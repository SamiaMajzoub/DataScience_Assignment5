from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.ebay.com/globaldeals/tech"

def scrape_ebay_deals():
    driver.get(url)
    time.sleep(15)  

    # Scroll down
    scroll_pause_time = 2
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1

    while True:
        driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
        i += 1
        time.sleep(scroll_pause_time)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if (screen_height * i) > scroll_height:
            break

    products = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class, 'sections-container')]//div[contains(@class, 'dne-itemtile-detail')]")
        )
    )

    data = []
    for product in products:
        timestamp =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            title = product.find_element(By.XPATH, ".//h3[contains(@class, 'dne-itemtile-title')]").text
        except:
            title = "N/A"

        try:
            price = product.find_element(By.XPATH, ".//span[contains(@class, 'first')]").text
        except:
            price = "N/A"

        try:
            original_price = product.find_element(By.XPATH, ".//span[contains(@class, 'itemtile-price-strikethrough')]").text
        except:
            original_price = "N/A"

        try:
            shipping = product.find_element(By.XPATH, ".//span[contains(@class, 'dne-itemtile-delivery')]").text
        except:
            shipping = "N/A"

        try:
            item_url = product.find_element(By.XPATH, ".//a").get_attribute("href")
        except:
            item_url = "N/A"

        data.append({"Timestamp": timestamp, "Title" : title, "Price": price , "Original_price" : original_price, "Shipping": shipping, "Item_url": item_url})

    return data

def save_to_csv(data):
    file_name = "ebay_tech_deals.csv"
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=[
            "Timestamp", "Title", "Price", "Original_price", "Shipping", "Item_url"
        ])

    new_data = pd.DataFrame(data)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file_name, index=False)

if __name__ == "__main__":
    print("Scraping eBay Tech Deals...")
    scraped_data = scrape_ebay_deals()

    if scraped_data:
        save_to_csv(scraped_data)
        print(f"Scraped {len(scraped_data)} products. Data saved to ebay_tech_deals.csv.")
    else:
        print("Failed to scrape data.")

    driver.quit()