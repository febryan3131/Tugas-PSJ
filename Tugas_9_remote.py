import paramiko
import sys

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
print('---- Connecting ----')
ip = sys.argv[1]
client.connect(ip,username='febryan',password='bismillah123')

stdin, stdout, stderr = client.exec_command("free | awk 'FNR == 2 {print ($4/$2)*100}'")
for line in stdout:
	print("free memory at " + ip+ " = "+line.strip('\n') +" %")


client.close()
del client, stdin, stdout, stderr

