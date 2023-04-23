import unittest

def d2b(number):
    binario = []
    number = int(number)
    if number == 0:
        binario.append(str(number))
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
    

def b2d(number):
    decimal_b = 0
    number = number[::-1]
    for i in range(len(number)):
        decimal_b += (int(number[i]) * (2**i))
    return decimal_b

def d2o(number):
    octal = []
    number = int(number)
    if number == 0:
        octal.append(str(number))
    while number != 0:
        if number <= 7:
            octal.append(number)
            number == 0
            break
        else:
            digit = number % 8
            octal.append(digit)
            number = number // 8
            if number == 0:
                octal.append(number)
    octal = octal[::-1]
    oct = ''.join(str(x) for x in octal)
    return oct

def o2d(number):
    decimal_o = 0
    number = str(number)[::-1]
    for i in range(len(number)):
        if number[i] == '9':
            return "INVALID NUMBER"
            break
        decimal_o += (int(number[i]) * (8**i))
    return str(decimal_o)

def d2h(number):
    hex = []
    number = int(number)
    if number == '0':
        hex.append(number)
    for i in range(len(str(number))):
        digit = number % 16
        if digit <= 9:
            hex.append(str(digit))
        else:
            if digit == 10:
                hex.append('A')
            elif digit == 11:
                hex.append('B')
            elif digit == 12:
                hex.append('C')
            elif digit == 13:
                hex.append('D')
            elif digit == 14:
                hex.append('E')
            elif digit == 15:
                hex.append('F')
        number = number // 16
        if number == 0:
            break
    hex = hex[::-1]
    hex = ''.join(str(x) for x in hex)
    return hex

def h2d(number):
    decimal_h = 0
    digit = 0
    number = number[::-1]
    for i in range(len(number)):
        if number[i].isalpha():
            
            if number[i] == 'A':
                digit = 10
            elif number[i] == 'B':
                digit = 11
            elif number[i] == 'C':
                digit = 12
            elif number[i] == 'D':
                digit = 13
            elif number[i] == 'E':
                digit = 14
            elif number[i] == 'F':
                digit = 15
        else:
            digit = int(number[i])
        decimal_h += digit * (16**i)
    return str(decimal_h)

def b2o(number):
    return d2o(b2d(number))

def b2h(number):
    return d2h(b2d(number))

def o2h(number):
    return d2h(o2d(number))

def o2b(number):
    return d2b(o2d(number))

def h2b(number):
    return d2b(h2d(number))

def h2o(number):
    return d2o(h2d(number))

if __name__ == '__main__':
    unittest.main()