import unittest

from app.bus_driver_from import bus_driver_from
from bus_driver.gossip import Gossip
from route import Route
from app.gossip_universe import GossipUniverse


class TestBusDriver(unittest.TestCase):
    def setUp(self):
        self.gossip_universe = GossipUniverse()
        self.bus_driver = bus_driver_from(Route([20, 54, 34]), self.gossip_universe)

    def test_driver_drives_bus_to_next_stop(self):
        self.bus_driver.drive()

        self.assertEqual(self.bus_driver.bus.current_stop(), 54)

    def test_driver_knows_a_gossip(self):
        self.assertEqual(self.bus_driver.known_gossips(), {self.bus_driver.gossip})

    def test_driver_got_to_know_new_gossip(self):
        new_gossip = Gossip(self.gossip_universe)

        self.bus_driver.got_to_know(new_gossip)

        self.assertEqual(self.bus_driver.known_gossips(), {self.bus_driver.gossip, new_gossip})

    def test_driver_can_share_gossips_with_other_driver(self):
        other_bus_driver = bus_driver_from(Route([20, 54, 34]), self.gossip_universe)

        self.bus_driver.share_gossips_with(other_bus_driver)

        self.assertEqual(other_bus_driver.known_gossips(),
                         {other_bus_driver.gossip, self.bus_driver.gossip})

    def test_driver_with_multiple_gossips_can_share_gossips_with_other_driver(self):
        bus_driver_with_multiple_gossips = bus_driver_from(Route([20, 54, 34]), self.gossip_universe)
        other_bus_driver = bus_driver_from(Route([20, 54, 34]), self.gossip_universe)

        second_gossip = Gossip(self.gossip_universe)
        bus_driver_with_multiple_gossips.got_to_know(second_gossip)

        bus_driver_with_multiple_gossips.share_gossips_with(other_bus_driver)

        self.assertEqual(other_bus_driver.known_gossips(), {
            other_bus_driver.gossip,
            bus_driver_with_multiple_gossips.gossip,
            second_gossip
        })


if __name__ == '__main__':
    unittest.main()
