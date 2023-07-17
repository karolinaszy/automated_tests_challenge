import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = "//*[text()='Main page']"
    players_xpath = "//*//ul[1]/div[2]/div[2]/span"
    polski_xpath = "//*[text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out']"
    scouts_panel_logo_xpath = "//*[contains(@style, 'background-image')]"
    left_panel_xpath = "//*[@id='__next']/div[1]/div/div]"
    dev_team_contact_xpath = "//*[contains(@target, '_blank')]"
    add_player_button_xpath = "//*/div[2]//div//button/span[1]"
    scouts_panel_header_xpath = "//*[@id='__next']//header//h6"
    players_count_tile_xpath = "//*//main/div[2]/div[1]/div"
    activity_tab_xpath = "//*/div[3]/div[3]/div"
    activity_text_xpath = "//*[text()='Activity']"
    shortcuts_text_xpath = "//*[text()='Shortcuts']"

    dashboard_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_dashboard_title = ('Scouts panel')

    add_a_player_url = ('https://scouts-test.futbolkolektyw.pl/en/players/add')
    add_a_player_expected_title = 'Add player'

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_dashboard_title

    def add_a_player(self):
        time.sleep(5)
        self.click_on_the_element(self.add_player_button_xpath)
        assert self.get_page_title(self.add_a_player_url) == self.add_a_player_expected_title