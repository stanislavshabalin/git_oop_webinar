#-*- coding utf-8 -*-

class Transport:
    def __init__(self, fuel):
        self.fuel = fuel
        self.trips = []

    def add_trip(self, trip):
        self.trips.append(trip)

    def sum_trips_distance(self):
        return sum(trip.distance for trip in self.trips)

    def calculate_reachable_distance(self):
        raise NotImplementedError()


class Trip:
    def __init__(self, dist, comment='Не регламентировано'):
        self.distance = dist
        self.comment = comment
