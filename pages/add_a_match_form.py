from pages.base_page import BasePage


class Addingmatch(BasePage):
    my_team_input_xpath = "//*[@name='myTeam']"
    enemy_team_input_xpath = "//*[@name='enemyTeam']"
    my_team_score_input_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_input_xpath = "//*[@name='enemyTeamScore']"
    submit_xpath = "//*/div[3]/button[1]/span[2]"
    clear_xpath = "//*/button[2]/span[2]"
    general_input_xpath = "//*/div[12]/div//input"
    rating_input_xpath = "//*/div[13]/div/div/input"
    tshirt_color_input_xpath = "//*[@name='tshirt']"
    league_input_xpath = "//*[@name='league']"
