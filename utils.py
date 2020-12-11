import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='Argument parser for sampiyonlar ligi script')
    parser.add_argument('--driver-path', help='Path of the Chrome driver', default="drivers/chromedriver")
    args = parser.parse_args()

    return args
