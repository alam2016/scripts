from app.ui.locators import LoginPageLocator


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def get_page_title(self):
        return self.driver.title

    def enter_username(self, username):
        self.driver.find_element_by_id("username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id("password").send_keys(password)

    def enter_company_id(self, company_id):
        self.driver.find_element_by_id("companyId").send_keys(company_id)

    def click_login(self):
        elem = self.driver.find_element(*LoginPageLocator.LOGIN_BUTTON)
        elem.click()
