from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class ConfirmationPage(BaseClass):
    Country_Field_Locator=(By.ID,"country")
    Agree_terms_Locator=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
    Purchase_Locator=(By.XPATH,"//input[@type='submit']")
    Country_list_Locator=(By.XPATH,"//div[@class='suggestions']/ul/li/a")
    Purchase_Status_Locator=(By.XPATH,"//div/strong")

    def __init__(self,driver):
        self.driver=driver

    def get_country_field(self):
        return self.get_element(self.Country_Field_Locator)

    def get_country_list(self):
        return self.get_elements(self.Country_list_Locator)

    def get_country(self,country_name):
        countries=self.get_country_list()
        for country in countries:
            if country_name.lower()==country.text.lower():
                return country
        return None

    def get_agree_terms(self):
        return self.get_element(self.Agree_terms_Locator)

    def get_Purchase(self):
        return self.get_element(self.Purchase_Locator)

    def get_purchase_status(self):
        return self.get_element(self.Purchase_Status_Locator)
