# print(bytes([0x41, 0x42, 0x43, 0x44, 0x45]))

import datetime

# from time import sleep

print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
print(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S.%f %p"))
print(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S.%f %p %Z"))
print(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S.%f %p %Z %z"))

# while True:
#     print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"))
#     sleep(1)
