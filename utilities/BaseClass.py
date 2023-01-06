from datetime import datetime

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    screen_shot_location="screenshots/"+str(datetime.now().strftime("%Y%m%d%H%M%S"))+".png"
    def Explicit_Wait(self,wait_condition,locator,waiting_time):
        wait=WebDriverWait(self.driver,waiting_time)
        wait.until(wait_condition(locator))

    def take_screenshot(self):
        self.driver.save_screenshot(self.screen_shot_location)

    def by_type(self,locator_type):
        locator_type=locator_type.lower()
        if locator_type=="id":
            return By.ID
        if locator_type=="name":
            return By.NAME
        if "class" in locator_type:
            return By.CLASS_NAME
        if "css" in locator_type:
            return By.CSS_SELECTOR
        if "partial" in locator_type:
            return By.PARTIAL_LINK_TEXT
        if "link"==locator_type:
            return By.LINK_TEXT
        if "tag" in locator_type:
            return By.TAG_NAME
        return By.XPATH

    def get_element(self,locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)



