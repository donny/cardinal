import logging
from flask import Flask
from bs4 import BeautifulSoup
from google.appengine.api import urlfetch

app = Flask(__name__)


@app.route('/')
def hello():

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

            return str(result.status_code)
        else:
            return str(result.status_code)
    except urlfetch.Error:
        logging.exception('Caught exception fetching url')
        return 'ERROR'


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
