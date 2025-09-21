import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from test_cases.conftest import setup
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test01AdminLogin:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    #For Invalid Login
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self, setup):
        self.logger.info("**************** Test Admin Login *******************")
        self.logger.info("**************** Verification of Admin Login Page Title *******************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            self.logger.info("**************** Title Matched *******************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("**************** Title Not Matched *******************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self,setup):
        self.logger.info("**************** Test Login Started *******************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_dashboard_text = self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if act_dashboard_text == "Dashboard":
            self.logger.info("**************** Dashboard Text Found *******************")
            assert True
            self.driver.close()
        else:
         self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
         self.driver.close()
         assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self, setup):
        self.logger.info("**************** Test Invalid Login Started *******************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH,"//li").text
        if error_message == "No customer account found":
            self.logger.info("**************** Test Invalid Login Error Message Matched *******************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False