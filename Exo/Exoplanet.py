# display exoplanet name, radius, mass, distance from Earth, random fun fact, etc
# num_stars, num_planets, orbital_period, inso_flux, equil_temp, effective_temp, metallicity, metallicity_ratio, distance
# v_magnitude

# map exoplanet descriptions to certain description keys?

# best to not generate html directly in code, opens app to cross-site scripting XSS attacks
# keep html out of your code by using templates so code is concerned only with data values and not with rendering 

class Exoplanet:
    def __init__(self, name, e_radius, disc_year, e_mass, surface_gravity):
        self.name = name
        self.e_radius = e_radius
        self.disc_year = disc_year
        self.e_mass = e_mass
        self.surface_gravity = surface_gravity


    