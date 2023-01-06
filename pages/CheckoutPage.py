from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class CheckoutPage(BaseClass):
    Checkout_Locator=(By.XPATH,"//button[contains(text(),'Checkout')]")

    def __init__(self,driver):
        self.driver=driver

    def get_checkout(self):
        return self.get_element(self.Checkout_Locator)
