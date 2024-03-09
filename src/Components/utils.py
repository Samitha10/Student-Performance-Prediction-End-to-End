import os, sys
import pandas as pd
import numpy as np

from src.expt import error_message_detail
from src.logger import logging
import pickle

def save_object(file_path,obj):
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
        logging.info(f"Object saved at: {file_path}")
    except Exception as e:
        error_message_detail(e)