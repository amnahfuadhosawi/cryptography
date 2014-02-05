def strxor(u, v):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(u, v)])
