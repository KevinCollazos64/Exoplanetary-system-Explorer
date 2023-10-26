from flask import Flask, render_template
# render_template() fxn from flask used to render html template when someone accesses root URL "/" of the app

# set up basic structure of flask
# define flask app and create route for home page 
# when someone accesses root URL the index() fxn will be executed and returns Hello, Flask as the response
app = Flask(__name__, template_folder='templates')

@app.route('/')  # decorator associates index() fxn with root URL of app
def index():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)

# for a web interface, need to render HTML templates
# in templates directory create HTML file (index.html)