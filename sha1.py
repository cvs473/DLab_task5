import hashlib
import time

def sha1(data):
    mask = 0xFFFFFFFF
    bytes = ""
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    def lrot(n, b):
        return ((n << b) | (n >> (32 - b))) & mask
    
    for n in range(len(data)):
        bytes+='{0:08b}'.format(ord(data[n]))
    bits = bytes + "1"
    pBits = bits
    while len(pBits)%512 != 448:
        pBits+="0"
    pBits+='{0:064b}'.format(len(bits)-1)

    def chunks(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

    for ch in chunks(pBits, 512): 
        words = chunks(ch, 32)
        w = [0]*80
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        for i in range(16, 80):
            w[i] = lrot((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)  

        a, b, c, d, e = h0, h1, h2, h3, h4

        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6


            a, b, c, d, e = lrot(a, 5) + f + e + k + w[i] & mask, a, lrot(b, 30), c, d


        h0 = h0 + a & mask
        h1 = h1 + b & mask
        h2 = h2 + c & mask
        h3 = h3 + d & mask
        h4 = h4 + e & mask

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

start_lib = time.time()
hashlib.sha1(b"x" * 1000000).hexdigest()
end_lib = time.time()

start_hm = time.time()
sha1("x" * 1000000)
end_hm = time.time()
q = (end_hm - start_hm) / (end_lib - start_lib) 
print(f"homemade algorithm is {q} times slower than hashlib realization")
