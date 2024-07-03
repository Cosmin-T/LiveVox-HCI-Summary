#!/usr/bin/env python3
# main.py

from logic.util import *
from logic.webdriver import *
from logic.login import *
from logic.navigation import *
from logic.dates import *
from logic.process import *
from logic.send_email import *


def app():
    move_older_files()

    driver = initialize_webdriver(URL)
    log(driver, USER_XPATH, PASSWORD_XPATH, LOGIN_XPATH, USER, PASSWORD)
    review(driver, REVIEW_XPATH, AGENT_REPORTS_XPATH, AGENT_SUMMARY_XPATH)

    add_dates(driver, FROM_DATE_ID)
    add_dates(driver, TO_DATE_ID)
    for hci_agent in HCI_AGENT_LIST:
        nav(driver, hci_agent, SERVICE_FORMAT, SERVICE_TYPE_XPATH, QUICK_CONNECT)
        time.sleep(1)
        try:
            generate(driver, GENERATE_CLASS, EXPORT_XPATH, EXCEL_XPATH, hci_agent)
            logging.info(f'Generated Successfully')
            logging.info(f'Downloading Successfully\n')
        except Exception as e:
            logging.error(f'Error: {e}')

    time.sleep(2)

    append_files(FILE_PATH1, GENERIC_FILE_NAME)
    append_new_data()
    send()
    delete_downloaded_files(FILE_PATH1, GENERIC_FILE_NAME)
    logging.info('Done')
    logging.info('---------------------------------------------------\n\n')


if __name__ == '__main__':
    app()