import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='Argument parser for sampiyonlar ligi script')
    parser.add_argument('--driver-path', help='Path of the Chrome driver', default="drivers/chromedriver")
    parser.add_argument('--best-k', help='Get best k fund for each category', default=5)
    args = parser.parse_args()

    return args

def export_to_csv(fund_type, best_funds):
    with open(fund_type + ".csv", "w") as fund_file:
        fund_file.write("kod,isim,tür,1 ay,3 Ay,6 Ay,Yılbaşından Beri,1 Yıl,3 Yıl,5 Yıl\n")
        for fund in best_funds:
            fund_file.write(fund.as_row())