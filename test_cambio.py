import unittest
from cambio import binario2decimal
from cambio import decimal2binario

class TestNumeracion(unittest.TestCase):
    def test_binario2decimal1(self):
        self.assertEqual(binario2decimal('01011100'), 92)
    def test_binario2decimal2(self):
        self.assertEqual(binario2decimal('00000001'), 1)

##decimal a binario
    def test_decimal2binario1(self):
        self.assertEqual(decimal2binario(97), '01100001')
    def test_decimal2binario2(self):
        self.assertEqual(decimal2binario(96), '01100000')
    def test_decimal2binario3(self):
        self.assertEqual(decimal2binario(1), '00000001')

if __name__ == '__main__':
    unittest.main()