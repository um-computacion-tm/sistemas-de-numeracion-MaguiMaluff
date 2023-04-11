import unittest

def decimal2binario(number):
    binario = []
    while number != 0:
        if number == 1:
            binario.append(1)
            number == 0
            break
        else:
            digit = number % 2
            binario.append(digit)
            number = number // 2
    while len(binario) % 8 != 0:
        binario.append(0)
    binario = binario[::-1]
    bin = ''.join(str(x) for x in binario)
    return bin
    

def binario2decimal(number):
    decimal = 0
    for i in range(len(number)):
        if number[-(i + 1)] == '1':
            decimal += (1 * (2**i))
        i += 1
    return decimal



if __name__ == '__main__':
    unittest.main()