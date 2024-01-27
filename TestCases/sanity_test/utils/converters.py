import struct

# region BYTES TO LIST OF INT32 WORDS ===============================
def bytes2words(data: bytes) -> list:
    """ Convert bytes to list of int32
    param data: bytes
    return: list of int32 """
    words = len(data) // 4
    return [struct.unpack('I', data[i*4:(i+1)*4])[0] for i in range(words)]
# endregion =========================================================

# region LIST OF INT32 WORDS TO BYTES ===============================
def words2bytes(data: list) -> bytes:
    """ Convert list of int32 to bytes 
    param data: list of int32    
    return: bytes """    
    return b''.join(struct.pack('<I', item) for item in data)
# endregion LIST OF BYTES WORDS TO BYTES ============================

# region LIST OF INT TO LIST OF HEX =================================
def words2hex(data: list, n_bytes: int = 8) -> list:
    """ Convert list of int32 to list of hex strings
    param data: list of int32
    param n_bytes: number of bytes to convert

    return: list of hex strings """
    return [f'0x{i:0{n_bytes}X}' for i in data]
# endregion =========================================================
