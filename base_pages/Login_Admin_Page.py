from selenium.webdriver.common.by import By


class Login_Admin_Page:
    textbox_username_id = "Email"

    textbox_password_id = "Password"

    btn_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"

    logout_linktext = "Logout"

    def __init__(self, driver):
      self.driver = driver

    def enter_username(self, username):
     self.driver.find_element(By.ID, self.textbox_username_id).clear()
     self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_linktext).click()