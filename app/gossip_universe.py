class GossipUniverse(object):
    def __init__(self):
        self.gossips = set()

    def all_gossips(self):
        return self.gossips

    def add(self, gossip):
        self.gossips.add(gossip)

    def knows_all_gossips(self, driver):
        return driver.known_gossips() == self.all_gossips()
