import logging
import webapp2
import re
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api import mail
from model import Person
import email_helper


class EmailHandler(InboundMailHandler):

    def receive(self, mail_message):
        logging.info("RECV: " + mail_message.sender +
                     " : " + mail_message.subject)

        message = mail.EmailMessage(subject='Info',
                                    sender=email_helper.SENDER)
        message.to = mail_message.sender

        subject = mail_message.subject.lower()

        if subject.startswith('subscribe'):
            sender = mail_message.sender
            keywords = re.sub(r'\W+', ' ', subject)
            keywords = keywords.split(' ')
            if len(keywords) <= 1:
                message.body = email_helper.HELP_MESSAGE
            else:
                keywords.pop(0)  # To remove 'subscribe'
                person = Person(id=sender, email=sender,
                                keywords=keywords)
                person.put()

        elif subject.startswith('help'):
            message.body = email_helper.HELP_MESSAGE

        else:
            return

        message.send()


app = webapp2.WSGIApplication([
    EmailHandler.mapping()
], debug=True)
