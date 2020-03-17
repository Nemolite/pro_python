from ftplib import FTP

ftp = FTP('localhost')

print(ftp)

dss = ftp.login('admin','123') 

print(dss)

ftp.retrlines('LIST') 

filename = 'D:\\bcb\\Python\\exfile2.xlsx'

f = open(filename, 'wb')

print(f)

send = ftp.retrbinary("STOR "+ "exfile2.xlsx", f)

ftp.quit()



