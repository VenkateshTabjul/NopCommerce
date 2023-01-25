import configparser
from configparser import ConfigParser
config = configparser.ConfigParser()
config.read(".\\Configurations\\config.ini") #r"K:\VenkateshTabjul\NopCommerce\Configurations\config.ini

class ReadConfig:
    @staticmethod  # static method means we are able to access these methods without creating an object
    def getbaseURL():
        baseurl = config['common info']['baseURL']
        print("baseurl:", baseurl)
        return baseurl

    @staticmethod
    def getuserName():
        username = config.get('common info', 'userName')
        print("username :", username)
        return username

    @staticmethod
    def getpassWord():
        password = config.get('common info', 'passWord')
        print("password :", password)
        return password

