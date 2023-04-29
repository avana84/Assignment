from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import  Page

class BookingPage(Page):
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '.bb0b3e18ca.d9b0185ac2 .e57ffa4eb5')
    EMAIL_FIELD = (By.ID, 'username')
    CONTINUE_WITH_EMAIL_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/div[3]/button/span')
    PASSWORD_FIELD = (By.ID, 'password')
    SIGN_IN_SUBMIT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/div[2]/button/span')
    USER_ACCOUNT_PAGE_TITLE = (By.XPATH, '//*[@id="b2indexPage"]/div[2]/div/header/nav[1]/div[2]/button[2]/span/div/picture/img')

    REGISTER_BUTTON = (By.CSS_SELECTOR, '.fc63351294.a822bdf511.e2b4ffd73d.f7db01295e.c334e6f658.a9a04704ee.js-header-login-link')
    EMAIL_FIELD_FOR_SIGNUP = (By.ID, 'username')
    CONTINUE_WITH_EMAIL_BUTTON_FOR_SIGNUP = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/div[3]/button/span')
    PASSWORD_FIELD_FOR_SIGNUP = (By.ID, 'password')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, '//*[@id="root"]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/div[2]/button/span')
    SIGN_IN_REGISTER = (By.CSS_SELECTOR, '.Iiab0gVMeWOd4XcyJGA3.wPxWIS_rJCpwAWksE0s3.Ut3prtt_wDsi7NM_83Jc.TuDOVH9WFSdot9jLyXlw.EJWUAldA4O1mP0SSFXPm.whxYYRnvyHGyGqxO4ici')

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BUTTON)

    def open_main_page(self):
        self.driver.get('https://www.booking.com/')
    def enter_email_address(self, email):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD)).send_keys(email)

    def click_continue_with_email_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CONTINUE_WITH_EMAIL_BUTTON)).click()

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)

    def click_sign_in_submit_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SIGN_IN_SUBMIT_BUTTON)).click()

    def is_user_account_page_loaded(self):
        self.find_element(self.USER_ACCOUNT_PAGE_TITLE).is_displayed()

    def click_register_button(self):
        self.click(*self.REGISTER_BUTTON)

    def enter_email_address_for_signup(self, email):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD_FOR_SIGNUP)).send_keys(email)

    def click_continue_with_email_button_for_signup(self):
        self.wait.until(EC.visibility_of_element_located(self.CONTINUE_WITH_EMAIL_BUTTON_FOR_SIGNUP)).click()

    def enter_password_for_signup(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD_FOR_SIGNUP)).send_keys(password)

    def click_sign_up_button(self):
        self.click(*self.SIGN_IN_REGISTER)




