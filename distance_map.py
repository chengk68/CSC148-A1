"""Assignment 1 - Distance map (Task 1)

CSC148, Winter 2021

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Diane Horton, Ian Berlott-Atwell, Jonathan Calver,
Sophia Huynh, Maryam Majedi, and Jaisie Sin.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Diane Horton, Ian Berlott-Atwell, Jonathan Calver,
Sophia Huynh, Maryam Majedi, and Jaisie Sin.

===== Module Description =====

This module contains the class DistanceMap, which is used to store
and look up distances between cities. This class does not read distances
from the map file. (All reading from files is done in module experiment.)
Instead, it provides public methods that can be called to store and look up
distances.
"""
from typing import Dict


class DistanceMap:
    """A class that keeps track of lines in a map-data file.

    === Private Attributes ===
    _city_distances:
        A Dictionary with keys of cities of dictionaries for
        distances to other cities
    """
    _city_distances: Dict[str, Dict[str, int]]

    def __init__(self) -> None:
        """Initialize a new DistanceMap"""
        self._city_distances = {}

    def distance(self, city1: str, city2: str) -> int:
        """Return the distance from city1 to city2,
        or -1 if distance is not stored
        """
        if city1 in self._city_distances:
            if city2 in self._city_distances:
                return self._city_distances[city1][city2]
        return -1

    def add_distance(self, city1: str, city2: str,
                     dist: int) -> None:
        """Adds distance dist1 between city1 and city2 to
        self._city_distances"""
        if city1 not in self._city_distances:
            self._city_distances[city1] = {}
        if city2 not in self._city_distances:
            self._city_distances[city2] = {}

        self._city_distances[city1][city2] = dist
        self._city_distances[city2][city1] = dist


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'allowed-import-modules': ['doctest', 'python_ta', 'typing'],
        'disable': ['E1136'],
        'max-attributes': 15,
    })
    import doctest
    doctest.testmod()
