import pysftp




# cnopts = pysftp.CnOpts(knownhosts='c:\users\Aga\known_hosts')
# cnopts.hostkeys = None

cnopts = pysftp.CnOpts()
cnopts = pysftp.CnOpts(knownhosts='C:\\Users\\Aga\\known_hosts')
# cnopts.hostkeys = None

myHostname = "85.14.106.186"
myUsername = "pppppp"
myPassword = "pppppp"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, port=2222, cnopts=cnopts) as sftp:
    print
    "Connection succesfully stablished ... "

    # Switch to a remote directory
    sftp.cwd('/')

    # Obtain structure of the remote directory '/var/www/vhosts'
    directory_structure = sftp.listdir_attr()
    # Print data
    for attr in directory_structure:
        print
        attr.filename, attr

# connection closed automatically at the end of the with-block
