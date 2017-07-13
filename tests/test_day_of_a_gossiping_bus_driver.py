import unittest

from app import DayOfAGossipingBusDriver
from app.bus_driver_from import bus_driver_from
from app.gossip_universe import GossipUniverse
from route import Route


class TestDayOfAGossipingBusDriverCommon(unittest.TestCase):
    def one_minute_passed_for(self, drivers):
        DayOfAGossipingBusDriver(drivers, self.gossip_universe) \
            .one_minute_passed()

    def know_all_gossips(self, drivers):
        return DayOfAGossipingBusDriver(drivers, self.gossip_universe) \
            .all_bus_drivers_know_all_gossips()

    def minutes_to_know_all_gossips_for(self, drivers):
        return DayOfAGossipingBusDriver(drivers, self.gossip_universe) \
            .minutes_to_know_all_the_gossips()


class TestDayOfAGossipingBusDriver(TestDayOfAGossipingBusDriverCommon):
    def setUp(self):
        self.gossip_universe = GossipUniverse()
        self.boris = bus_driver_from(Route([1, 12, 13]), self.gossip_universe)
        self.anna = bus_driver_from(Route([1, 22, 23]), self.gossip_universe)
        self.sam = bus_driver_from(Route([12, 32, 33]), self.gossip_universe)

    def test_drivers_share_gossips_when_on_same_stop(self):
        self.one_minute_passed_for([self.boris, self.anna])

        all_gossips = {self.boris.gossip, self.anna.gossip}
        self.assertEqual(self.boris.known_gossips(), all_gossips)
        self.assertEqual(self.anna.known_gossips(), all_gossips)

    def test_drivers_dont_share_gossips_when_on_different_stops(self):
        self.one_minute_passed_for([self.boris, self.sam])

        self.assertEqual(self.boris.known_gossips(), {self.boris.gossip})
        self.assertEqual(self.sam.known_gossips(), {self.sam.gossip})

    def test_drivers_all_drive_as_minutes_pass(self):
        drivers = [self.boris, self.anna, self.sam]

        self.one_minute_passed_for(drivers)

        self.assertEqual(self.boris.bus.current_stop(), 12)
        self.assertEqual(self.anna.bus.current_stop(), 22)
        self.assertEqual(self.sam.bus.current_stop(), 32)

        self.one_minute_passed_for(drivers)

        self.assertEqual(self.boris.bus.current_stop(), 13)
        self.assertEqual(self.anna.bus.current_stop(), 23)
        self.assertEqual(self.sam.bus.current_stop(), 33)


class TestDayOfAGossipingBusDriverWhenTwoDriversCanCatchUp(TestDayOfAGossipingBusDriverCommon):
    def setUp(self):
        self.gossip_universe = GossipUniverse()

        # 14 23 34 13 24 33 => 6 minutes
        self.andy = bus_driver_from(Route([1, 2, 3]), self.gossip_universe)
        self.cindy = bus_driver_from(Route([4, 3]), self.gossip_universe)
        self.drivers = [self.andy, self.cindy]

    def test_know_all_gossips(self):
        self.one_minute_passed_for(self.drivers)
        self.assertFalse(self.know_all_gossips(self.drivers), "know all gossips after 1 minute")

        self.one_minute_passed_for(self.drivers)
        self.assertFalse(self.know_all_gossips(self.drivers), "know all gossips after 2 minutes")

        self.one_minute_passed_for(self.drivers)
        self.assertFalse(self.know_all_gossips(self.drivers), "know all gossips after 3 minutes")

        self.one_minute_passed_for(self.drivers)
        self.assertFalse(self.know_all_gossips(self.drivers), "know all gossips after 4 minutes")

        self.one_minute_passed_for(self.drivers)
        self.assertFalse(self.know_all_gossips(self.drivers), "know all gossips after 5 minutes")

        self.one_minute_passed_for(self.drivers)
        self.assertTrue(self.know_all_gossips(self.drivers), "know all gossips after 6 minutes")

    def test_how_many_minutes_to_know_all_the_gossips(self):
        minutes = self.minutes_to_know_all_gossips_for(self.drivers)

        self.assertEqual(minutes, 6)


class TestDayOfAGossipingBusDriverWhenTwoDriversCanNotCatchUp(TestDayOfAGossipingBusDriverCommon):
    def setUp(self):
        self.gossip_universe = GossipUniverse()

        self.martin = bus_driver_from(Route([2, 1, 2]), self.gossip_universe)
        self.alex = bus_driver_from(Route([5, 2, 8]), self.gossip_universe)
        self.drivers = [self.martin, self.alex]

    def test_how_many_minutes_to_know_all_the_gossips(self):
        minutes = self.minutes_to_know_all_gossips_for(self.drivers)

        self.assertEqual(minutes, "never")


class TestDayOfAGossipingBusDriverAcceptanceTest(TestDayOfAGossipingBusDriverCommon):
    def setUp(self):
        self.gossip_universe = GossipUniverse()

        # - minute    stop    G1    G2    G3
        #
        # -      1      3      y     y     n
        #               3      y     y     n
        #               4      n     n     y
        #
        # -      2      1      y     y     n
        #               2      y     y     y
        #               2      y     y     y
        #
        # -      3      2      y     y     n
        #               3      y     y     y
        #               3      y     y     y
        #
        # -      4      3      y     y     n
        #               1      y     y     y
        #               4      y     y     y
        #
        # -      5      3      y     y     y
        #               3      y     y     y
        #               5      y     y     y
        #
        # -             result => 5
        self.bob = bus_driver_from(Route([3, 1, 2, 3]), self.gossip_universe)
        self.alice = bus_driver_from(Route([3, 2, 3, 1]), self.gossip_universe)
        self.sascha = bus_driver_from(Route([4, 2, 3, 4, 5]), self.gossip_universe)
        self.drivers = [self.bob, self.alice, self.sascha]

    def test_how_many_minutes_to_know_all_the_gossips(self):
        minutes = self.minutes_to_know_all_gossips_for(self.drivers)

        self.assertEqual(minutes, 5)


if __name__ == '__main__':
    unittest.main()
