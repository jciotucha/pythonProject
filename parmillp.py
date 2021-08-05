import paramiko

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
filepath = "/Diuna.txt"
localpath = "Diuna2.txt"
sftp.get(filepath, localpath)

# Upload
# filepath = "/"
# localpath = "e:/device.xml"
# sftp.put(localpath, filepath)

# Close
if sftp: sftp.close()
if transport: transport.close()