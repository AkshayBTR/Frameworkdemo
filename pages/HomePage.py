from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class HomePage(BaseClass):
    shop_locator=(By.XPATH,"//a[text()='Shop']")

    def __init__(self,driver):
        self.driver=driver

    def get_shop(self):
        return self.get_element(self.shop_locator)

