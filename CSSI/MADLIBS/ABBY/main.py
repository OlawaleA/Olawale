
import webapp2
import json

import urllib
import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        giphy_data_source = urllib.urlopen(
            "https://media2.giphy.com/media/mksx7SSd2QhP2/giphy.gif?fingerprint=e1bb72ff59931519584c707063c32b07")
        giphy_json_content = giphy_data_source.read()
        parsed_giphy_dictionary = json.loads(giphy_json_content)
        gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        self.response.write(gif_url)

class GipHandler(webapp2.RequestHandler):
    def get(self):
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': 'cristiano ronaldo', 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}

        giphy_response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()
        json_data =json.loads(giphy_response)
        img_url = json_data['data'][0]['images']['original']['url']
        template_vars= {'url': img_url}

        main_template = env.get_template('abby.html')
        self.response.out.write(main_template.render(template_vars))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/gip', GipHandler)
], debug=True)
