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


def ftp_down(filepath, localpath):
    return sftp.get(filepath, localpath)


def ftp_upl(localpath, filepath):
    return sftp.put(localpath, filepath)


def del_ftp(filepath):
    return sftp.remove(filepath)

a = True
while a:
    oper = input('Typ operacji: ')
    if oper == '1':
        filepath = input('Podaj plik z dysku: ')
        localpath = input('Podaj nazwe na dysku: ')
        print(filepath)
        print(localpath)
        ftp_down(filepath, localpath)
        if sftp: sftp.close()
        if transport: transport.close()

    elif oper == '2':
        filepath = input('Podaj plik do wyslania: ')
        localpath = input('Podaj nazwe na dysku: ')
        ftp_upl(localpath, filepath)
        if sftp: sftp.close()
        if transport: transport.close()

    elif oper == '3':
        filepath = input('Podaj plik do usuniecia: ')
        del_ftp(filepath)
        if sftp: sftp.close()
        if transport: transport.close()

    elif oper == '0':
        a = False
print('Dzięki za uwagę')