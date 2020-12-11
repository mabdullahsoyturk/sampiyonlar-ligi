import argparse
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
import time, datetime, platform
from utils import get_arguments

fon_types = ["Altın", "Borçlanma Araçları", "Değişken", "Endeks", "Eurobond", "Hisse Senedi", "Katılım"]

def launch_browser(driver_path):
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument('disable-infobars')
    browser_options.add_argument("disable-notifications")
    browser = webdriver.Chrome(executable_path=driver_path, options=browser_options)
    browser.get('https://www.tefas.gov.tr/FonKarsilastirma.aspx')
    return browser

def parse_fund_type(browser, fon_type, best_of=5):
    pass
    
def parse_fund_types(browser):
    best_funds_all = {}

    for fon_type in fon_types:
        best_funds = parse_fund_type(fon_type)
        best_funds_all[fon_type] = best_funds

    return best_funds_all

if __name__ == "__main__":
    args = get_arguments()

    browser = launch_browser(args.driver_path)