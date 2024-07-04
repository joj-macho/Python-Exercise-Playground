'''
Exercise: Distance Between Two Points on Earth

This script calculates the distance between two points on Earth given their
latitude and longitude using the formula:
R = 6371; # in km
φ1 = lat1 * PI/180 # φ, λ in radians
φ2 = lat2 * PI/180
Δφ = (lat2-lat1) * PI/180
Δλ = (lon2-lon1) * PI/180

a = sin(Δφ/2) * sin(Δφ/2) + cos(φ1) * cos(φ2) * sin(Δλ/2) * sin(Δλ/2)
c = 2 * atan2(sqrt(a), sqrt(1-a))
d = R * c # in km

Usage:
    Call the function with the latitude and longitude of two points.

Tags: arithmetic operations, math module, trig functions, latitude, longitude
degrees, radians
'''

import math


def main():
    '''Main function to calculate distance between two points on Earth.'''
    lat1, lon1 = 38.8976, -77.0366
    lat2, lon2 = 39.9496, -75.1503
    print(f'The distance between the points is: '
          f'{distance_between_points(lat1, lon1, lat2, lon2):.2f} km')


def distance_between_points(lat1, lon1, lat2, lon2):
    '''
    Calculates the distance between two points on Earth.

    Parameters:
        lat1 (float): Latitude of the first point.
        lon1 (float): Longitude of the first point.
        lat2 (float): Latitude of the second point.
        lon2 (float): Longitude of the second point.

    Returns:
        float: Distance between the points in kilometers.
    '''
    R = 6378.0  # Radius of the Earth in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


if __name__ == '__main__':
    main()
