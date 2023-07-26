import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = "//*[text()='Main page']"
    players_xpath = "//*//ul[1]/div[2]/div[2]/span"
    polski_xpath = "//*[text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    scouts_panel_logo_xpath = "//*[@title='Logo Scouts Panel']"
    left_panel_xpath = "//*[@id='__next']/div[1]/div/div]"
    dev_team_contact_xpath = "//*[contains(@target, '_blank')]"
    add_player_button_xpath = "//*/div[2]//div//button/span[1]"
    scouts_panel_header_xpath = "//*[@id='__next']//header//h6"
    players_count_tile_xpath = "//*//main/div[2]/div[1]/div"
    activity_tab_xpath = "//*/div[3]/div[3]/div"
    activity_text_xpath = "//*[text()='Activity']"
    shortcuts_text_xpath = "//*[text()='Shortcuts']"
    karolina_xpath = "//*[text()='Karolina Szybiak']"
    last_created_player_xpath = "//*[@id='__next']//div/div[3]//div/a[1]/button"

    dashboard_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_dashboard_title = ('Scouts panel')

    add_a_player_name_xpath = "//*[@name='name']"
    add_a_player_surname_xpath = "//*[@name='surname']"
    add_a_player_age_xpath = "//*[@name='age']"
    add_a_player_main_position_xpath = "//*[@name='mainPosition']"
    add_a_player_submit_xpath = "//*[@id='__next']//div[3]/button[1]"

    add_a_player_url = ('https://scouts-test.futbolkolektyw.pl/en/players/add')
    add_a_player_expected_title = 'Add player'

    polish_url = ('https://scouts-test.futbolkolektyw.pl/pl')
    polish_expected_title = 'Scouts panel'

    players_url = ('https://scouts-test.futbolkolektyw.pl/en/players')
    players_expected_title = 'Players (4263) page 1'

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.activity_tab_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_dashboard_title

    def add_a_player(self):
        time.sleep(3)
        self.click_on_the_element(self.add_player_button_xpath)
        assert self.get_page_title(self.add_a_player_url) == self.add_a_player_expected_title

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def type_in_name(self, name):
        self.field_send_keys(self.add_a_player_name_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.add_a_player_surname_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.add_a_player_age_xpath, age)

    def type_in_main_position(self, mainPosition):
        self.field_send_keys(self.add_a_player_main_position_xpath, mainPosition)

    def click_submit_button(self):
        self.click_on_the_element(self.add_a_player_submit_xpath)

    def click_on_the_players_button(self):
        self.click_on_the_element(self.players_xpath)

    def title_of_polish_page(self):
        self.click_on_the_element(self.polski_xpath)
        assert self.get_page_title(self.polish_url) == self.polish_expected_title