# -*- coding: utf-8 -*-


def xor_chipher(line, key):
    line = int(line) ^ int(key)
    return line


def xor_unchipher(line):
    key = 222
    xor = line ^ key
    return print(xor)

import unittest

class XORTestCase (unittest.TestCase):
    def test_cipher(self):
            self.assertEqual (XOR_cipher ("Hello","1"),"yT]]^")

    def test_uncipher(self):
            self.assertEqual (XOR_uncipher ("yT]]^","1"),"Hello")

    def test_equality(self):
            string,key = "Python","World"
            self.assertEqual (XOR_uncipher (XOR_cipher (string,key),key),string)

    def test_cipher_same_key(self):
            string = "ABCDFF"
            self.assertEqual (XOR_cipher (string,string),"\0" * len (string))

    def test_cipher_large_key(self):
            self.assertEqual (XOR_cipher ("1","Hello"),"y")

if __name__ == "__main__":
    unittest.main ()

        #if __name__=='__main__':
#    a = '5555522225'
#    b = '222'
#    c = xor_chipher(a, b)
#    print(c)
#    xor_unchipher(c)