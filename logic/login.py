#!/usr/bin/env python3
# login.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.util import *
import logging
from logic.logs import *

conf_log()

def log(driver, user_xpath, pass_xpath, login_xpath, user, password):
    try:
        search_user = driver.find_element(By.XPATH, user_xpath)
        search_user.send_keys(user)
        logging.info('User Added')
        search_user = driver.find_element(By.XPATH, pass_xpath)
        search_user.send_keys(password)
        logging.info('Password Added')
        login_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
        login_btn.click()
        logging.info('Next Clicked')

        time.sleep(1)

    except Exception as e:
        logging.error(f'Error: {e}')