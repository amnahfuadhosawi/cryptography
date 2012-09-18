from Crypto.Cipher import AES

def strxor(u, v):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(u, v)])

def f1(x,y):
    cipher = AES.new(x, AES.MODE_ECB)
    d = cipher.encrypt(x)
    return strxor(d, y).encode('hex')

z = '00000000000000000000000000000000'.decode('hex')
w = '00000000000000000000000000000001'.decode('hex')
print f1(z,z)
s = strxor('66e94bd4ef8a2c3b884cfa59ca342b2e'.decode('hex'), 'a17e9f69e4f25a8b8620b4af78eefd6f'.decode('hex'))

print f1(w,s)

def f2(x,y):
    cipher = AES.new(y, AES.MODE_ECB)
    d = cipher.encrypt(x)
    return strxor(d, y).encode('hex')

print f2(z, w)
# q = strxor('0545aad56da2a97c3663d1432a3d1c85'.decode('hex'), w) # output of AES part
q = '0545aad56da2a97c3663d1432a3d1c85'.decode('hex')
cipher  = AES.new(z)
x = cipher.decrypt(q)


print f2(x, z)
print f2(z, w)

print s.encode('hex')
print z.encode('hex')
print z.encode('hex')
print w.encode('hex')

print [i.encode('hex') for i in [x, z, z, w]]
