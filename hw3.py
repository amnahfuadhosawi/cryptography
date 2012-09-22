from Crypto.Hash import SHA256
import functools
import os

def getfilesize(filepath):
    return os.stat(filepath).st_size

def hashchunk(s):
    h = SHA256.new()
    h.update(s)
    return h.digest()

def doit():
    stride = 1024
    filepath = os.path.expanduser("~/tmp/6 - 1 - Introduction (11 min).mp4")
    f = open(filepath, 'r')
    f.seek(0, os.SEEK_END)
    fsize = f.tell()
    nchunks, lastsize = divmod(fsize, stride)
    print nchunks, lastsize, fsize
    f.seek(fsize - lastsize)
    chunk = f.read(lastsize)
    lasthash = hashchunk(chunk)
    f.seek(-lastsize, os.SEEK_END)
    for i in xrange(0, nchunks):
        # print i
        f.seek(f.tell() - stride)
        pos = f.tell()          # before read
        chunk = f.read(stride)
        f.seek(pos)
        lasthash = hashchunk(chunk + lasthash)
    return lasthash
res = doit()
print res.encode('hex')