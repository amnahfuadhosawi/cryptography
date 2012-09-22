from Crypto.Cipher import AES
import urllib2
import sys

cmsg = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4".decode('hex')
TARGET = 'http://crypto-class.appspot.com/po?er='

def BadPad(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def strxor(u, v):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(u, v)])

def strippad(msg):
    n = ord(msg[-1])
    for c in msg[-n:]:
        if(ord(c) != n):
            raise BadPad("bad pad")
    return msg[0:-n]

def goodpad(msg):
    n = ord(msg[-1])
    if n > 16:
        return False
    for c in msg[-n:]:
        if(ord(c) != n):
            return False
    return True

key = "x"*16
cipher = AES.new(key, AES.MODE_CBC)
msg = "x"*50
npad = 64-len(msg)
msg = msg + chr(npad)*npad
cmsg = cipher.encrypt(msg)

#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding


po = PaddingOracle()
guess = bytearray(chr(0)*len(cmsg))
nblocks = len(cmsg)/16
firstbyte = True
for nblock in xrange(nblocks - 2, -1, -1):
    print "block " + str(nblock)
    for offset in xrange(0,16): # 16
        idx = (nblock+1)*16 - offset - 1 
        output = bytearray(cmsg[:(nblock+2)*16])

        # set trailing pad
        for j in xrange(idx + 1, (nblock+1)*16):
            mask = (offset + 1)^guess[j+16]
            output[j] = strxor(cmsg[j], chr(mask))
        print "Trying idx: " + str(idx + 16)
        # print output
        for i in xrange(0, 255): 
     #                print i
            mask = (offset + 1)^i
            if(firstbyte and mask == 0): # We want a valid padding different from real padding
                firstbyte = False
                continue
            output[idx] = strxor(cmsg[idx], chr(mask))
            cipher = AES.new(key, AES.MODE_CBC)
            d = cipher.decrypt(str(output))
            
            # print str(output).encode("hex")
            # print str(cmsg).encode('hex')
            # print d.encode('hex')
            # print d
            # print ord(d[-1])
            # print ord(d[-14])
            # if(offset == 13 and i == 0):
            #     import pdb
            #     pdb.set_trace()

            if goodpad(d):
                guess[idx + 16] = chr(i)
                print "guess[%i]: %s" % (idx + 16, chr(i))
                break
            else:
                pass
                ###print "badpad"
            # if(po.query(str(output))):       # Issue HTTP query with the given argument 
            #     break


    # raise(Exception)
    print guess