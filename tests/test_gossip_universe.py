import unittest

from app.gossip_universe import GossipUniverse
from bus_driver.gossip import Gossip


class TestBus(unittest.TestCase):
    def setUp(self):
        self.gossip_universe = GossipUniverse()

    def test_created_gossip_is_recorded_in_gossip_universe(self):
        gossip = Gossip(self.gossip_universe)

        self.assertEqual(self.gossip_universe.all_gossips(), {gossip})


if __name__ == '__main__':
    unittest.main()
