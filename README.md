# cardinal

Cardinal is a [Google App Engine](https://cloud.google.com/appengine/) app that checks a popular [Australian bargain](https://www.ozbargain.com.au/) web site and emails deals that match users' keywords.

### Background

This project is part of [52projects](https://donny.github.io/52projects/) and the new stuff that I learn through this project: [Google Cloud Datastore](https://cloud.google.com/datastore/) and [Google App Engine](https://cloud.google.com/appengine/) (revisit).

I used Google App Engine (GAE) in the past,  around seven years ago, in [several](https://github.com/donny/meltrams-back-end) [apps](https://github.com/donny/melb-journey-back-end). I've been meaning to revisit, relearn, and use it again. And through this project, I use the GAE platform to check on a bargain web site that I frequently visit. [OzBargain](https://www.ozbargain.com.au/) is a popular Australian web site that lists user-submitted bargain deals. The submissions can be voted up or down to determine their positions on the site's pages.

### Project

Cardinal retrieves the new submissions periodically at intervals, checks for matching keywords, and emails users according to their matched keywords.

The main user interface to Cardinal is through email. Specifically, a user sends emails with specific subject lines to a predefined Cardinal email address.

### Implementation

### Conclusion


Before running or deploying this application, install the dependencies using
[pip](http://pip.readthedocs.io/en/stable/):

    pip install -t lib -r requirements.txt

For more information, see the [App Engine Standard README](../../README.md)
