from datetime import datetime as dt
from time import time
def data_logger(data):
    time = dt.now()
    with open('log.txt', 'a') as file:
        file.write('{};datachange;{}\n'
                    .format(time, data))