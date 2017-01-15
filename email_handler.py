import logging
import webapp2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler


class EmailHandler(InboundMailHandler):

    def receive(self, mail_message):
        logging.info("RECV: " + mail_message.sender +
                     " : " + mail_message.subject)


app = webapp2.WSGIApplication([
    EmailHandler.mapping()
], debug=True)
