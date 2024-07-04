'''
Exercise: Distance Between Two Points on Earth

This script calculates the distance between two points on the Earth's
surface given their latitude and longitude using the Haversine formula.

Haversine Formula:
    d = 2 * R * asin(sqrt(hav(Δlat) + cos(lat1) * cos(lat2) * hav(Δlong)))
where:
    - d is the distance between the two points.
    - R is the Earth's radius (mean radius = 6,371 km).
    - hav is the haversine function: hav(θ) = sin^2(θ / 2)
    - Δlat = lat2 - lat1
    - Δlong = long2 - long1
    - lat1, long1 are the coordinates of the first point.
    - lat2, long2 are the coordinates of the second point.

Usage:
    Call the function with the latitude and longitude of two points.

Tags: arithmetic operations, math module, haversine formula, distance,
coordinates, earth
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
