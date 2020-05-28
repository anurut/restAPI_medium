# First import the class Flask from the module flask
from flask import Flask

# Create an object of Class Flask
app = Flask(__name__)


# Create a base route (called endpoints in REST API terms)
@app.route('/')
def index():
    return '<H1> Welcome to Flask tutorial</H1>'


# Run the app
if __name__ == '__main__':
    app.run()
