import csv
from datetime import datetime
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from loguru import logger


class Client:
    @staticmethod
    def setup_driver():
        user_agent = UserAgent().random

        options = Options()
        options.add_argument("--headless")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service, options=options)
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})

        return driver
    
    @staticmethod
    def get_table_data(driver: webdriver) -> list:
        wait = WebDriverWait(driver, 60)
        table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sc-cOifOu")))
        table_html = table.get_attribute('outerHTML')
    
        soup = BeautifulSoup(table_html, 'html.parser')
        rows = soup.find_all('div', class_='sc-jcwpoC')
    
        data = []
        for row in rows:
            cols = row.find_all('div', class_='sc-ciSkZP')
            if cols:
                data.append([col.text.strip() for col in cols])
    
        return data
    
    @staticmethod
    def write_to_csv(data: list, path: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(path, 'a', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, delimiter = ';')
            for row in data:
                last_row = row[:-1] + [row[-1].replace('€', '€ ')]
                writer.writerow([timestamp] + last_row)

    @staticmethod
    def data_changed(old_data: list, new_data: list) -> bool:
        if len(old_data) != len(new_data):
            return True
        for old_row, new_row in zip(old_data, new_data):
            if old_row != new_row:
                return True
        return False
    
    @staticmethod
    def get_data_with_retry(driver: webdriver, max_attempts=3) -> list | None:
        for attempt in range(max_attempts):
            driver.refresh()
            data = Client.get_table_data(driver)
            if data:
                return data
            logger.warning(f"Попытка {attempt + 1} не удалась. Повторное обновление страницы...")
            b = random.randint(5, 12)
            time.sleep(b)
        return None