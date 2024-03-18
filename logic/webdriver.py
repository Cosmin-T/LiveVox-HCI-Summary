#!/usr/bin/env python3
# webdriver.py

import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from logic.util import *
import time
import logging
from logic.logs import *

conf_log()

def initialize_webdriver(URL):
    """Opens a Chrome browser in headless mode, visits the specified URL, and waits for the page to fully load.

    Args:
        url (str): The URL to visit.

    Returns:
        webdriver.Chrome: The Chrome webdriver instance, or None if an error occurs.
    """
    try:
        # Get the path to the directory where your script is located
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

        # Define the relative path to the Chrome WebDriver executable within the bundle
        webdriver_path = os.path.join(script_dir, CROMEDRIVER_PATH)

        # Creating ChromeOptions instance for headless mode
        chrome_options = Options()
        # chrome_options.add_argument('--headless')  # Run Chrome in headless mode

        # Creating the Chrome driver instance with the specified options and WebDriver path
        driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

        # Setting the size of the Chrome window (not necessary in headless mode)
        driver.set_window_size(1400, 1440)

        # Entering the URL to the Chrome driver instance
        driver.get(URL)

        # Returning the Chrome driver instance
        return driver

    except Exception as e:
        logging.error('Error getting Chrome driver:', str(e))
        return None