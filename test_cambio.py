import unittest
from cambio import b2d, d2b, d2o, o2d, d2h, h2d, b2o, b2h, o2h, o2b, h2b, h2o


    
class TestNumeracion(unittest.TestCase):

##binario a decimal
    def test_b2d1(self):
        self.assertEqual(b2d('01011100'), 92)
    def test_b2d2(self):
        self.assertEqual(b2d('00000001'), 1)
    def test_b2dl0(self):
        self.assertEqual(b2d('00000000'), 0)
    def test_b2dl3(self):
        self.assertEqual(b2d('1111110000000'), 8064)

##decimal a binario
    def test_d2b1(self):
        self.assertEqual(d2b(97), '01100001')
    def test_d2b2(self):
        self.assertEqual(d2b(96), '01100000')
    def test_d2b3(self):
        self.assertEqual(d2b(1), '00000001')
    def test_d2b0(self):
        self.assertEqual(d2b(0), '00000000')  

##decimal a octal
    def test_d2o1(self):
        self.assertEqual(d2o(0), '0')
    def test_d2o2(self):
        self.assertEqual(d2o(3), '3')
    def test_d2o3(self):
        self.assertEqual(d2o(8), '10')
    def test_d2o4(self):
        self.assertEqual(d2o(28), '34')
    def test_d2o5(self):
        self.assertEqual(d2o(14586), '34372')

##octal a decimal
    def test_o2d1(self):
        self.assertEqual(o2d(10), '8')
    def test_o2d2(self):
        self.assertEqual(o2d(2), '2')
    def test_o2d3(self):
        self.assertEqual(o2d(34372), '14586')

##decimal a hexadecimal
    def test_d2h1(self):
        self.assertEqual(d2h(10), 'A')
    def test_d2h2(self):
        self.assertEqual(d2h(45), '2D')
    def test_d2h3(self):
        self.assertEqual(d2h(59762), 'E972')
    def test_d2h4(self):
        self.assertEqual(d2h('8064'), '1F80')

##hexadecimal a decimal
    def test_h2d1(self):
        self.assertEqual(h2d('A'), '10')
    def test_h2d2(self):
        self.assertEqual(h2d('2D'), '45')
    def test_h2d3(self):
        self.assertEqual(h2d('E972'), '59762')

##binario a octal
    def test_b2o1(self):
        self.assertEqual(b2o('00000000'), '0')
    def test_b2o2(self):
        self.assertEqual(b2o('00010000'), '20')
    def test_b2o3(self):
        self.assertEqual(b2o('11100011111010'), '34372')

##binario a hexadecimal
    def test_b2h1(self):
        self.assertEqual(b2h('00000000'), '0')
    def test_b2h2(self):
        self.assertEqual(b2h('1111110000000'), '1F80')

##octal a hexadecimal
    def test_o2h1(self):
        self.assertEqual(o2h('34512'), '394A')
    def test_o2h2(self):
        self.assertEqual(o2h('25'), '15')
    def test_o2h3(self):
        self.assertEqual(o2h('8258'), '10B0')

##octal a binario
    def test_o2b1(self):
        self.assertEqual(o2b('34512'), '0011100101001010')
    def test_o2b2(self):
        self.assertEqual(o2b('6515'), '0000110101001101')


##hexadecimal a binario
    def test_h2b1(self):
        self.assertEqual(h2b('394A'), '0011100101001010')
    def test_h2b2(self):
        self.assertEqual(h2b('2F75A'), '000000101111011101011010')

##hexadecimal a octal
    def test_h2o1(self):
        self.assertEqual(h2o('15'), '25')
    def test_h2o2(self):
        self.assertEqual(h2o('394A'), '34512')
    def test_h2o3(self):
        self.assertEqual(h2o('A0B0'), '120260')

if __name__ == '__main__':
    unittest.main()