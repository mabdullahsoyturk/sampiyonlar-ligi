import argparse
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import time, datetime, platform
from utils import get_arguments

fund_types = ["Altın", "Borçlanma Araçları", "Değişken", "Endeks", "Eurobond", "Hisse Senedi", "Katılım"]

def launch_browser(driver_path):
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument('disable-infobars')
    browser_options.add_argument("disable-notifications")
    browser = webdriver.Chrome(executable_path=driver_path, options=browser_options)
    browser.get('https://www.tefas.gov.tr/FonKarsilastirma.aspx')
    browser.maximize_window()
    return browser

def parse_fund_type(browser, fund_type, best_of=5):
    select = browser.find_element_by_id('MainContent_DropDownListFundTypeExplanation')
    for option in select.find_elements_by_tag_name('option'):
        print(option.text)
        print(fund_type)
        if option.text == fund_type:
            option.click()
            break

    browser.execute_script("__doPostBack('ctl00$MainContent$GridViewFundReturn','Sort$GETIRI1A')")
    time.sleep(10)
    browser.execute_script("__doPostBack('ctl00$MainContent$GridViewFundReturn','Sort$GETIRI1A')")

    

def parse_fund_types(browser):
    best_funds_all = {}

    for fon_type in fund_types:
        best_funds = parse_fund_type(browser, fon_type)
        exit()
        best_funds_all[fon_type] = best_funds

    return best_funds_all

if __name__ == "__main__":
    args = get_arguments()

    browser = launch_browser(args.driver_path)
    parse_fund_types(browser)