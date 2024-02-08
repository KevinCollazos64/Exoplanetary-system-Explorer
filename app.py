from flask import Flask, render_template, request  # Flask- The web frameowkr used to create web apps; Render_temp- Used to render HTML temp; Request object contains information about current HTTP request
import requests  # Requests library is used to send the HTTP requests
import random
app=Flask(__name__)  # creates a Flask web app INSTANCE


# Endpoint is the URL of the API from which we want to extract Data
ENDPOINT="https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=SELECT * FROM ps" 

def get_random_exoplanet_facts():
    # request to the exoplanet API 
    response=requests.get(ENDPOINT, timeout=98)

    if response.status_code==200:
        exoplanet_data=response.json()

        # extract relevant information
        exoplanets=exoplanet_data.get('exoplanets',[])

        # randomly select 3 exoplanets
        selected_exoplanets=random.sample(exoplanets, min(3, len(exoplanets)))

        return selected_exoplanets
    
# Data for demonstration
def get_exoplanets_data():  # fxn sends GET req to API , only if status code=200 (valid) we parse the JSON response and return Data; Else None
    response= requests.get(ENDPOINT, timeout=98)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        return None

@app.route('/')  # Decorator associates index() with root URL ('/') of the web app. Handles main page where you can search for exoplanets 
def index():  # Retrieves search query from request; Fetches exoplanet data, filters based on query, renders index html template with list of exoplanets
    """query=request.args.get('query', '')
    exoplanets_data=get_exoplanets_data()
    if exoplanets_data:
        if query:
            exoplanets=[planet for planet in exoplanets_data if query.lower() in planet['pl_hostname'].lower()]
        else:
            exoplanets=exoplanets_data
    else:
        exoplanets=[]"""
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/search', methods=['GET'])
def search():
    exoplanets_data=get_exoplanets_data()
    if exoplanets_data:
        exoplanets=[planet for planet in exoplanets_data]
    else:
        exoplanets=[]
    return render_template('search.html')

@app.route('/search_results')
def search_results():
    # handles form submission and query the database for search results
    planet_name=request.args.get('planet_name')
    discovery_method=request.args.get('discovery_method')

    # performs the search logic and retrieve results from your data source

    # temporary dummy data for illustration
    results= [
        {'name': 'Exoplanet 1', 'method': 'Radial Velocity'},
        {'name': 'Exoplanet 2', 'method': 'Transit'},

    ]

    return render_template('search_results.html', results=search_results)
@app.route('/explore')
def explore():
    # get random exoplanet facts
    exoplanets=get_random_exoplanet_facts()
    return render_template('explore.html', exoplanets=exoplanets)

@app.route('/exoplanet/<id>')  # Decorator associates exoplanet_detail() fxn with URLs such as 'exoplanet'/1 where <int:id> is var for ID of the exoplanet
def exoplanet_detail(planet_id):  # Handles detail page for SPECIFIC exoplanet
    exoplanets_data=get_exoplanets_data()
    if exoplanets_data:
        exoplanet=next((planet for planet in exoplanets_data if planet['pl_id']==planet_id), None)
        if exoplanet:
            return render_template('exoplanet_detail.html', exoplanet=exoplanet)
    return "Exoplanet not found", 404

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/myfavexopl')
def myfavexopl():
    return render_template('myfavexopl.html')

if __name__=='__main__':  # Ensures Flask app is only run if script executed directly (not imported as module)
    app.run(debug=True)  # Starts dev server with debugging enabled 