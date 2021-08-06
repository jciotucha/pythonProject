import paramiko
import os

paramiko.util.log_to_file("paramiko.log")

# Open a transport
host, port = "85.14.106.186", 2222
transport = paramiko.Transport((host, port))

# Auth
username, password = "pppppp", "pppppp"
transport.connect(None, username, password)

# Go!
sftp = paramiko.SFTPClient.from_transport(transport)

# Download
# filepath = "/tt.pdf"
# localpath = "tt.pdf"
# sftp.get(filepath, localpath)


# Upload
filepath = "/[A-z].txt"
# localpath = "Diuna2.txt"
# sftp.put(localpath, filepath)

# Delete

sftp.remove(filepath)


# os.remove("Diuna2.txt")


# Close
if sftp: sftp.close()
if transport: transport.close()
