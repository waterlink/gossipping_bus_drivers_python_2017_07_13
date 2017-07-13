class Route(object):
    def __init__(self, stops):
        self.stops = stops

    def next_stop_number(self, number):
        return (number + 1) % len(self.stops)

    def stop_at(self, number):
        return self.stops[number]