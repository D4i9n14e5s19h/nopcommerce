import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_Customer_Page:

    #Locators for Add Customer Page
    link_customers_menu_xpath = "/html/body/div[3]/aside/div/nav/ul/li[4]/a"
    link_customers_menuoption_xpath = "/html/body/div[3]/aside/div/nav/ul/li[4]/ul/li[1]/a/p"
    link_addnewcustomers_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    email_id = "Email"
    password_id = "Password"
    firstname_id = "FirstName"
    lastname_id = "LastName"
    gender_male_id = "Gender_Male"
    gender_female_id = "Gender_Female"
    companyname_id = "Company"
    tax_exempt_id ="IsTaxExempt"
    newsletter_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[8]/div[2]/div/div[1]/div/span/span[1]/span/ul/li/input"
    customer_roles_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[9]/div[2]/div/div[1]/div/span/span[1]/span/ul/li/input"

    customer_administrator_xpath = "/html/body/span/span/span/ul/li[1]"
    customer_forummoderators_xpath = "/html/body/span/span/span/ul/li[2]"
    customer_registered_xpath = "/html/body/span/span/span/ul/li[3]"
    customer_guests_xpath = "/html/body/span/span/span/ul/li[4]"
    customer_vendors_xpath = "/html/body/span/span/span/ul/li[5]"
    drpdwn_vendormanager_id = "VendorId"
    activestatus_id = "Active"
    change_password_id = "MustChangePassword"
    admin_comment_id = "AdminComment"
    btn_save_xpath ="/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver


    def click_customers(self):
        self.driver.find_element(By.XPATH, self.link_customers_menu_xpath).click()

    def click_customers_from_menu_options(self):
        self.driver.find_element(By.XPATH, self.link_customers_menuoption_xpath).click()

    def click_addnew_customers(self):
        self.driver.find_element(By.XPATH, self.link_addnewcustomers_xpath).click()

    def enter_email(self,email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def enter_firstname(self,firstname):
        self.driver.find_element(By.ID, self.firstname_id).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element(By.ID, self.lastname_id).send_keys(lastname)

    def select_gender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID,self.gender_female_id).click()
        else:
            self.driver.find_element(By.ID,self.gender_female_id).click()

    def enter_companyname(self, companyname):
        self.driver.find_element(By.ID, self.companyname_id).send_keys(companyname)

    def istaxexempt(self, taxexempt):
        self.driver.find_element(By.ID, self.tax_exempt_id).click()

    def select_newsletter(self, value):
        # click on the newsletter dropdown field
        elements = self.driver.find_elements(By.XPATH, self.newsletter_xpath)
        if not elements:
            raise Exception(f"Newsletter field not found with xpath: {self.newsletter_xpath}")

        newsletter_field = elements[0]
        newsletter_field.click()
        time.sleep(2)

        # choose based on value
        option_xpath = f"//li[contains(text(),'{value}')]"
        option = self.driver.find_element(By.XPATH, option_xpath)
        option.click()

    def select_customer_roles(self, role):
        # Click the customer roles dropdown
        elements = self.driver.find_elements(By.XPATH, self.customer_roles_xpath)
        if not elements:
            raise Exception("Customer Roles field not found!")

        customer_role_field = elements[0]
        customer_role_field.click()
        time.sleep(1)

        # Remove pre-selected roles if necessary
        try:
            selected_roles = self.driver.find_elements(By.XPATH, "/html/body/span/span/span/ul/li[3]")
            for sel in selected_roles:
                sel.click()  # removes role
        except:
            pass

        # Select the desired role
        if role == "Guests":
            self.driver.find_element(By.XPATH, self.customer_guests_xpath).click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.customer_administrator_xpath).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.customer_forummoderators_xpath).click()
        elif role == "Registered":
            self.driver.find_element(By.XPATH, self.customer_registered_xpath).click()
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.customer_vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.customer_administrator_xpath).click()
        time.sleep(1)
        customer_role_field.click()  # close dropdown

    def select_manager_of_vendor(self, value):
        drp_dwn = Select(self.driver.find_element(By.ID, self.drpdwn_vendormanager_id))
        drp_dwn.select_by_visible_text(value)

    def active_status(self, activestatus):
        self.driver.find_element(By.ID, self.activestatus_id).send_keys(activestatus)

    def change_pwd(self, changepwd):
        self.driver.find_element(By.ID, self.change_password_id).send_keys(changepwd)

    def enter_admin_comment(self, admincomment):
        self.driver.find_element(By.ID, self.admin_comment_id).send_keys(admincomment)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()


