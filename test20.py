from ftplib import FTP

ftp = FTP('localhost')

print(ftp)

dss = ftp.login('admin','123') 

print(dss)

ftp.retrlines('LIST') 

filename = 'D:\\bcb\\Python\\test.py'

f = open(filename, 'wb')

print(f)

send = ftp.retrbinary("STOR "+ "test.py", f)

ftp.quit()



