import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)

    def post(self):
        user_input=self.request.get('user_input')
        self.response.out.write(form % user_input)


application = webapp2.WSGIApplication([
    ('/', MainPage),
      ('/documentary/?', DocumentaryFront),
      ('/documentary/([0-9]+)', PostPage),
      ('/documentary/newpost', NewPost),

], debug=True)