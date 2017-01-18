import logging
import webapp2
from model import Deal, Person
from google.appengine.api import mail
import email_helper


class Notify(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        people = Person.query().fetch()
        new_deals = Deal.filter(Deal.new == True).fetch()

        new_emails = {}

        try:
            for person in people:
                for new_deal in new_deals:
                    intersect = set(new_deal.keywords) & set(person.keywords)
                    if len(intersect) != 0:
                        if person.email not in new_emails:
                            new_emails[person.email] = []
                        new_emails[person.email].append(new_deal)

            for new_deal in new_deals:
                new_deal.new = False
                new_deal.put()

            for email, deals in new_emails.iteritems():
                message = mail.EmailMessage(subject='New Deals',
                                            sender=email_helper.SENDER)
                message.to = email
                message.body = email_helper.NEW_DEALS_MESSAGE.format(deals)
                message.send()

            self.response.write('OK')
        except urlfetch.Error:
            logging.exception('Caught exception fetching data')
            self.response.write('EXCEPTION')

app = webapp2.WSGIApplication([
    ('/notify', Notify),
], debug=True)
