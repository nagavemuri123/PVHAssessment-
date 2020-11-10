class MyAccountPage():
    def __init__(self, driver):

        self.driver = driver
        self.my_account_hlink_xpath = '//*[@id="root"]/div/div[2]/div/h1'
        self.address_hlink_xpath = '//*[@id="root"]/div/div[1]/ul/li[3]/a'
        self.add_new_address_button_xpath = '//*[@id="root"]/div/div[2]/div/div/button'
        self.first_name_textbox_xpath = '//*[@id="firstName"]'
        self.last_name_textbox_xpath = '//*[@id="lastName"]'
        self.street_textbox_xpath = '//*[@id="address1"]'
        self.houseNo_textbox_xpath = '//*[@id="address2"]'
        self.city_textbox_xpath = '//*[@id="city"]'
        self.zip_code_textbox_xpath = '//*[@id="zipCode"]'
        self.save_button_xpath = '//*[@id="root"]/div[2]/div/div/div/form/div[9]/button[2]'
        self.address_book_subtitle_xpath = '//*[@id="root"]/div/div[2]/div/h2'

    def get_my_account_text(self):
        text = self.driver.find_element_by_xpath(self.my_account_hlink_xpath).text
        return text

    def go_to_address_book(self):
        self.driver.find_element_by_xpath(self.address_hlink_xpath).click()

    def add_new_address(self):
        self.driver.find_element_by_xpath(self.add_new_address_button_xpath).click()

    def enter_first_name(self, fname):
        self.driver.find_element_by_xpath(self.first_name_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.first_name_textbox_xpath).send_keys(fname)

    def enter_last_name(self, lname):
        self.driver.find_element_by_xpath(self.last_name_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.last_name_textbox_xpath).send_keys(lname)

    def enter_street(self, street):
        self.driver.find_element_by_xpath(self.street_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.street_textbox_xpath).send_keys(street)

    def enter_house_number(self, house_number):
        self.driver.find_element_by_xpath(self.houseNo_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.houseNo_textbox_xpath).send_keys(house_number)

    def enter_city(self, city):
        self.driver.find_element_by_xpath(self.city_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.city_textbox_xpath).send_keys(city)

    def enter_zip_code(self, zip):
        self.driver.find_element_by_xpath(self.zip_code_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.zip_code_textbox_xpath).send_keys(zip)

    def save_address(self):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()

    def get_address_as_subtitle(self):
        sub_title = self.driver.find_element_by_xpath(self.address_book_subtitle_xpath).text
        return sub_title
