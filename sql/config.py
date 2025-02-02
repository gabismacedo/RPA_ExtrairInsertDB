# BIBLIOTECAS
from configparser import ConfigParser

config = ConfigParser()
config.read("auth.ini")
sql_driver = config["SQL-SERVER"]["DRIVER"]
server = config["SQL-SERVER"]["SERVER"]
database = config["SQL-SERVER"]["DATABASE"]
sql_user = config["SQL-SERVER"]["USER_NAME"]
sql_password = config["SQL-SERVER"]["PASSWORD"]
