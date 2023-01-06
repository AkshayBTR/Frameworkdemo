import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.CheckoutPage import CheckoutPage
from pages.ConfirmationPage import ConfirmationPage
from pages.HomePage import HomePage
from pages.ItemsPage import ItemsPage
from utilities.BaseClass import BaseClass


class Test_e2e(BaseClass):
    def test_scenario_e2e(self):
        HomePage(self.driver).get_shop().click()

        item=ItemsPage(self.driver)
        item.get_required_item("Samsung").click()
        item.get_checkout_button().click()


        CheckoutPage(self.driver).get_checkout().click()

        confirmation=ConfirmationPage(self.driver)
        confirmation.get_country_field().send_keys("Ind")
        self.Explicit_Wait(EC.visibility_of_element_located,confirmation.Country_list_Locator,10)
        confirmation.get_country("India").click()
        confirmation.get_agree_terms().click()
        confirmation.get_Purchase().click()
        assert "Suchcess" in confirmation.get_purchase_status().text
        self.take_screenshot()
