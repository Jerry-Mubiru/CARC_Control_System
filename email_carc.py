#import the Deliverable class
from deliverable import Deliverable
import smtplib

#class definition of the email sending class
class Email_carc:
    #stores the password to the email address
    password = "<<insert password here>>"
    #define a function
    @staticmethod
    def send_email(deliverable: Deliverable):
        #create an email client
        smtp_client = smtplib.SMTP('smtp.gmail.com', 587)
        #call the ehlo function
        smtp_client.ehlo()
        #Start a tls connection
        smtp_client.starttls()
        #login to the email account
        smtp_client.login(deliverable.FROM_ADDRESS, Email_carc.password)
        #send the email with the deliverable's information
        smtp_client.sendmail(deliverable.FROM_ADDRESS, deliverable.TO_ADDRESS, f'Subject:{deliverable.email_subject}\n {deliverable.email_message}\n Sincerely, \n Case Amateur Radio Club.')
        #close the connection
        smtp_client.quit()