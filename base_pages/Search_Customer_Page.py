from selenium.webdriver.common.by import By


class Search_Customer_Page:
     email_id = "SearchEmail"
     firstname_id = "SearchFirstName"
     lastname_id = "SearchLastName"
     btn_search_id = "search-customers"
     companyname_id = "SearchCompany"

     rows_table_xpath = "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div/table/thead/tr"
     columns_table_xpath = "/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]"

     def __init__(self, driver):
         self.driver = driver

     def enter_customer_email(self,email):
         self.driver.find_element(By.ID, self.email_id).clear()
         self.driver.find_element(By.ID, self.email_id).send_keys(email)

     def enter_customer_firstname(self,firstname):
         self.driver.find_element(By.ID, self.firstname_id).clear()
         self.driver.find_element(By.ID, self.firstname_id).send_keys(firstname)

     def enter_customer_lastname(self,lastname):
         self.driver.find_element(By.ID, self.lastname_id).clear()
         self.driver.find_element(By.ID, self.lastname_id).send_keys(lastname)

     def search_customer(self):
         self.driver.find_element(By.ID, self.btn_search_id).click()

     def company_name(self, companyname):
         self.driver.find_element(By.ID, self.companyname_id).clear()
         self.driver.find_element(By.ID, self.companyname_id).send_keys(companyname)

     def get_results_table_rows(self):
         return len (self.driver.find_elements(By.XPATH, self.rows_table_xpath))

     def get_results_table_columns(self):
         return len (self.driver.find_elements(By.ID, self.columns_table_xpath))

     def search_customer_by_email(self, email):
         email_present_flag = False
         for r in range(1, self.get_results_table_rows() + 1):
             customer_email = self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']//tbody/tr[{r}]/td[2]").text
             if customer_email == email:
                 email_present_flag = True
                 break
         return email_present_flag

     def search_customer_by_name(self, name):
         name_present_flag = False
         for r in range(1, self.get_results_table_rows() + 1):
             customer_name = self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']//tbody/tr[{r}]/td[3]").text
             if customer_name == name:
                 name_present_flag = True
                 break
         return name_present_flag

     def search_customer_by_companyname(self, companyname):
         companyname_present_flag = False
         for r in range(1, self.get_results_table_rows() + 1):
             company_name = self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']//tbody/tr[{r}]/td[5]").text
             if company_name == companyname:
                 companyname_present_flag = True
                 break
         return companyname_present_flag


