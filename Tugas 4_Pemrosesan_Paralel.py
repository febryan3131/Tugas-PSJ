import os
import subprocess
import time

T1 = time.perf_counter()
hosts = ["192.168.1.1","192.168.1.2","192.168.1.3","8.8.8.8","8.8.4.4","111.111.111.1"]
def png(ip):
    response = subprocess.call(["ping", "-n", "1", ip], stdout=subprocess.DEVNULL, 
    stderr=subprocess.STDOUT)
    if response == 0:
        status = "Up"
    else:
        status = "Down"
    return f"Host {ip} is {status}"

for ip in hosts:
    print(png(ip))

T2 = time.perf_counter()
print(f"selesai dalam {round(T2-T1)} detik")