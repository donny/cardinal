import logging
import webapp2
from bs4 import BeautifulSoup
from google.appengine.api import urlfetch
from model import Deal


class Fetch(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        url = 'https://www.ozbargain.com.au/deals/feed'
        try:
            result = urlfetch.fetch(url, validate_certificate=True)
            if result.status_code == 200:
                soup = BeautifulSoup(result.content, 'xml')
                items = soup.findAll('item')
                for item in items:
                    title = item.title.text.encode('utf-8')
                    link = item.link.text.encode('utf-8')
                    description = item.description.text.encode('utf-8')

                    deal = Deal(id=link, title=title, link=link,
                                description=description)
                    deal.put()

                self.response.write('OK')
            else:
                self.response.write('ERROR')
        except urlfetch.Error:
            logging.exception('Caught exception fetching data')
            self.response.write('EXCEPTION')

app = webapp2.WSGIApplication([
    ('/fetch', Fetch),
], debug=True)
