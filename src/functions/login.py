import os

from selenium.webdriver.common.by import By
from dotenv import load_dotenv

BANK_LOGIN_ADDRESS = "https://login.portal.bancochile.cl/bancochile-web/persona/login/index.html"

load_dotenv()


class Login:
    def __init__(self, driver):
        self.driver = driver

    def execute(self):
        self.driver.get(BANK_LOGIN_ADDRESS)

        self.driver.set_page_load_timeout(30)

        rut_field = self.driver.find_element(
            by=By.XPATH, value='//*[@id="iduserName"]')
        rut_field.clear()
        rut_field.send_keys(os.getenv("BANCO_DE_CHILE_ACCOUNT_RUT"))

        password_field = self.driver.find_element(
            by=By.XPATH, value='/html/body/div[2]/div/article/form/div[2]/input[2]')
        password_field.clear()
        password_field.send_keys(os.getenv("BANCO_DE_CHILE_ACCOUNT_PASSWORD"))

        login_button = self.driver.find_element(
            by=By.XPATH, value='//*[@id="idIngresar"]')
        login_button.click()

        self.driver.set_page_load_timeout(30)
