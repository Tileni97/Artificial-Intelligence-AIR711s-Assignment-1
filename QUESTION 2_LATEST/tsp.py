class TSP:
    def __init__(self, places, distances):
        """
        Initialize the TSP problem instance with a list of places and a distance matrix.
        """
        self.places = places
        self.distances = distances

    def get_distance(self, place1, place2):
        """
        Get the distance between two places.
        """
        return self.distances[self.places.index(place1)][self.places.index(place2)]
