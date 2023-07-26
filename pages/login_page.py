from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    scouts_panel_label_xpath = "//*[text()='Scouts Panel']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    page_logo_xpath = "//*[@id='__next']//div[3]/div[1]/div/div[1]"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = ('Scouts panel - sign in')

    polski_login_panel_xpath = "//*[@id='menu-']//li[1]"
    english_login_panel_xpath = "//*[@id='__next']//div[2]/div/div"

    polski_url = ('https://scouts-test.futbolkolektyw.pl/pl/login')
    polski_expected_title = 'Scouts panel - zaloguj'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def click_on_the_english_button(self):
        self.click_on_the_element(self.english_login_panel_xpath)

    def click_on_the_polski_button(self):
        self.click_on_the_element(self.polski_login_panel_xpath)

    def title_of_polish_login_page(self):
        assert self.get_page_title(self.polski_url) == self.polski_expected_title
