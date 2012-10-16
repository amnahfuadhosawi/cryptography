import gmpy
from gmpy import mpz

gmpy.set_minprec(700)

N1 = mpz('179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581')
N2 = mpz('648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877')

N = N1
def try_midpoint(N, midpoint):
    delta = gmpy.sqrt(midpoint*midpoint - N)
    p = midpoint - delta
    q = midpoint + delta
    if p*q == N:
        return min(p,q)
    else:
        return False

def try_weightedavg(N, weightedavg2sq):
    # gmpy.set_minprec(1000) 
    # print weightedavg2 - 2*gmpy.ceil(gmpy.fsqrt(6*N))
    import pdb
    # pdb.set_trace()
    # radical = gmpy.fsqrt(weightedavg2sq - 24*N)
    # numerators = [gmpy.fsqrt(weightedavg2sq) + x for x in [radical, -radical]]
    # for n in numerators:
    #     p = gmpy.cdivmod(mpz(gmpy.fround(n)), 6)[0] # +/- 1?
    #     # q = gmpy.cdivmod(weightedavg2 - 3*p, 2)[0]
    #     if(gmpy.cdivmod(N,p)[1] == 0):
    #         print("found divisor")
    #         print p
    #     if p*q == N:
    #         return min(p,q)
    #     print "diff"
    #     print (3*p + 2*q)/2 - gmpy.ceil(gmpy.sqrt(6*N))

    # pdb.set_trace()
    # weightedavg2 = mpz(gmpy.floor(gmpy.fsqrt(weightedavg2sq)))
    # num = weightedavg2 - mpz(gmpy.fsqrt(N/2)) - 1
    # lim = weightedavg2 + 1
    # done = False
    # while not done and num < lim:
    #     # print num
    #     p = gmpy.cdivmod(num, 6)[0] # +/- 1?
    #     # q = gmpy.cdivmod(weightedavg2 - 3*p, 2)[0]
    #     if(gmpy.cdivmod(N,p)[1] == 0):
    #         done = True
    #         print("found divisor")
    #         print min(p, gmpy.cdivmod(N,p)[0])
    #         return True
    #     num += 1

    weightedavg2 = gmpy.ceil(gmpy.fsqrt(weightedavg2sq))
    num = weightedavg2 - gmpy.fsqrt(weightedavg2*weightedavg2 - 24*N)
    p = gmpy.cdivmod(mpz(num), 6)[0]
    for i in xrange(0, 100000):
        if(gmpy.cdivmod(N,p+i)[1] == 0 or gmpy.cdivmod(N,p-i)[1] == 0) :
            print("found divisor")
            q = gmpy.cdivmod(N,p)[0]
            print min(p, q)
            print N == p*q
            print i
            return True

    return False


# question 1
# try_midpoint(ceil(sqrt(N)))
p1 = 13407807929942597099574024998205846127479365820592393377723561443721764030073662768891111614362326998675040546094339320838419523375986027530441562135724301

def q2():
    done = False
    i = 0
    sqrtN2 = gmpy.sqrt(N2) + 1
    print "start"
    done = False
    while(i < 2**20):
        res = try_midpoint(N2, sqrtN2 + i)
        if res:
            done = True
            print(res)
        i += 1
    print(done)


def q3():
    done = False
    i = 0
    N = mpz('720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929')
    # N = mpz(1523*1009)
    print "start"
    done = False
    weightedavg2sq = 24*N
    import pdb
    # pdb.set_trace()
    res = try_weightedavg(N, weightedavg2sq) # equivalent to ceil
    if res:
        done = True
        print(res)
    print(done)


q3()
