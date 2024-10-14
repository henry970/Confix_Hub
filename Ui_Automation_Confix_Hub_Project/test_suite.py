import pytest
from selenium import webdriver

from Ui_Automation_Confix_Hub_Project.Add_Contact_Page.ActionPage import LoginPage, ContactList_page
from config.config import Config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()

# Fixture for login page
@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.open_login_page(Config.BASE_URL)
    return login_page


# Negative test case for failed login
def test_negative_login_with_invalid_credentials(login):
    login.enter_email_address(Config.EMAIL)  # Enter invalid email
    login.enter_password(Config.WRONG_PASSWORD)  # Enter invalid password
    login.click_login_button()
    assert "Incorrect username or password" in login.get_error_message(), "Expected error message not displayed!"


# Positive test case for successful login
def test_positive_login_on_contact_list_website(login):
    login.clear_email_address()
    login.clear_password()
    login.enter_email_address(Config.EMAIL)
    login.enter_password(Config.PASSWORD)
    login.click_login_button()


# Test to click contact list button after login
def test_to_click_contact_list(login):
    contact_list = ContactList_page(login.driver)
    contact_list.click_contact_button()
