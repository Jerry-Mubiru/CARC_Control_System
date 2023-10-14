#import the Deliverable class
from deliverable import Deliverable
import yagmail

#class definition of the email sending class
class Email_carc:
    
    #define a function
    @staticmethod
    def send_email(deliverable: Deliverable):
        #create an email client and authenticate
        yag_client = yagmail.SMTP(deliverable.FROM_ADDRESS, oauth2_file='CARC_Secret_Authentication_file.json')
        yag_client.login()
        #send the email with the deliverable's information
        yag_client.send(
            to = deliverable.TO_ADDRESS, 
            subject = deliverable.email_subject, 
            contents = deliverable.email_message + '\n Sincerely, \n Case Amateur Radio Club.'
            )
        print("email sent")