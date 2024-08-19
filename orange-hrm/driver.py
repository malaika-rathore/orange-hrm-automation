from selenium import webdriver

from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from pprint import pprint

# Functions
def setup_driver():
    # Doing the driver setting

    service = Service(executable_path=r"C:\Users\hp\Downloads\chromedriver_win32.zip\chromedriver.exe")

    options = Options()
    options.add_argument("--start-maximized")

    options.add_argument("disable-infobars")
    options.add_experimental_option("detach", True)

    # disable popups on startup
    options.add_argument("--disable-extensions")
    options.add_argument('--no-first-run')
    options.add_argument('--no-service-autorun')
    options.add_argument('--no-default-browser-check')
    # options.add_argument("--headless")  # This enables headless mode


    options.add_argument('--lang=en-US,en;q=0.9')

    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(service=service, options=options)
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 7)  # we may try with 3 values: 15, 20, 30
    return driver


