class Bus(object):
    def __init__(self, route):
        self.current_stop_number = 0
        self.route = route

    def next_stop(self):
        self.current_stop_number = self.route.next_stop_number(
            self.current_stop_number)

    def current_stop(self):
        return self.route.stop_at(self.current_stop_number)
