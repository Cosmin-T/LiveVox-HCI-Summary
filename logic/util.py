#!/usr/bin/env python3
#util.py

from dotenv import load_dotenv, get_key
import os
import logging
import glob
from datetime import datetime, timedelta

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

CROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
USER = get_key(dotenv_path, 'USER')
PASSWORD = get_key(dotenv_path, 'PASSWORD')
OUTLOOK_TEMPLATE = get_key(dotenv_path, 'OUTLOOK_TEMPLATE')
URL = get_key(dotenv_path, 'URL')
USER_XPATH = '//*[@id="username"]'
PASSWORD_XPATH = '//*[@id="password"]'
LOGIN_XPATH = '//*[@id="loginBtn"]/span'

# nav
REVIEW_XPATH = '//*[@id="lv-app"]/div/div/div/aside/div/div/div[2]/ul/button[3]'
AGENT_REPORTS_XPATH = '//*[@id="acdReports"]/div'
AGENT_SUMMARY_XPATH = '//*[@id="11"]'
FROM_DATE_ID = 'search-panel__start-date'
TO_DATE_ID = 'search-panel__end-date'
GENERATE_CLASS = 'lv-button__inside'
SERVICE_FORMAT = '//*[@id="service_combo"]'
SERVICE_TYPE_XPATH = '//*[@id="service_type_combo"]'
QUICK_CONNECT = 'Quick Connect (Auto)'
EXPORT_XPATH = "//button[@id='search-panel__export-btn']"
EXCEL_XPATH = "//div[@class='dropdown-content']/a[text()='Excel']"

# hci_agent
HCI_AGENT_LIST = (
    'JCI_HCI_AGENT (3181894)',
    'BN_HCI_AGENT (3176615)',
    'AU_HCI_AGENT (3174939)',
    'DS_HCI_AGENT (3173370)',
    'FEDEX_HCI_AGENT (3175378)',
    'LB1_HCI_AGENT (3183640)',
    'LB2_HCI_AGENT (3174416)',
    'SW_HCI_AGENT (3174210)',
    'LARGE_BAL_HCI_AGENT (3179837)',
    'PRIMO_HCI_AGENT (3177881)',
    'SMALL_BAL_HCI_AGENT (3179861)',
    'DELL_HCI_AGENT (3184975)',
    'USS_HCI_AGENT (3178530)',
    'DOM_HCI_AGENT_Uline (3186839)',
    'DOM_HCI_AGENT_SB_Team (3187140)',
)


# files
GENERIC_NAME = 'report_' # downloaded name (downloads folder)
FILE_PATH1 = '/Users/cosmint/Downloads'
FILE_HISTORY = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_hci_summary/history'

# pandas
GENERIC_FILE_NAME = 'HCI_AGENT' # HCI name (livevx_hci_summary folder)
OUTPUT_DIR = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_hci_summary'
HEADERS = ['Service', 'Total', 'Successful Op Transfer', 'Successful Transactional Email', 'Successful Transactional SMS', 'In Call (Min)', 'In Call (%)', 'Ready (Min)', 'Ready (%)', 'Wrapup (Min)', 'Wrapup (%)', 'Not Ready (Min)', 'Not Ready (%)', 'RPC : Payment/PTP', 'RPC : No Payment/PTP', 'WPC', 'Non-Contacts', 'Total RPCs']
RELEVANT_COLS = ['Date', 'Service', 'Successful Op Transfer', 'In Call (Min)', 'Ready (Min)', 'Wrapup (Min)', 'Not Ready (Min)', 'Average Ready Time (Min)']
FINAL_FILE_DIRECTORY = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_hci_summary'
FINAL_FILE_PREIFX = "Overall Average Ready Time"

# Log
LOG_OUTPUT = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_hci_summary/log.txt'
LOG_LEVEL = logging.INFO

# Email sending
SUBJECT = 'HCI_Agent_Summary_Report'
GENERIC_COMPLETE_FILE_NAME = 'Overall Average Ready'  # Complete file name (livevox_hci_summary folder)

today = datetime.now()
yesterday = today - timedelta(days=1)
yesterday_str = yesterday.strftime('%m-%d-%Y')

matching_files = glob.glob(f'{FINAL_FILE_DIRECTORY}/**/*{GENERIC_COMPLETE_FILE_NAME}*', recursive=True)
FILE_OUTPUT = None
FILE_NAME = None
if matching_files:
    for file_path in matching_files:
        if file_path.endswith(f' - {yesterday_str}.xlsx'):
            FILE_OUTPUT = file_path
            FILE_NAME = os.path.basename(file_path)
            print(f'File output: {FILE_OUTPUT}')
            break

RECEIVER_EMAIL = get_key(dotenv_path, 'RECEIVER_EMAIL')
SENDER_EMAIL = get_key(dotenv_path, 'SENDER_EMAIL')
GMAIL_APP_PASSWORD = get_key(dotenv_path, 'GMAIL_APP_PASSWORD')