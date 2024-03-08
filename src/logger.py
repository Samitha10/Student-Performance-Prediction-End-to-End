import logging,os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M')}.log"
logs = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs, LOG_FILE)

# Move the log file inside the 'logs' folder
logging.basicConfig(
    filename=LOG_FILE_PATH, 
    level=logging.INFO, 
    format='%(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    logging.info('Logging Started')