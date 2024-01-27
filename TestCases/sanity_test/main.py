from link.addr_map import *
from link.link import Link
from tests.sanity_test import SanityTest


if __name__ == '__main__':
    mmio_link = Link()
    
    sanity_test = SanityTest(mmio_link)
    sanity_test.run()
