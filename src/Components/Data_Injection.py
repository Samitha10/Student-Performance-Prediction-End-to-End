import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.expt import CustomeException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass #This is a decorator that is used to create a dataclass. It is a part of the dataclasses module which is provided by Python 3.7 and later.
class DataInjectionConfig:
    train_data_path: str=os.path.join('src', 'Components', 'artifacts', 'train.csv')
    test_data_path: str=os.path.join('src', 'Components', 'artifacts', 'test.csv')
    raw_data_path: str=os.path.join('src', 'Components', 'artifacts', 'raw.csv')
class DataInjection:
    def __init__(self):
        self.config = DataInjectionConfig()

    def initiate_data_injection(self):
        try:
            logging.info('Data Injection Started')
            logging.info('Reading Raw Data')
            data = pd.read_csv(self.config.raw_data_path)#If the folder or file can be created or data can be read from cloud storage, then the path can be updated here
            logging.info('Data Reading Completed')
            logging.info('Splitting Data into Train and Test')
            train, test = train_test_split(data, test_size=0.2, random_state=42)
            logging.info('Data Splitting Completed')
            logging.info('Saving Train and Test Data')
            train.to_csv(self.config.train_data_path, index=False, header=True)
            test.to_csv(self.config.test_data_path, index=False, header=True)
            logging.info('Data Injection Completed')

            return(
                self.config.train_data_path,
                self.config.test_data_path
            )
        except Exception as e:
            error_message = CustomeException(e,sys)
            logging.error(error_message)
            raise Exception(error_message)

if __name__=="__main__":
    obj = DataInjection()
    train_data, test_data = obj.initiate_data_injection()
    print(train_data, test_data)

    