def strxor(u, v):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(u, v)])

msg = '20814804c1767293b99f1d9cab3bc3e7ac1e37bfb15599e5f40eef805488281d'.decode('hex')
x = bytearray(msg)

s = "Pay Bob 100$"

idx = [i for i,z in enumerate(s) if z=='1'][0]

x[8] = x[8] ^ ord('5') ^ ord('1')
print str(x).encode('hex')

