"""
A simple python program to send email from a gmail account to any other mail service
"""
from smtplib import SMTP, SMTPAuthenticationError
import getpass
host="smtp.gmail.com"
port=587 #will be different for different email services
username=input("Enter your mail id:\n")
password=getpass.getpass()
email_conn=SMTP(host, port)
email_conn.ehlo()#to view these messages write inside print statement
email_conn.starttls()#to view these messages write inside print statement
try:
    email_conn.login(username, password)
    to_list=list(input("Enter recipients mail id seperated by a comma:\n").split(","))
    message_text=input("Enter your message:\n")
    email_conn.sendmail(username,to_list,message_text)
except SMTPAuthenticationError:
    print("Could not log in. Please check username and password.")
except:
    print("Some error occured mail not sent. Sorry!")


email_conn.quit()#to logout
