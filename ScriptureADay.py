import Scriptures
import Subscribers
import smtplib
import datetime
import time

#Sprint [10 digit number]@messaging.sprintpcs.com
#T-Mobile []@tmomail.net
#US Cellular []@email.uscc.net
#Verizon []@vtext.com
#sprintMessage = '@messaging.sprintpcs.com'

day_of_year = datetime.datetime.now().timetuple().tm_yday
now = datetime.datetime.now()



fromMe = '365scriptureaday@gmail.com'
sendTo = Subscribers.sendTo

message = Scriptures.scriptures[day_of_year]


#setting up the time to check when to send the email.
year = now.year
month = now.month
day = now.day
hour = 9
minute = 30
second = 00
format = "%H:%M"

email_time = datetime.datetime(year,month,day,hour,minute,second)
send_time = email_time.strftime(format)
sent_emails = 0
while True:


    current_time = datetime.datetime.now()
    check_time = current_time.strftime(format)
    if sent_emails == 0:
        if send_time == check_time and sent_emails <= 0:
            # setting up the server to send the email
            smtObject = smtplib.SMTP('smtp.gmail.com', 587)
            smtObject.ehlo()
            smtObject.starttls()
            smtObject.login('365scriptureaday@gmail.com', '<password>')
            for person in sendTo:
                smtObject.sendmail(fromMe, person, str(message))

            smtObject.quit()
            sent_emails = 1
            print 'sent on ', datetime.datetime.now()

            time.sleep(60)
        elif send_time != check_time:
            sent_emails = 0
