import time
import datetime

first_list = []

for i in range(5):
    first_list.append(datetime.datetime.now())
    time.sleep(2)

print(first_list)