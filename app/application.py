from pages.booking_page import BookingPage
from pages.search_page import SearchPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.booking_page = BookingPage(self.driver)
        self.search_page = SearchPage(self.driver)