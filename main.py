import pandas
import datetime as dt
import random
import smtplib

today = dt.datetime.now()
today_monthday = (today.month, today.day)

csv = pandas.read_csv("birthdays.csv")
birthday = {(row.month, row.day): row for (index, row) in csv.iterrows()}

my_email = "fakeemail43066@gmail.com"
my_password = "chtf fklg uscx lwbj"

if today_monthday in birthday:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        birthday_person = birthday[today_monthday]
        letter = letter_file.readlines()
        old_letter =' '.join(map(str, letter))
        new_letter = old_letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{new_letter}")