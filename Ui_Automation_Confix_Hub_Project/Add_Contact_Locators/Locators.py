from selenium.webdriver.common.by import By


class LoginLocator:
    ENTER_EMAIL = (By.XPATH, "/html/body/div[3]/form/p[1]/input")
    ENTER_PASSWORD = (By.XPATH, "/html/body/div[3]/form/p[2]/input")
    CLICK_SUBMIT = (By.XPATH, "/html/body/div[3]/form/p[3]/button")
    ERROR_MESSAGE = (By.XPATH, "/html/body/div[3]/span")

class ContactListLocators:
    CLICK_CONTACT_LIST = (By.XPATH, "/html/body/div/p[2]/button")

