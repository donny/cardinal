from google.appengine.ext import ndb

class Deal(ndb.Model):
    title = ndb.StringProperty()
    link = ndb.StringProperty()
    description = ndb.TextProperty()
