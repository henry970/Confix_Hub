# import pytest
# from selenium import webdriver
# from config.config import Config
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from UI_Automation_Contact_list.Add_Contact_Page.ActionPage import LoginPage, ContactList_page
#
#
#
# # Fixture for browser setup, used across all tests in the module
# @pytest.fixture(scope="module")
# def driver_setup():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--window-size=1920x1080")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     driver.implicitly_wait(20)
#     yield driver
#     driver.quit()
#
#
# # Fixture for login page
# @pytest.fixture(scope="module")
# def login(driver_setup):
#     driver = driver_setup
#     login_page = LoginPage(driver)
#     login_page.open_login_page(Config.BASE_URL)
#     return login_page
#
#
# # Negative test case for failed login
# def test_negative_login_with_invalid_credentials(login):
#     login.enter_email_address(Config.EMAIL)  # Enter invalid email
#     login.enter_password(Config.WRONG_PASSWORD)  # Enter invalid password
#     login.click_login_button()
#
#
# # Positive test case for successful login
# def test_positive_login_on_contact_list_website(login):
#     login.enter_email_address(Config.EMAIL)
#     login.enter_password(Config.PASSWORD)
#     login.click_login_button()
#
#
# def test_to_click_contact_list(login):
#     contact_list = ContactList_page(login.driver)
#     contact_list.click_contact_button()



import pytest
from selenium import webdriver
from config.config import Config
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from UI_Automation_Contact_list.Add_Contact_Page.ActionPage import LoginPage, ContactList_page


# Fixture for browser setup, used across all tests in the module
@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(20)
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
    assert "Invalid email or password" in login.get_error_message(), "Expected error message not displayed!"


# Positive test case for successful login
def test_positive_login_on_contact_list_website(login):
    login.enter_email_address(Config.EMAIL)
    login.enter_password(Config.PASSWORD)
    login.click_login_button()


# Test to click contact list button after login
def test_to_click_contact_list(login):
    contact_list = ContactList_page(login.driver)
    contact_list.click_contact_button()
