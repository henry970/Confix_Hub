import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from UI_Automation_Contact_list.Add_Contact_Locators.Locators import LoginLocator, ContactListLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_email_address(self, email):
        try:
            enter_email_address = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LoginLocator.ENTER_EMAIL))
            enter_email_address.send_keys(email)
            self.logger.info(f"Email username: {email}")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to enter email address: {email} - {e}")
            self._take_screenshot("enter_email_address")

    def enter_password(self, password):
        try:
            password_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LoginLocator.ENTER_PASSWORD))
            password_field.send_keys(password)
            self.logger.info(f"Entered password")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to enter password - {e}")
            self._take_screenshot("enter_password")

    def click_login_button(self):
        try:
            login_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(LoginLocator.CLICK_SUBMIT))
            login_button.click()
            self.logger.info("Clicked login button")
            time.sleep(2)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to click login button - {e}")
            self._take_screenshot("click_login_button")

    def get_error_message(self):
        """Check if an error message is displayed after a failed login attempt."""
        try:
            error_message = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LoginLocator.ERROR_MESSAGE))
            self.logger.info("Incorrect username or password")
            return True
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Error message not displayed - {e}")
            self._take_screenshot("error_message_not_displayed")
            return False

    def _take_screenshot(self, action_name):
        screenshot_path = f"screenshots/{action_name}_{int(time.time())}.png"
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Screenshot saved to {screenshot_path}")



class ContactList_page:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def click_contact_button(self):
        try:
            click_contact_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(ContactListLocators.CLICK_CONTACT_LIST))
            click_contact_button.click()
            self.logger.info("Clicked contact list button")
            time.sleep(2)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to click contact list button - {e}")
            self._take_screenshot("click_contact_list_button")


    def _take_screenshot(self, action_name):
        screenshot_path = f"screenshots/{action_name}_{int(time.time())}.png"
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Screenshot saved to {screenshot_path}")




