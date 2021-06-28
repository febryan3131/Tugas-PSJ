import os
import subprocess
import time
import datetime
import threading

f = open('hosts.cfg')

def png(data):
    g = open('report.csv', 'a')
    dt = datetime.datetime.now()
    dt = dt.strftime("%m-%d-%Y %H:%M:%S")
    response = subprocess.call(["ping", "-n", "1", data], stdout=subprocess.DEVNULL, 
    stderr=subprocess.STDOUT)
    if response == 0:
        status = "Up"
    else:
        status = "Down"
    print(f"{dt};{data};{status}")
    g.write(f"{dt};{data};{status}\n")
    g.close()
    

hosts = []
for ip in f:
    ip = ip.strip()
    hosts.append(ip)

while True:
    print("\n")
    print("Mulai Monitoring...")
    time.sleep(2)
    T1 = time.perf_counter()
    Threads = []
    for x in range(len(hosts)):
        CK = threading.Thread(target=png, args=[hosts[x]])
        CK.start()
        Threads.append(CK)

    for t in Threads :
        t.join()
    T2 = time.perf_counter()
    print(f"selesai dalam {round(T2-T1, 2)} detik")
    time.sleep(10)
        
