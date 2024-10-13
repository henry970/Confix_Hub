from selenium.webdriver.common.by import By


class LoginLocator:
    ENTER_EMAIL = (By.XPATH, "/html/body/div[3]/form/p[1]/input")
    ENTER_PASSWORD = (By.XPATH, "/html/body/div[3]/form/p[2]/input")
    CLICK_SUBMIT = (By.ID, "submit")
    ERROR_MESSAGE = (By.ID, "error")

class ContactListLocators:
    CLICK_CONTACT_LIST = (By.ID, "add-contact")