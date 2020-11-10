class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.agreement_button_xpath = '/html/body/div[4]/div/div/div/div[2]/button[1]'
        self.SignUp_button_xpath = '//*[@id="root"]/div/header/div[2]/div[2]/button'
        self.email_to_register_textbox_xpath = '//*[@name="email1"]'
        self.password_to_register_textbox_xpath = '//*[@id="root"]/div/header/div[3]/div[3]/div/div/div/div[2]/form/div[2]/div[1]/input'
        self.password_verify_textbox_xpath = '//*[@name="logonPasswordVerify"]'
        self.condition_checkbox_xpath = '//*[@id="root"]/div/header/div[3]/div[3]/div/div/div/div[2]/form/div[3]/label'
        self.register_button_xpath = '//*[@id="root"]/div/header/div[3]/div[3]/div/div/div/div[2]/form/button'
        self.empty_email_message_xpath = '//*[@id="root"]/div/header/div[3]/div[3]/div/div/div/div[2]/form/div[1]/div'
        self.empty_password_message_xpath = '//*[@id="root"]/div/header/div[3]/div[3]/div/div/div/div[2]/form/div[2]/div[1]/div'
        self.empty_verify_password_message_xpath = '//*[@id="root"]/div/header/div[3]/div[3]/div/div/div/div[2]/form/div[2]/div[2]/div'

    def accept_agreement(self):
        self.driver.find_element_by_xpath(self.agreement_button_xpath).click()

    def select_signup(self):
        self.driver.find_element_by_xpath(self.SignUp_button_xpath).click()

    def enter_email_to_register(self, email):
        self.driver.find_element_by_xpath(self.email_to_register_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.email_to_register_textbox_xpath).send_keys(email)

    def enter_password_to_register(self, password):
        self.driver.find_element_by_xpath(self.password_to_register_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_to_register_textbox_xpath).send_keys(password)

    def verify_password_entered(self, password):
        self.driver.find_element_by_xpath(self.password_verify_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_verify_textbox_xpath).send_keys(password)

    def accept_condition(self):
        self.driver.find_element_by_xpath(self.condition_checkbox_xpath).click()

    def register(self):
        self.driver.find_element_by_xpath(self.register_button_xpath).click()

    def enter_empty_email_and_tab(self):
        self.driver.find_element_by_xpath(self.email_to_register_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.email_to_register_textbox_xpath).click()

    def tab_to_verify_password(self):
        self.driver.find_element_by_xpath(self.password_verify_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_verify_textbox_xpath).click()

    def invalid_message_for_email(self):
        message = self.driver.find_element_by_xpath(self.empty_email_message_xpath).text
        return message

    def invalid_message_for_password(self):
        message = self.driver.find_element_by_xpath(self.empty_password_message_xpath).text
        return message

    def invalid_verify_password_message(self):
        message = self.driver.find_element_by_xpath(self.empty_verify_password_message_xpath).text
        return message
