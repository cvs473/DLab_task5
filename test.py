import unittest
import time
from sha1 import *

class TestSHA1(unittest.TestCase):
    def test_comparing(self):
        hexdigests_from_lib = []
        hexdigests_from_homemade_alg = []
        test1 = "abc"
        test2 = ""
        test3 = "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
        test4 = "abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu"
        test5 = "x" * 1000000
        hexdigests_from_lib.append(hashlib.sha1(test1.encode('utf-8')).hexdigest())
        hexdigests_from_lib.append(hashlib.sha1(test2.encode('utf-8')).hexdigest())
        hexdigests_from_lib.append(hashlib.sha1(test3.encode('utf-8')).hexdigest())
        hexdigests_from_lib.append(hashlib.sha1(test4.encode('utf-8')).hexdigest())
        hexdigests_from_lib.append(hashlib.sha1(test5.encode('utf-8')).hexdigest())
        
        hexdigests_from_homemade_alg.append(sha1(test1))
        hexdigests_from_homemade_alg.append(sha1(test2))
        hexdigests_from_homemade_alg.append(sha1(test3))
        hexdigests_from_homemade_alg.append(sha1(test4))
        hexdigests_from_homemade_alg.append(sha1(test5))
        self.assertEqual(list(hexdigests_from_lib), list(hexdigests_from_homemade_alg))

    def time_test(self):
        start_lib = time.time()
        hashlib.sha1(b"x" * 1000000).hexdigest()
        end_lib = time.time()
        print(end_lib - start_lib)
        

if __name__ == '__main__':
    unittest.main()
   
