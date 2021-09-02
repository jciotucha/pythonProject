from ftplib import FTP

filename = 'lista.txt'
# host = "pepli.pl"
# port = '51619'
# username = 'pppppp'
# password = 'pppppp'
host = "ftp.uni-kl.de"
ftp = FTP(host)  # connect to host, default port
# ftp.connect(username, password)
ftp.login()  # user anonymous, passwd anonymous@

ftp.retrlines('LIST')  # list directory contents
respMessage = ftp.getwelcome()
getFile = ftp, 'robots.txt'
print(respMessage)
respMessage2 = ftp.pwd()
print(respMessage2)
ftp.cwd('/pub/')
ftp.retrlines('LIST')

ftp.quit()