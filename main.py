import logging
import webapp2
from bs4 import BeautifulSoup
from google.appengine.api import urlfetch


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

        url = 'https://www.ozbargain.com.au/deals/feed'
        try:
            result = urlfetch.fetch(url, validate_certificate=True)
            if result.status_code == 200:
                data = result.content
                soup = BeautifulSoup(data, 'xml')
                items = soup.findAll('item')
                for item in items:
                    title = item.title.text
                    link = item.link.text
                    description = item.description.text
                    print title.encode('utf-8')
                    print link.encode('utf-8')
                    print description.encode('utf-8')

                self.response.write(str(result.status_code))
            else:
                self.response.write(str(result.status_code))
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')
            self.response.write("ERROR")

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
