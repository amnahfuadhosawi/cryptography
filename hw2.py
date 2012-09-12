from Crypto.Cipher import AES
import struct

def strxor(u, v):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(u, v)])

# key = '140b41b22a29beb4061bda66b6747e14'.decode('hex')
# ct = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'.decode('hex')

# ct = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48\
# e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'.decode('hex')

key = '36f18357be4dbd77f050515c73fcf9f2'.decode('hex')
ct = [x.decode('hex') for x in 
      ['69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329',
       '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451']]

x = bytearray()

def strippad(msg):
    return msg[0:-msg[-1]]

def decrypt_cbc(ct):
    x = bytearray()
    iv = ct[0:16]
    ct = ct[16:]
    cipher = AES.new(key, AES.MODE_ECB)
    
    x.extend(strxor(iv, cipher.decrypt(ct[0:cipher.block_size])))
    ptr = cipher.block_size
    for i in xrange(1, len(ct)/cipher.block_size):
        d = cipher.decrypt(ct[i*cipher.block_size:(i+1)*cipher.block_size])
        x.extend(strxor(d,ct[(i-1)*cipher.block_size:i*cipher.block_size]))
    return strippad(x)

def decrypt_ctr(ct):
    x = bytearray()
    iv = ct[0:16]
    ct = ct[16:]
    cipher = AES.new(key, AES.MODE_ECB)

    fmt = '>QQ'                  # two unsigned long long (big-endian)
    intiv1, intiv2 = struct.unpack(fmt, iv)
    intiv = intiv1*2**64 + intiv2
    for i in xrange(0, len(ct)/cipher.block_size + 1): 
        print i
        print len(ct)/cipher.block_size
        intiv1 = intiv/2**64
        intiv2 = intiv % 2**64
        striv = struct.pack(fmt, intiv1, intiv2)
        # print striv.encode('hex')
        d = cipher.encrypt(striv)
        c = ct[i*cipher.block_size:(i+1)*cipher.block_size]
        x.extend(strxor(c,d))
        intiv += 1
        # print intiv
    return x

# cipher = AES.new(key, AES.MODE_CBC, iv)
# print cipher.decrypt(ct)

# print (strippad(x))


# Basic CBC mode encryption needs padding.
# Our implementation uses rand. IV
