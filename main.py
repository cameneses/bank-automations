import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

from src.functions import Login, Transfer

BANK_LOGIN_ADDRESS = "https://login.portal.bancochile.cl/bancochile-web/persona/login/index.html"

load_dotenv()


def base_login():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,700")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options)

    if (os.getenv("BANCO_DE_CHILE_ACCOUNT_RUT") is None) or (os.getenv("BANCO_DE_CHILE_ACCOUNT_PASSWORD") is None):
        raise Exception("Missing environment variables")

    Login(driver).execute()

    Transfer(driver).execute()

    # driver.quit()


if __name__ == "__main__":
    base_login()
