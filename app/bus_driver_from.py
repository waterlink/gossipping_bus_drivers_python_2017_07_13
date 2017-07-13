from bus import Bus
from bus_driver import BusDriver
from bus_driver.gossip import Gossip


def bus_driver_from(route, gossip_universe):
    bus = Bus(route)
    gossip = Gossip(gossip_universe)
    return BusDriver(bus, gossip)