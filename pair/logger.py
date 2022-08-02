from datetime import datetime as dt
from time import time
def calc_logger(data):
    time = dt.now()
    with open('log.txt', 'a') as file:
        file.write('{};math;{}\n'
                    .format(time, data))