import sys
from logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    error_message ='Error: ' + str(error) + ' in line : ' + str(exc_tb.tb_lineno) + '   ' 'File : ' + exc_tb.tb_frame.f_code.co_filename
    return error_message    

class CustomeException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)

    def __str__(self):
        return f'{self.error_message}'
    
if __name__ == "__main__":
    try:
        a = 10/0
    except Exception as e:
        logging.error(error_message_detail(e,sys))
        raise Exception(error_message_detail(e,sys))