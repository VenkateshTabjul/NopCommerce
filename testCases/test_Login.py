import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Login:
    baseURl = ReadConfig.getbaseURL()  # "https://admin-demo.nopcommerce.com/"
    userName = ReadConfig.getuserName()   # "admin@yourstore.com"
    passWord = ReadConfig.getpassWord()   # "admin"

    logger = LogGen.loggen()  # Creating logs

    print("baseURl:", baseURl)

    @pytest.mark.sanity
    def test_homepage(self, setup):

        self.logger.info("********** Test Home_Page **********")
        self.driver = setup  # related to conftest.py file
        self.driver.get(self.baseURl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("********* Home page tiltle test is passed **********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.logger.error("********* Home page tiltle test is failed **********")
            self.driver.close()
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("********** Test Home_Page **********")
        self.driver = setup
        self.driver.get(self.baseURl)

        # Login Page
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.passWord)
        time.sleep(3)
        self.lp.clickLogin()
        act_title = self.driver.title
        print("act_title:", act_title)
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("********* Login page test is passed **********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_loginTitle.png")
            self.logger.error("********* Login page test is failed **********")
            self.driver.close()
            assert False
