from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


def is_logged_in():
    return False  # TODO: Define function

def bootstrap_link():
    return '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">'


@app.route("/")
def index():
    return render_template('./Spoodazo.html')


@app.route("/login")
def login():
    html = """
        <!doctype html>
        <html lang="en">
            <head>
                <title>Login</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Tagesschrift&display=swap" rel="stylesheet">
                {bootstrap_link}
            </head>

            <body>
                <div class="container">
                    <div class="row">
                        <div class="col-3">
                            &nbsp;
                        </div>
                        <div class="col-3">
                            <div class="card mt-3">
                                <div class="card-header">
                                    <h4>Login</h4>
                                </div>
                                <div class="card-body">
                                </div>
                            </div>
                        </div>
                        <div class="col-3">
                            &nbsp;
                        </div>
                    </div>
                </div>
            </body>
        </html>
    """.format(bootstrap_link=bootstrap_link())

    return html
