#!/usr/bin/env python3
# navigation.py

import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from logic.util import *
import logging
from logic.logs import *
import os
from datetime import datetime, timedelta

conf_log()

def review(driver, review_tab, agent_reports_expander, agent_summary_tab):
    try:
        review_selector = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, review_tab)))
        review_selector.click()
        logging.info('Review Clicked')

        agent_reports_selector = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, agent_reports_expander)))
        agent_reports_selector.click()
        logging.info('Agent Reports Clicked')

        agent_summary_selector = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, agent_summary_tab)))
        agent_summary_selector.click()
        logging.info('Agent Summary Report Clicked')

    except Exception as e:
        logging.error(f'Error: {e}')

def nav(driver, hci_agent_list, service_format, quick_connect_xpath, quick_connect):
    try:
        quick_connext_selector = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, quick_connect_xpath)))
        quick_connext_selector.send_keys(quick_connect + Keys.ENTER)
        logging.info('Quick Connect Clicked')

        service_format = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, service_format)))
        service_format.send_keys(hci_agent_list + Keys.ENTER)
        logging.info(f'Service Format {hci_agent_list} Clicked')
    except Exception as e:
        logging.error(f'Error: {e}')


def generate(driver, generate_class, export_xpath, excel_xpath, hci_agent):
    gen = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, generate_class)))
    gen.click()

    time.sleep(1)

    try:
        export_dropdown = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, export_xpath)))
        if export_dropdown.is_displayed():
            export_dropdown.click()

            time.sleep(1)

            excel_selector = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, excel_xpath)))
            excel_selector.click()
        else:
            logging.warning('Export dropdown element not found')
    except TimeoutException:
        logging.warning('Export dropdown element not found or button is greyed out')

    time.sleep(2)
    file_rename(hci_agent)

def file_rename(agent_name):
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_str = yesterday.strftime('%m_%d_%Y')
    for file_name in os.listdir(FILE_PATH1):
        if file_name.startswith(GENERIC_NAME):
            specific_name = file_name[len(GENERIC_NAME):]
            new_name = f'{agent_name}_{yesterday_str}.xls'
            os.rename(os.path.join(FILE_PATH1, file_name), os.path.join(FILE_PATH1, new_name))
            logging.info(f'Renamed file {file_name} to: {new_name}')