import requests
# specify columns to return (select+pl_name,pl_masse,ra,dec+from+ps) for ex all spaces replaced with +
# more constraints with where
# examples on usingTAP website

# example query to return planet names, masses, coordinates for all confirmed planets of about Earth size
# https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=
# select+pl_name,pl_masse,ra,dec+from+ps+where+upper(soltype)+like+'%CONF%'+and+pl_masse+between+0.5+and+2.0


# specify output file format (json)
# spacial constraints in queries (circle, box, polygon)

# TAP query to get info about data tables
# GET to pull data on confirmed existing exoplanets

# queries must be a single line
# eb aware of case sensitivity
# use a TAP client when returning large data sets
# what is the filter you wanna have for this program? how could we allow user to have a filter?


url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name+pl_rade+disc_year+pl_masse+st_logg+from+ps+where+pl_rade+<+2&format=json"
response = requests.get(url)
if response.status_code == 200:
    print('ok')
    data = response.json()
    print(data[0])

