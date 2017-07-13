class Gossip(object):
    def __init__(self, gossip_universe):
        self.gossip_universe = gossip_universe
        gossip_universe.add(self)
