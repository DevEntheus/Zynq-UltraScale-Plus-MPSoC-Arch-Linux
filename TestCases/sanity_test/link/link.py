# from periphery.mmio import MMIO
from link.mmio import MMIO
from setup_test import BASE_ADDR, REGION_SIZE


class Link:
    def __init__(self):        
        self.mmio = MMIO(BASE_ADDR, REGION_SIZE)

    def write(self, offset, buff: list, size=0):
        if size != 0:
            for i in range(0, size, 4):
                self.mmio.write32(offset + i, buff[int(i/4)])
        else:
            for i in range(len(buff)):
                self.mmio.write32(offset + i*4, buff[i])

    def read(self, offset, buff: list, size=0):
        if size != 0:
            for i in range(0, size, 4):
                buff.append(self.mmio.read32(offset + i))
        else:
            for i in range(len(buff)):
                buff.append(self.mmio.read32(offset + i*4))        

    def write_word(self, offset, data):
        self.mmio.write32(offset, data)

    def read_word(self, offset):
        return self.mmio.read32(offset)
