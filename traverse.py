import math

def calculate_another_point(easting, northing, bearing, distance):
    delta_easting = distance * math.sin(math.radians(bearing))
    delta_northing = distance * math.cos(math.radians(bearing))

    easting_point_1 = easting + delta_easting
    northing_point_1 = northing + delta_northing
    return [easting_point_1, northing_point_1] #list of doubles/floating point numbers

"""
easting = 601192.524
northing = 873241.123

bearing = 90 # degrees

distance = 120 # meters
"""


point_b = calculate_another_point(601192.524, 873241.123, 90, 120)
point_c = calculate_another_point(601192.524, 873241.123, 97, 119)

print("Coordinates of point B: ")
print(point_b)

print("Coordinates of point C: ")
print(point_c)