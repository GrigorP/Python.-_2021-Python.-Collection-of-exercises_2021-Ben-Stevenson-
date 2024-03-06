# Exercise 12. Distance between points on Earth

import math

lat1 = float(input("Enter the latitude of the first point in degrees: "))
lon1 = float(input("Enter the longitude of the first point in degrees: "))
lat2 = float(input("Enter the latitude of the second point in degrees: "))
lon2 = float(input("Enter the longitude of the second point in degrees: "))

lat1, lon1, lat2, lon2 = map(lambda x: x * math.pi / 180, [lat1, lon1, lat2, lon2])

dlat = lat2 - lat1
dlon = lon2 - lon1
a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

radius = 6371.01

distance = radius * c

print(f"The distance between the two points is {distance:.2f} kilometers.")