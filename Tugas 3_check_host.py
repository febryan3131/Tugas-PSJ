import os
import sys
import subprocess


if len(sys.argv) < 2:
    print('Gagal: IP Address belum diberikan')
else: 
    tes = sys.argv[1]
    if tes.count(".") < 3:
        print(tes, "Bukan IP")
    else:
        response = subprocess.call(["ping", "-n", "1", tes], stdout=subprocess.DEVNULL, 
        stderr=subprocess.STDOUT)
        if response == 0:
            print("Host", tes, "is UP!")
        else:
            print("Host", tes, "is DOWN!")
