import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils


class Test_Login_ddt:
    baseURl = ReadConfig.getbaseURL()  # "https://admin-demo.nopcommerce.com/"
    path = ".//TestData/LoginData.xlsx"
    # userName = ReadConfig.getuserName()   # "admin@yourstore.com"
    # passWord = ReadConfig.getpassWord()   # "admin"
    logger = LogGen.loggen()  # Creating logs


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********** Test_Login_ddt **********")
        self.logger.info("********** Test_Login_Page **********")
        self.driver = setup
        self.driver.get(self.baseURl)

        #Login Page
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("No of Rows in Excel :", self.rows)

        lst_status = []  #Empty list variable
        for row in range(2, self.rows+1):
            self.username = ExcelUtils.readData(self.path, 'Sheet1', row, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', row, 2)
            self.result = ExcelUtils.readData(self.path, 'Sheet1', row, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            time.sleep(3)
            self.lp.clickLogin()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            print("act_title:", act_title)

            if act_title == exp_title:
                if self.result == 'Pass':
                    self.logger.info("********* Passed **********")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.result == 'Fail':
                    self.logger.info("********* Failed ************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.result == 'Pass':
                    self.logger.info("********* Failed **********")
                    lst_status.append("Fail")
                elif self.result == 'Fail':
                    self.logger.info("********* Passed ************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***** Login DDT is Passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT is Failed ******")
            self.driver.close()
            assert False

        self.logger.info("****** End of DDT Login Test ******")
        self.logger.info("****** Completed Test Login DDT ******")
