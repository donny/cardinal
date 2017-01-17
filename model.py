from google.appengine.ext import ndb

class Deal(ndb.Model):
    title = ndb.StringProperty()
    link = ndb.StringProperty()
    description = ndb.TextProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class Person(ndb.Model):
    email = ndb.StringProperty()
    keywords = ndb.StringProperty(repeated=True)
