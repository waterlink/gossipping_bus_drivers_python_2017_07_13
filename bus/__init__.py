class Bus(object):
    def __init__(self, route):
        self.current_stop_number = 0
        self.route = route

    def next_stop(self):
        self.current_stop_number += 1

    def current_stop(self):
        return self.route.stops[self.current_stop_number]