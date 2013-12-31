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
                    <li><a href="#">Interview Prep</a></li>
                    <li><a href="#">Interviews</a></li>
                    <li><a href="#">Project</a></li>
                    <li><a href="#">Women in Tech</a></li>
                </ul>
            </div>
         </nav>
    </div>
    <div class="jumbotron" style="background-color:white;">
        <img>
        <h2><i>Bay Area Tech Girl</i></h2>
        <p>Hi, My name is <b>Yayoi Ukai</b>. I am a Software Engineer. I studied computer science and engineering at UC Davis and \
        currently I live in San Francisco and looking for job. \
        This is my work in progress website and a blog. I put an interesting technical bits and pieces on this website.\
        I hope this site is something interesting or useful. </p>
        <h3>Welcome!</h3>

    </div>
    <div class="row">
    <div class="col-md-3 col-sm-6">
    <h4><span class="glyphicon glyphicon-film"></span>Interview Prep</h4>
    <p>As I am looking for a job, it is super important to be able to do well on the interviews. \
    All my codes are in github but this section has an update for my interivew prep. </p>
    <p>Read More >></p>
    </div>
    <div class="col-md-3 col-sm-6" style="background-color:#FFFF91;">
     <h4><span class="glyphicon glyphicon-book"></span>Interviews</h4>
     <p>I am always interested in what other fellow Software Engineers are doing. So I decided to interview them. \
     read my interview correction here.</p>
     <p>Read More >></p>
     </p>
     </div>
     <div class="col-md-3 col-sm-6" style="background-color:#B8FF94;">
     <h4><span class="glyphicon glyphicon-pencil"></span>Projects </h4>
     <p>This is the section that slightly bigger project that I am working on \
     such as this website. Or I am also working on maze generator and solver. So any update \
     on my projects goes here. 
      </p>
     <p>Read More >></p>
     </div>
    <div class="col-md-3 col-sm-6" style="background-color:#FFB2D1;">
     <h4><span class="glyphicon glyphicon-star" ></span>Women in TECH</h4>
     Anything related to women in tech. 
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