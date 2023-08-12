import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

BANK_LOGIN_ADDRESS = "https://login.portal.bancochile.cl/bancochile-web/persona/login/index.html"

load_dotenv()


def base_login():
    driver = webdriver.Chrome()

    driver.get(BANK_LOGIN_ADDRESS)

    rut_field = driver.find_element(by=By.XPATH, value='//*[@id="iduserName"]')
    rut_field.clear()
    rut_field.send_keys(os.getenv("BANCO_DE_CHILE_ACCOUNT_RUT"))

    password_field = driver.find_element(
        by=By.XPATH, value='/html/body/div[2]/div/article/form/div[2]/input[2]')
    password_field.clear()
    password_field.send_keys(os.getenv("BANCO_DE_CHILE_ACCOUNT_PASSWORD"))

    login_button = driver.find_element(
        by=By.XPATH, value='//*[@id="idIngresar"]')
    login_button.click()

    driver.set_page_load_timeout(30)

    driver.quit()


if __name__ == "__main__":
    base_login()
