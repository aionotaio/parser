import os
import sys
from pathlib import Path


if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.absolute()

LOGS_DIR = os.path.join(ROOT_DIR, 'logs')
LOGS_PATH = os.path.join(LOGS_DIR, 'logs.txt')

RES_DIR = os.path.join(ROOT_DIR, 'results')
RES_PATH = os.path.join(RES_DIR, 'data.csv')

SLEEP_DELAY = [50, 80] 
MAX_ATTEMPTS = 3 