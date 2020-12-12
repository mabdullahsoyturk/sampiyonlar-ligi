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

def parse_fund_type(browser, fund_type, best_k):
    select = browser.find_element_by_id('MainContent_DropDownListFundTypeExplanation')
    for option in select.find_elements_by_tag_name('option'):
        if option.text == fund_type:
            option.click()
            break

    time.sleep(3) # Quick hack to wait for page to load
    browser.execute_script("__doPostBack('ctl00$MainContent$GridViewFundReturn','Sort$GETIRI1A')")
    time.sleep(3) # Quick hack to wait for page to load
    browser.execute_script("__doPostBack('ctl00$MainContent$GridViewFundReturn','Sort$GETIRI1A')")
    time.sleep(3) # Quick hack to wait for page to load
    fund_table = browser.find_element_by_id("MainContent_GridViewFundReturn")
    rows = fund_table.find_elements(By.TAG_NAME,"tr")
    fund_elements = rows[1:best_k + 1]

    funds = []
    
    for fund_element in fund_elements:
        descriptions = fund_element.find_elements_by_class_name("fund-grid-item")
        performances = fund_element.find_elements_by_class_name("fund-grid-numeric")

        fund_code, fund_name, fund_type = [desc.text for desc in descriptions]
        one_month, three_months, six_months, from_new_year, one_year, three_years, five_years = [perf.text.replace(",",".").strip() for perf in performances]

        fund = Fund(fund_code, fund_name, fund_type, one_month, three_months, six_months, from_new_year, one_year, three_years, five_years)
        funds.append(fund)

    return funds

def parse_fund_types(browser, best_k):
    best_funds_all = {}

    for fon_type in fund_types:
        best_funds = parse_fund_type(browser, fon_type, best_k)
        best_funds_all[fon_type] = best_funds

    return best_funds_all

if __name__ == "__main__":
    args = get_arguments()

    browser = launch_browser(args.driver_path)
    best_funds_all = parse_fund_types(browser, args.best_k)

    for fund_type in fund_types:
        best_funds = best_funds_all[fund_type]
        export_to_csv(fund_type, best_funds)
    
    browser.quit()