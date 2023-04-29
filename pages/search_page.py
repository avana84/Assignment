from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import Page

class SearchPage(Page):
    SEARCH_STAYS_BUTTON = (By.CSS_SELECTOR, "#accommodations")
    SEARCH_FIELD = (By.NAME, "ss")
    #CHECK_IN_DATE = (By.XPATH, "//button[text()='Check-in Date']")
    CHECK_IN_DATE = (By.XPATH, "//button[@data-testid='date-display-field-end']")
    CHECK_OUT_DATE = (By.XPATH, "//button[text()='Check-out Date']")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='fc63351294 a822bdf511 d4b6b7a9e7 cfb238afa1 c938084447 f4605622ad aa11d0d5cd']")
    SEARCH_RESULTS_TITLE = (By.XPATH, "//h1[@class='e1f827110f f0d4d6a2f5 fda3b74d0d']")
    SEARCH_RESULTS_PROPERTY_NAMES = (By.ID, ":Rp5:")
    COOKIE_ACCEPT = (By.ID, "onetrust-accept-btn-handler")
    DATE_TABLES = (By.XPATH, "//div[@data-testid='searchbox-datepicker-calendar']/div/div")
    ACTUAL_DESTINATION = (By.XPATH, "//div[@data-component='arp-header']//h1")

    def click_search_stays_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_STAYS_BUTTON)).click()

    def enter_destination(self, destination):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD)).send_keys(destination)

    def select_checkin_date(self, checkin_date):
        self.wait_for_element_click(*self.COOKIE_ACCEPT)
        self.wait_for_element_click(*self.CHECK_IN_DATE)
        table = self.find_elements(*self.DATE_TABLES)[1]
        table.find_element(By.XPATH, f".//tr/td//span[text()='{checkin_date}']").click()


    def select_checkout_date(self, checkout_date):
        table = self.find_elements(*self.DATE_TABLES)[1]
        table.find_element(By.XPATH, f".//tr/td//span[text()='{checkout_date}']").click()

    def click_search_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_BUTTON)).click()

    def is_search_results_loaded(self):
        return self.wait.until(EC.visibility_of_element_located(self.SEARCH_RESULTS_TITLE)).is_displayed()

    def get_property_names(self):
        property_names = []
        for property_name in self.driver.find_elements(*self.SEARCH_RESULTS_PROPERTY_NAMES):
            property_names.append(property_name.text)
        return property_names

    def is_destination_in_search_results(self, destination):
        actual_destination = self.wait_for_element_appear(*self.ACTUAL_DESTINATION).text
        actual_destination = actual_destination[:actual_destination.index(":")]
        assert destination == actual_destination, f"Expected destination to be {destination} but found {actual_destination}"


