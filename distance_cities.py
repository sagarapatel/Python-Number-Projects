#!/usr/bin/env python3
# Program calculate distance between two cities using Nominatim library.
# https://github.com/sagarapatel/Python-Number-Projects/blob/master/distance_cities.py
# IDE PyCharm
# Python 3.8 compatible

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

locator = Nominatim(user_agent="myGeocode")
city_one = str(input("Please enter name of the first city "))
location_one = locator.geocode(city_one)
city_two = str(input("Please enter name of the second city "))
location_two = locator.geocode(city_two)

print(city_one + " Latitude = {} and Longitude = {}".format(location_one.latitude, location_one.longitude))
print(city_two + " Latitude = {} and Longitude = {}".format(location_two.latitude, location_two.longitude))

city_one_position = (location_one.latitude, location_one.longitude)
city_two_positon = (location_two.latitude, location_two.longitude)

print("Distance between {} and {} is {} km".format(city_one, city_two, round(geodesic(city_one_position, city_two_positon).km)))
