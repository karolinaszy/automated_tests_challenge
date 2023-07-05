from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = " //*[text()="Main page"]"
    players_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    polski_xpath ="//*[text()="Polski"]"
    sign_out_xpath = "//*[text()="Sign out"]"
    scouts_panel_logo_xpath = "//*[contains(@style, "background-image")]"
    contact_xpath = "//*[contains(@target, "_blank")]"
    left_panel_xpath = "//*[@id="__next"]/div[1]/div/div"
    email__xpath = "//input[starts-with(@name,'email')]"
    leg_xpath = "//*[@id="mui-component-select-leg"]"
    scouts_panel_header = "//*[@id="__next"]/div[1]/header/div/h6"

    pass