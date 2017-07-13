import unittest

from bus import Bus
from bus.route import Route


class TestBus(unittest.TestCase):

    def setUp(self):
        self.route = Route([10, 3, 6])
        self.bus = Bus(self.route)
        self.assertEqual(self.bus.current_stop(), self.route.stops[0])

    def test_bus_moves_to_the_next_stop_in_one_minute(self):
        self.bus.next_stop()

        self.assertEqual(self.bus.current_stop(), 3)

    def test_bus_moves_to_the_next_next_stop_in_two_minute(self):
        self.bus.next_stop()
        self.bus.next_stop()

        self.assertEqual(self.bus.current_stop(), 6)

    def test_bus_moves_to_the_first_stop_given_enough_minutes(self):
        self.bus.next_stop()
        self.bus.next_stop()
        self.bus.next_stop()

        self.assertEqual(self.bus.current_stop(), 10)


if __name__ == '__main__':
    unittest.main()
