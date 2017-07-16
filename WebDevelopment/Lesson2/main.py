import webapp2

form = """
<h>Enter some text to ROT13:</h>
<br>
<textarea></textarea>
<br>
<input type="submit"></input>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)