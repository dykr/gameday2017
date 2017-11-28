from flask import Flask, send_from_directory, Response, make_response
from webserver import app
from webserver import set_header

# add a rule for the index page.
#@app.route('/', defaults={'file': 'index.html'})
@app.route('/')
@app.route('/index.html')
#def serve_results(file):
def serve_results():
    html_content = '''<!DOCTYPE html> <html lang="en"><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Unicorn.Rentals DRAFT FINAL WEBSITE</title>

        <!-- Bootstrap -->
        <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
        <!-- custom css -->
        <link href="css/style.css" rel="stylesheet" type="text/css" media="screen">
        <!-- font awesome for icons -->
        <link href="font-awesome-4.1.0/css/font-awesome.min.css" rel="stylesheet">

        <!-- animated css  -->
        <link href="css/animate.css" rel="stylesheet" type="text/css" media="screen">
        <!--web fonts-->
        <link href='http://fonts.googleapis.com/css?family=Raleway:400,900,500' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Lobster' rel='stylesheet' type='text/css'>

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->


    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-md-12 text-center">
                    <h1 class="soon-logo"><img src="img/FinalLogo.svg" width="250" height="250"><br />Unicorn.Rentals</h1>
                    <div class="soon-info-text">
                        <p class="lead">disruptive innovation on a global scale <br />making the world a better place for everyone</p>
                    </div>
                    <div class="soon-info-text">
                        <h1 class="Display-4"><a href = "text/rentals.html">Rent a Unicorn</a></h1><h1 class="Display-4"> <a href = "text/spot.html">NEW! Spot Market for Unicorns </a></h1><h1 class="Display-4"><a href = "text/leases.html">Lease a Unicorn</a></h1>
                    </div>
                </div>
            </div><!--intro text row-->
            <div class="row">
                <div class="col-md-12 text-center">
                    <div id="defaultCountdown"></div><!--countdown-->
                </div>
            </div><!--countdown row-->
        </div><!--.container-->
        <div class="container">
            <div class="row">
                <div class="col-md-12 text-center animated fadeInLeft">

                    <form class="form-inline soon-form" role="form">
                          <h4>Do you want to know more?</h4>
                        <a href="https://aws.amazon.com/summits/new-york/activities/" class="btn-white-border btn btn-lg">Elucidation</a>
                        <!-- <button type="submit" class="btn-theme-color btn btn-lg">Notify me</button> -->
                    </form>
                </div>
            </div>
        </div>
        <footer id="footer">
            <span>&copy;2016</span>
        </footer><!--footer-->
        <!--scripts and plugins -->
        <!--must need plugin jquery-->
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
        <!--bootstrap js plugin-->
        <script src="bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
        <!--easing plugin for smooth scroll-->
        <script src="js/jquery.easing.1.3.min.js" type="text/javascript"></script>
        <script src="js/jquery.backstretch.min.js" type="text/javascript"></script>
        <!--customizable plugin edit according to your needs-->
        <script src="js/custom.js" type="text/javascript"></script>
        <!--countdown coming soon-->
        <script src="js/jquery.countdown.js" type="text/javascript"></script>
        <script type="text/javascript">
            $(function() {
                var austDay = new Date();
                austDay = new Date(2016, 8 - 1, 10, 09);
                $("#defaultCountdown").countdown({until: austDay});
                $("#year").text(austDay.getFullYear());
            });
        </script>

    </body>
</html>
'''
    response = Response(html_content)
    response.headers["X-gameday-wheres-my-website-response"] = set_header.뭴("index_html")
    return response
@app.route('/css/<path:filename>')
def serve_css(filename):
    response = make_response(send_from_directory("css", filename))
    response.headers["X-gameday-wheres-my-website-response"] = set_header.뭴("css")
    return response
@app.route('/text/<path:filename>')
def serve_text(filename):
    response = make_response(send_from_directory("text", filename))
    response.headers["X-gameday-wheres-my-website-response"] = set_header.뭴("text")
    return response
@app.route('/bootstrap/<path:filename>')
def serve_bootstrap(filename):
    response = make_response(send_from_directory("bootstrap", filename))
    response.headers["X-gameday-wheres-my-website-response"] = set_header.뭴("bootstrap")
    return response
@app.route('/font-awesome-4.1.0/<path:filename>')
def serve_fontawesome(filename):
    response = make_response(send_from_directory("font-awesome-4.1.0", filename))
    response.headers["X-gameday-wheres-my-website-response"] = set_header.뭴("font-awesome-4.1.0")
    return response
@app.route('/js/<path:filename>')
def serve_js(filename):
    response = make_response(send_from_directory("js", filename))
    response.headers["X-gameday-wheres-my-website-response"] = set_header.뭴("js")
    return response
@app.route('/img/<path:filename>')
def serve_img(filename):
    response = make_response(send_from_directory("img", filename))
    response.headers["X-gameday-wheres-my-website-response"] = set_header.뭴("img")
    return response
