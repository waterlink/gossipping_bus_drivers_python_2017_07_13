import unittest

from bus import Bus
from route import Route


class BusDriver(object):
    def __init__(self, bus, gossip):
        self.bus = bus
        self.gossip = gossip
        self.all_gossips = {self.gossip}

    def drive(self):
        self.bus.next_stop()

    def known_gossips(self):
        return self.all_gossips

    def got_to_know(self, new_gossip):
        self.all_gossips.add(new_gossip)


class Gossip(object):
    pass


class TestBusDriver(unittest.TestCase):
    def setUp(self):
        self.route = Route([20, 54, 34])
        self.bus = Bus(self.route)
        self.gossip = Gossip()
        self.bus_driver = BusDriver(self.bus, self.gossip)

    def test_driver_drives_bus_to_next_stop(self):
        self.bus_driver.drive()

        self.assertEqual(self.bus.current_stop(), 54)

    def test_driver_knows_a_gossip(self):
        self.assertEqual(self.bus_driver.known_gossips(), {self.gossip})

    def test_driver_got_to_know_new_gossip(self):
        new_gossip = Gossip()

        self.bus_driver.got_to_know(new_gossip)

        self.assertEqual(self.bus_driver.known_gossips(), {self.gossip, new_gossip})


if __name__ == '__main__':
    unittest.main()
