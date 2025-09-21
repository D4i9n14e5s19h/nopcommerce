import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from base_pages.Add_Customer_Page import Add_Customer_Page
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config


class Test_03_Add_New_Customer:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_new_customer(self, setup):
        self.logger.info("**********Test Case 3: Add New Customer Started ************")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("********* Login Completed **********")

        self.logger.info("************ Starting Add Customer Test **************")

        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.add_customer.click_addnew_customers()
        self.logger.info("************** Providing Customer Info Started ****************")


        email = self.generate_random_email()
        self.add_customer.enter_email(email)
        self.add_customer.enter_password("Test@123")
        self.add_customer.enter_firstname("Dinesh")
        self.add_customer.enter_lastname("Maharjan")
        self.add_customer.select_gender("Male")
        self.add_customer.enter_companyname("NepQA Pvt.Limited")
        self.add_customer.istaxexempt(True)
        self.add_customer.select_newsletter("nopCommerce admin demo store")
        self.logger.info("************** nopCommerce admin demo store Selected *****************")
        self.add_customer.select_customer_roles("Registered")
        self.add_customer.select_manager_of_vendor("Vendor 1")
        self.add_customer.enter_admin_comment("Test Admin Comment")
        self.add_customer.click_save()
        time.sleep(3)

        customer_add_success_text = "The new customer has been added successfully."
        success_text = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]").text

        if customer_add_success_text in success_text:
            assert True
            self.logger.info("*********** Test 3 Add New Customer Test Passed *************")
            self.driver.close()
        else:
            self.logger.info("*********** Test 3 Add New Customer Test Failed *************")
            self.driver.save_screenshot(".\\screenshots\\test_add_new_customer.png")
            self.driver.close()
            assert False


    @staticmethod
    def generate_random_email():
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domain = random.choice(['gmail.com','yahoo.com','outlook.com','example.com'])
        return f'{username}@{domain}'