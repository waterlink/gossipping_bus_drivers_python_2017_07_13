class DayOfAGossipingBusDriver(object):
    def __init__(self, drivers, gossip_universe):
        self.drivers = drivers
        self.gossip_universe = gossip_universe

    def one_minute_passed(self):
        self.share_gossips_between_all_drivers()
        self.all_drivers_drive()

    def share_gossips_between_all_drivers(self):
        for driver in self.drivers:
            driver.share_gossips_with_all(self.drivers)

    def all_drivers_drive(self):
        for driver in self.drivers:
            driver.drive()

    def all_bus_drivers_know_all_gossips(self):
        for driver in self.drivers:
            if not self.gossip_universe.knows_all_gossips(driver):
                return False
        return True

    def minutes_to_know_all_the_gossips(self):
        for minute in range(480):
            self.one_minute_passed()
            if self.all_bus_drivers_know_all_gossips():
                return minute + 1

        return "never"
