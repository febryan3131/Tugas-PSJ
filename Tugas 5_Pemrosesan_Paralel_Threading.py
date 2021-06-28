import os
import subprocess
import time
import threading

T1 = time.perf_counter()

def png(data):
    response = subprocess.call(["ping", "-n", "1", data], stdout=subprocess.DEVNULL, 
    stderr=subprocess.STDOUT)
    if response == 0:
        status = "Up"
    else:
        status = "Down"
    print(f"Host {data} is {status}")

Threads = []
hosts = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '8.8.8.8', '8.8.4.4']

for x in range(len(hosts)):
    CK = threading.Thread(target=png, args=[hosts[x]])
    CK.start()
    Threads.append(CK)

for t in Threads :
    t.join()


T2 = time.perf_counter()
print(f"selesai dalam {round(T2-T1)} detik")