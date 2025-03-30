#import smtplib

#my_email="cabhirup69@gmail.com"
#password="mysy hjln elqt dzqz"

#connection=smtplib.SMTP("smtp.gmail.com",587)
#connection.starttls()
#connection.login(user=my_email,password=password)
#connection.sendmail(from_addr=my_email,to_addrs="hthere12393@myyahoo.com",msg="hello there")
#connection.close()

import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
day_of_week=now.weekday()
print(day_of_week)

date_of_birth=dt.datetime(year=1995,month=12,day=15,hour=4)
print(date_of_birth)