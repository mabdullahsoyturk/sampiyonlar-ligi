import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By       
import selenium.common.exceptions
import time, datetime, platform
from fund import Fund
from utils import get_arguments, export_to_csv

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
        if option.text == fund_type:
            option.click()
            break

    browser.execute_script("__doPostBack('ctl00$MainContent$GridViewFundReturn','Sort$GETIRI1A')")
    time.sleep(3) # Quick hack
    browser.execute_script("__doPostBack('ctl00$MainContent$GridViewFundReturn','Sort$GETIRI1A')")
    time.sleep(3) # Quick hack
    fund_table = browser.find_element_by_id("MainContent_GridViewFundReturn")
    rows = fund_table.find_elements(By.TAG_NAME,"tr")
    fund_elements = rows[1:best_of + 1]

    funds = []
    
    for fund_element in fund_elements:
        fund_descriptions = fund_element.find_elements_by_class_name("fund-grid-item")
        fund_performances = fund_element.find_elements_by_class_name("fund-grid-numeric")

        fund_code = fund_descriptions[0].text
        fund_name = fund_descriptions[1].text
        fund_type = fund_performances[2].text.strip()
        one_month = fund_performances[0].text.strip()
        three_months = fund_performances[1].text.strip()
        six_months = fund_performances[2].text.strip()
        from_new_year = fund_performances[3].text.strip()
        one_year = fund_performances[4].text.strip()
        three_years = fund_performances[5].text.strip()
        five_years = fund_performances[6].text.strip()

        fund = Fund(fund_code, fund_name, fund_type, one_month, three_months, six_months, from_new_year, one_year, three_years, five_years)
        funds.append(fund)

    return funds

def parse_fund_types(browser):
    best_funds_all = {}

    for fon_type in fund_types:
        best_funds = parse_fund_type(browser, fon_type)
        best_funds_all[fon_type] = best_funds

    return best_funds_all

if __name__ == "__main__":
    args = get_arguments()

    browser = launch_browser(args.driver_path)
    best_funds_all = parse_fund_types(browser)

    for fund_type in fund_types:
        best_funds = best_funds_all[fund_type]
        export_to_csv(fund_type, best_funds)