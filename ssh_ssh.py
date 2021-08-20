import paramiko
import sys

paramiko.util.log_to_file("paramiko2.log")

hostname = "*****"
username = "*****8"
password = "qwaszx3232..PP"
port = 51619

commands = [
    "pwd",
    "id",
    "uname -a",
    "df -h",
    "ps aux"
]

tab = []

# initialize the SSH client
client = paramiko.SSHClient()
# # add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())



try:
    client.connect(hostname=hostname, username=username, password=password, port=port)
    for command in commands:
        with open("log.txt", 'a') as sys.stdout:
            print("=" * 50, command, "=" * 50)
            stdin, stdout, stderr = client.exec_command(command)
            print(stdout.read().decode())
            err = stderr.read().decode()
            if err:
                print(err)

except:
    print("[!] Cannot connect to the SSH Server")
    exit()