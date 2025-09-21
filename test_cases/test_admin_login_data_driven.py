import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from test_cases.conftest import setup
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils

class Test02AdminLogin_Data_Driven:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = ".//test_data//Dataaa.xlsx"
    status_list = []


    def test_valid_admin_login_data_driven(self,setup):
        self.logger.info("**************** Test Login Data Driven Started *******************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.path,"Sheet1")
        print("Number of Rows", self.rows)



        for r in range(2, self.rows+1):
            self.Username = excel_utils.read_data(self.path,"Sheet1",r,1)
            self.Password = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.Exp_Login = excel_utils.read_data(self.path, "Sheet1", r, 3)
            self.admin_lp.enter_username(self.Username)
            self.admin_lp.enter_password(self.Password)
            self.admin_lp.click_login()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.Exp_Login == "Yes":
                    self.logger.info("Test Data Passed.")
                    self.status_list.append("Pass")
                    self.admin_lp.click_logout()
                elif self.Exp_Login == "No":
                    self.logger.info("Test Data Failed.")
                    self.status_list.append("Fail")

            elif act_title != exp_title:
                if self.Exp_Login == "Yes":
                    self.logger.info("Test Data Failed.")
                    self.status_list.append("Fail")

                elif self.Exp_Login == "No":
                    self.logger.info("Test Data Passed.")
                    self.status_list.append("Pass")

        print("Status list is", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test Admin Data Driven Test is Failed.")
            assert False
        else:
            self.logger.info("Test Admin Data Driven Test is Passed.")
            assert True



