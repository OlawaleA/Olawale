import json
import urllib

import jinja2
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('main.html')
        self.response.out.write(main_template.render())
    def post(self): ## here's the new POST method in the MainHandler
        self.response.out.write("You have submitted your madlib")

class JsonHandler(webapp2.RequestHandler):
    def get(self):
        response = urllib.urlopen("https://uinames.com/api/")
        content = response.read()
        content_dict = json.loads(content)
        main_template = env.get_template('names.html')

        self.response.out.write(main_template.render(content_dict))




app = webapp2.WSGIApplication(
    [
        ('/', MainHandler),
        ('/names',JsonHandler)
    ],
    debug=False
)
