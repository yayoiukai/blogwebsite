import webapp2


form="""<html>
     <head>
    <meta charset="utf-8">

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="bootstrap/css/custom.css" ref="stylesheet">
    <script src="bootstrap/js/respond.js"></script>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Grid Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.css" rel="stylesheet">
	<style>
		body {
			padding: 50px 16px;
			background-color:#F8F8F8;

		}
		.container {
		  padding: 0 1em;
		  background-color:white;
		  width:90%;
		  align:center;
		}

		h4 {
		  margin-top: 1.5em;
		}
		.row {
		  margin-bottom: 1.5em;
		}
		.row .row {
		  margin-top: 0.8em;
		  margin-bottom: 0;
		}
		[class*="col-"] {
		  padding: 1em 0;
		  background-color:#99ADEB;
          border-radius:25px;
          padding: 0px 0px 15px 15px;

}

	</style>
    <body>
    <div class="container">
    <div class="row">
    	<nav class="navbar navbar-default navbar-fixed-top navbar-inverse">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#collapse">
                  <span class="sr-only">Toggle navigation</span>
                  <span class="glyphicon glyphicon-arrow-down"></span>
                  MENU
                </button>
            </div>
            <div class="collapse navbar-collapse" id="collapse">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="#">Home</a></li>
                    <li><a href="#">Documentary</a></li>
                    <li><a href="#">Education</a></li>
                    <li><a href="#">Culture</a></li>
                    <li><a href="#">About</a></li>
                </ul>
            </div>
         </nav>
    </div>
    <div class="jumbotron" style="background-color:white;">
        <img>
        <h2><i>Documentary, Education, and Culture</i></h2>
        <p>Hi, My name is <b>Yayoi Ukai</b>. I am a <b>Software Engineer</b>. I made this website to share some of my thoughts.
        I plan to write about documentaries I watched (huge fan of documentaries.) and some education issues/culture \
         issues I am interested in. I hope this site is something interesting or useful. </p>
        <h3>Welcome!</h3>

    </div>
    <div class="row">
    <div class="col-md-3 col-sm-6">
    <h4><span class="glyphicon glyphicon-film"></span>Documentary</h4>
    <p>I watch a lot of documentaries every week. My favorite genres are politics, social issues, technology, and sciences \
    My recent favorate was "Park Avenue", "1%","flaw", and "Davis vs Monsato". I write my reviews of each documentary I watched here.</p>
    <p>Read More >></p>
    </div>
    <div class="col-md-3 col-sm-6" style="background-color:#FFFF91;">
     <h4><span class="glyphicon glyphicon-book"></span>Education</h4>
     <p>I am always interested in learning new things. I also think that our higher education system is deeply in danger. \
     California school system went through hugh tuition hike and budget cut and student loans are big issues too. \
     I write about anything related to learning and education here.
     <p>Read More >></p>
     </p>
     </div>
     <div class="col-md-3 col-sm-6" style="background-color:#B8FF94;">
     <h4><span class="glyphicon glyphicon-pencil"></span>Culture</h4>
     <p>I am originally from Japan and I live in the U.S. more than 10 years now. I love languages, traveling and cooking. \
     So I write about anything that is related to culture and languages. </p>
     <p>Read More >></p>
     </div>
      <div class="col-md-3 col-sm-6" style="background-color:#FFB2D1;">
     <h4><span class="glyphicon glyphicon-star" ></span>About</h4>
     About me and this website. You can read about me more or you can also read about construct of this website. This is twitter bootstrap
     and google app engine backend (Python).
     <p>Read More >></p>
     </div>
     </div>



    </div> <!-- end of container -->
    </body>
     <script src="http://code.jquery.com/jquery-latest.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    </html>

    """

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