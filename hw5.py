# Run in sage

N = 40
B = 2^(N/2)
p = Integer('13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171')
R = GF(p)
h = R('3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333')
g = R('11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568')
finished = False
i = Integer(0)
htable = {}
print "Started building hash table"
while(not finished):
        key = R(h/(g^i))
        htable[key] = i
        if(i == B):
            finished = True
        else:
            i += 1

print "finished building hash table"
            
notFound = True
finished = False
i = Integer(0)
gb = R(g^B)
while(not finished):
        key = R(gb^i)
        if(htable.has_key(key)):
            res = (i, htable[key])
            notFound = False
            finished = True
        htable[key] = i
        if(i == B):
            notFound = True
            finished = True
        else:
            i += 1

print "finished search hash table"
            
if notFound:
    print "Solution not found"
else:
    print res
    x = res[0]*B + res[1]
    print "Exponent: " + str(x)
    print R(g^x) 
    
