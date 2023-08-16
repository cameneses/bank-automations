import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from dotenv import load_dotenv

BANK_LOGIN_ADDRESS = "https://login.portal.bancochile.cl/bancochile-web/persona/login/index.html"

load_dotenv()

TRANSFERENCE_PAGE_ADDRESS = (
    "https://portalpersonas.bancochile.cl/mibancochile-web/"
    "front/persona/index.html#/tef/transferencia-electronica/transferencia-mis-cuentas"
)


class Transfer:
    def __init__(self, driver: Chrome):
        self.driver = driver

    def execute(self):
        self.driver.get(TRANSFERENCE_PAGE_ADDRESS)

        self.driver.set_page_load_timeout(30)

        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.find_element(
            By.ID, 'productos-resumen').is_displayed())

        resumen = self.driver.find_element(By.ID, 'productos-resumen')

        data = resumen.find_elements(By.CLASS_NAME, 'number number--small')

        print(resumen.get_attribute('innerHTML'))

        # # Find origin account field
        # self.driver.find_element(
        #     By.XPATH, '//*[@id="mat-select-2"]/div/div[2]').click()

        # self.driver.implicitly_wait(5)

        # # Select first account as the origin account
        # self.driver.find_element(By.XPATH, '//*[@id="mat-option-3"]').click()

        # self.driver.find_element(
        #     By.XPATH, '//*[@id="mat-input-3"]').send_keys('1')

        # self.driver.find_element(
        #     By.XPATH, '//*[@id="mat-input-2"]').send_keys(os.getenv("BANCO_DE_CHILE_ACCOUNT_PASSWORD"))

        # self.driver.implicitly_wait(5)

        # self.driver.find_elements(
        #     By.XPATH, ('//*[@id="main"]/fenix-transferencia-electronica-root/div/ui-view/'
        #                'fenix-main/section/ui-view/fenix-tef-mis-cuentas/div/div[2]/bch-button/div/button')).click()

        self.driver.implicitly_wait(10)
