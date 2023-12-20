class Planet:
    def _init_(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        earth_distance = abs(self.distance_from_sun - 147_000_000)
        return {'distance_to_earth': earth_distance}


class Mercury(Planet):
    def _init_(self, name, distance_from_sun=58_000_000, planet_type='Terrestrial'):
        super()._init_(name, distance_from_sun, planet_type)

    @staticmethod
    def happy_new_year():
        return "Happy New Year on Mercury! A year lasts 88 Earth days."


class Jupiter(Planet):
    def _init_(self, name, distance_from_sun=779_000_000, planet_type='Gas Giant', number_of_moons=80):
        super()._init_(name, distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
        return "Happy New Year on Jupiter! A year lasts 4383 Earth days."


# Example usage for Mercury
mercury_obj = Mercury(name="Mercury")
print(f"Name: {mercury_obj.name}")
print(f"Distance to Earth: {mercury_obj.get_distance_to_earth()}")
print(f"Planet Type: {mercury_obj.planet_type}")
print(Mercury.happy_new_year())

# Example usage for Jupiter
jupiter_obj = Jupiter(name="Jupiter")
print(f"Name: {jupiter_obj.name}")
print(f"Distance to Earth: {jupiter_obj.get_distance_to_earth()}")
print(f"Planet Type: {jupiter_obj.planet_type}")
print(f"Number of Moons: {jupiter_obj.number_of_moons}")
print(Jupiter.happy_new_year())