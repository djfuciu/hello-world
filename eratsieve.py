import math

sieve = dict()
pointer = 2
def sieve_gen(n):
    for n in xrange(2, n + 1):
        sieve.update({n: True})

def next_num():
    for x, y in sieve.iteritems():
        if y == True and x > pointer:
            return x

def process():
    for x in xrange(pointer, len(sieve) + 3, pointer):
        if x > pointer:
            sieve[x] = False

primeto = int(raw_input("Please input the value of n: "))
topval = int(math.ceil(math.sqrt(primeto)))
sieve_gen(primeto)

while pointer <= topval:
    process()
    pointer = next_num()

for x, y in sieve.iteritems():
    if y == True:
        print x
