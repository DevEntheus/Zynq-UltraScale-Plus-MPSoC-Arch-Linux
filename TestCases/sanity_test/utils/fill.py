from random import randint, seed


def fill_buffer(init, size, incr, rnd, rnd_seed, buff: list):
        data = init
        try:
            if rnd and rnd_seed: seed(init)
            while size > 0:
                if rnd:
                    data = randint(0x00000000, 0xffffffff)
                    buff.append(data)                
                else:
                    if data > 0xffffffff: data = init
                    buff.append(data)
                    data += incr

                size -= 4

        except Exception as e:
            print(f'Fill buffer error.\nReason: {e}')