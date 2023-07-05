from pages.base_page import BasePage


class Addingmatch(BasePage):
    my_team_xpath = "//*[@name="myTeam"]"
    enemy_team_xpath = "//*[@name="enemyTeam"]"
    my_team_score_xpath = "//*[@name="myTeamScore"]"
    enemy_team_score_xpath = "//*[@name="enemyTeamScore"]"
    submit_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]/span[2]"
    cancel_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]/span[2]"
    general_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    rating_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[13]/div/div/input"
    tshirt_xpath = "//*[@name="tshirt"]"
    league_xpath = "//*[@name="league"]"

    pass