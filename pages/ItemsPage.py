from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class ItemsPage(BaseClass):
    items_locator=(By.XPATH,"//div[@class='card h-100']")
    checkout_locator=(By.XPATH,"//a[@class='nav-link btn btn-primary']")

    def __init__(self,driver):
        self.driver=driver

    def get_all_items(self):
        return self.get_elements(self.items_locator)


    def get_required_item(self,item_name):
        items=self.get_all_items()
        for item in items:
            if item_name.lower() in item.find_element(By.XPATH,"div/h4/a").text.lower():
                return item.find_element(By.XPATH, "div/button")
        return None

    def get_checkout_button(self):
        return self.get_element(self.checkout_locator)



