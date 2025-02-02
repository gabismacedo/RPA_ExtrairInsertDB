# BIBLIOTECAS

import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

web = Service(r'chromedriver/chromedriver.exe')
config = configparser.ConfigParser()
config.read('auth.ini')
login = config["INFOB2B"]['login']
senha = config["INFOB2B"]['senha']
# driver = webdriver.Chrome(service=web)
url_portal = "https://www.portalinfob2b.com.br/"

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options,service=web)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
})