import webapp2
import cgi

form = """
<h>Enter some text to ROT13:</h>
<br>
<form method="post">
    <textarea name="text">%(textInput)s</textarea>
    <br>
    <input type="submit"></input>
</form>
"""



def get_rot13(text):
    encrypted = ""
    for char in text:
        value_of_char = ord(char)
        new_value_of_char = value_of_char + 13

        if ord('a') <= value_of_char <= ord('z'):
            if new_value_of_char > ord('z'):
                new_value_of_char = ord('a') + (new_value_of_char - ord('z') - 1)
        elif 64 < value_of_char < 91:
            if new_value_of_char > 90:
                new_value_of_char = 65 + (new_value_of_char - 91)
        else:
            new_value_of_char = value_of_char

        char = chr(new_value_of_char)
        encrypted += char
    return encrypted

class MainPage(webapp2.RequestHandler):
    def write_form(self, textIn=""):
        self.response.out.write(form % {"textInput": textIn})

    def get(self):
        self.write_form()
    
    def post(self):
        text_output = get_rot13(self.request.get('text'))
        text_output = cgi.escape(text_output, quote=True)
        self.write_form(text_output)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)