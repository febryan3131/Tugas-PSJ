import os

hostname = "192.168.43.34"
response = os.system("ping -c 1 " + hostname)

if response == 0:
    print(hostname, "UP")
else:
    print(hostname, "DOWN")