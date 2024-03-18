#!/usr/bin/env python3
# dates.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from logic.util import *
import logging
from logic.logs import *

conf_log()

def add_dates(driver, input_id):
    try:
        date_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, input_id)))
        current_date_str = date_input.get_attribute("value")
        logging.info(f'Current Date String: {current_date_str}')

        current_date = datetime.strptime(current_date_str, "%m/%d/%Y")
        today = datetime.now().date()
        logging.info(f'Current Date: {current_date.date()} Today:, {today}')

        if current_date.date() == today:
            logging.info("Dates match")
            yesterday = today - timedelta(days=1)
            yesterday_str = yesterday.strftime('%m/%d/%Y')

            date_input.clear()
            date_input.send_keys(yesterday_str)
            logging.info(f'SET {yesterday_str}')
    except Exception as e:
        logging.error(f'Error: {e}')