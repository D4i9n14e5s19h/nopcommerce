import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_admin_page_url():
       url = config.get('Admin Login Info','admin_page_url')
       return url

    @staticmethod
    def get_username():
        username = config.get('Admin Login Info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('Admin Login Info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('Admin Login Info', 'invalid_username')
        return invalid_username