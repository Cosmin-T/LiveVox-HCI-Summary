#!/usr/bin/env python3
# logs.py

import logging
from logic.util import *

def conf_log():
    logging.basicConfig(level=LOG_LEVEL,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename = LOG_OUTPUT,
                        filemode = 'a')