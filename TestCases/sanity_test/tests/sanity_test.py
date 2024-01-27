import re
from link.addr_map import *
from link.link import Link
from setup_test import *
from utils.fill import fill_buffer

PASSED = f'\033[38;2;{0};{200};{0};1m{PASSED}\033[0m '
FAILED = f'\033[38;2;{200};{0};{0};1m{FAILED}\033[0m '

class SanityTest:
    def __init__(self, link: Link):
        print(SANITY_TEST)
        self.link = link
        self.sanity_test_toggle = 1 << 31 

    def print_err(self, direction, name, index, data):
        b = f'{data:032b}'
        b = ' '.join(re.findall('.{1,4}', b))

        print(f'{direction} ADDR: 0x{name + (index*4):08X}: DATA --> HEX: 0x{data:08X} --> BIN: {b}')

    def create_test(self, offset, size, init, incr, rnd, rnd_seed):
        tx_data = list()
        rx_data = list()

        fill_buffer(init, size, incr, rnd, rnd_seed, tx_data)

        self.link.write(offset, tx_data, size)
        self.link.read(offset, rx_data, size)

        errors = 0

        for i in range(0, size, 4):
            j = i // 4
            if tx_data[j] != rx_data[j]:
                errors += 1
                self.print_err('Tx', offset, j, tx_data[j])
                self.print_err('Rx', offset, j, rx_data[j])
                print()
        return errors

    def ram_test(self, name, offset, size, init, incr, rnd, rnd_seed):
        errors = self.create_test(offset, size, init, incr, rnd, rnd_seed)
        
        if errors > 0: print(f'\n{name}: 0x{(BASE_ADDR + offset):08X} size = {size:5d} bytes, test {FAILED}\nwith {errors} errors.\n')
        else: print(f'{name} {name}: 0x{(BASE_ADDR + offset):08X} size = {size:5d} bytes, test {PASSED}') 

    def run(self):
        # RAMs TEST
        print(f'\nRAMs TEST START {"="*49}\n')
        self.ram_test('DBG01_RAM', DBG01_RAM, DBG01_RAM_SIZE, 0x00, 0x00, 1, 1)
        self.ram_test('DBG02_RAM', DBG02_RAM, DBG02_RAM_SIZE, 0x00, 0x00, 1, 1)

        print(f'RAMs TEST STOP {"="*50}\n')
