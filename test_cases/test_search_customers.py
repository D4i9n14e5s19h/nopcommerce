import pytest
import time

from base_pages.Add_Customer_Page import Add_Customer_Page
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Search_Customer_Page import Search_Customer_Page
from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config


class Test_04_Search_Customer:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_customer_by_email(self,setup):
        self.logger.info("********* Test_04_Search Customer with Email Started **********")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("*********** Login Completed **************")
        self.logger.info("*********** Navigating to Customer Search Page **************")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.logger.info("*********** Starting Search Customer By Email **************")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_customer_email("arthur_holmes@nopCommerce.com")
        self.search_customer.search_customer()
        time.sleep(3)

        is_email_present = self.search_customer.search_customer_by_email("arthur_holmes@nopCommerce.com")
        if is_email_present == True:
            assert True
            self.logger.info("************ Test Case: Search Customer By Email Test Passed ****************")
            self.driver.close()
        else:
            self.logger.info("************ Test Case: Search Customer By Email Test Failed ****************")
            self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_email.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_name(self,setup):
        self.logger.info("*********** Test 4: Search Customer with Name Started **************")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("*********** Login Completed **************")
        self.logger.info("*********** Navigating to Customer Search Page **************")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.logger.info("*********** Starting Search Customer By Name **************")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_customer_firstname("Jenny")
        self.search_customer.enter_customer_lastname("Shaw")
        self.search_customer.search_customer()
        time.sleep(3)

        is_name_present = self.search_customer.search_customer_by_name("Jenny Shaw")
        if is_name_present == True:
            assert True
            self.logger.info("************ Test Case: Search Customer By Name Test Passed ****************")
            self.driver.close()
        else:
            self.logger.info("************ Test Case: Search Customer By Name Test Failed ****************")
            self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_name.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_companyname(self,setup):
        self.logger.info("*********** Test 4: Search Customer with Company Name Started **************")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("*********** Login Completed **************")
        self.logger.info("*********** Navigating to Customer Search Page **************")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.logger.info("*********** Starting Search Customer By Company Name **************")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.company_name("CGSASP PVT LTD")
        self.search_customer.search_customer()
        time.sleep(3)

        is_cmpname_present = self.search_customer.search_customer_by_companyname("CGSASP PVT LTD")
        if is_cmpname_present == True:
            assert True
            self.logger.info("************ Test Case: Search Customer By Company Name Test Passed ****************")
            self.driver.close()
        else:
            self.logger.info("************ Test Case: Search Customer By Company Name Test Failed ****************")
            self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_companyname.png")
            self.driver.close()
            assert False







