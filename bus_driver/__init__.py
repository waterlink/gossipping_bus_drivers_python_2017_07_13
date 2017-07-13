class BusDriver(object):
    def __init__(self, bus, gossip):
        self.bus = bus
        self.gossip = gossip
        self.all_gossips = {gossip}

    def drive(self):
        self.bus.next_stop()

    def known_gossips(self):
        return self.all_gossips

    def got_to_know(self, new_gossip):
        self.all_gossips.add(new_gossip)

    def share_gossips_with(self, other_driver):
        if self == other_driver:
            return

        if self.bus.current_stop() != other_driver.bus.current_stop():
            return

        for gossip in self.all_gossips:
            other_driver.got_to_know(gossip)

    def share_gossips_with_all(self, drivers):
        for other_driver in drivers:
            self.share_gossips_with(other_driver)
            other_driver.share_gossips_with(self)
