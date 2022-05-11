import numpy as np
import itertools

const = [3/2+1j*3/2, 3/2+1j*1/2, 1/2+1j*3/2, 1/2+1j*1/2,
         3/2-1j*3/2, 3/2-1j*1/2, 1/2-1j*3/2, 1/2-1j*1/2,
         -3/2-1j*3/2, -3/2-1j*1/2, -1/2-1j*3/2,  -1/2-1j*1/2, 
         -3/2+1j*3/2, -3/2+1j*1/2, -1/2+1j*3/2, -1/2+1j*1/2]

codes = [['1000', '1001', '1100', '1101', '1010', '1011', '1110', '1111', '0010', '0011', '0110', '0111', '0000', '0001', '0100', '0101'],
        ['0000', '0100', '0001', '0101', '1000', '1100', '1001', '1101', '1010', '1110', '1011', '1111', '0010', '0110', '0011', '0111'],
        ['0010', '0011', '0110', '0111', '0000', '0001', '0100', '0101', '1000', '1001', '1100', '1101', '1010', '1011', '1110', '1111'],
        ['1010', '1110', '1011', '1111', '0010', '0110', '0011', '0111', '0000', '0100', '0001', '0101', '1000', '1100', '1001', '1101']]

def to_qam(s):
    result = []
    bytes_check = []
    for c in s:
        bits = bin(ord(c))[2:]
        byte = '00000000'[len(bits):] + bits
        bytes_check.append(byte)
        tmp = []
        for i in range(0, len(byte), 4):
            b = byte[i:i+4]
            if  b == '0000':
                tmp.append(-3/2+1j*3/2)
            elif b == '0100':
                tmp.append(-1/2+1j*3/2)
            elif b == '0001':
                tmp.append(-3/2+1j*1/2)
            elif b == '0101':
                tmp.append(-1/2+1j*1/2)

            elif b == '0011':
                tmp.append(-3/2-1j*1/2)
            elif b == '0111':
                tmp.append(-1/2-1j*1/2)
            elif b == '0010':
                tmp.append(-3/2-1j*3/2)
            elif b == '0110':
                tmp.append(-1/2-1j*3/2)

            elif b == '1100':
                tmp.append(1/2+1j*3/2)
            elif b == '1000':
                tmp.append(3/2+1j*3/2)
            elif b == '1101':
                tmp.append(1/2+1j*1/2)
            elif b == '1001':
                tmp.append(3/2+1j*1/2)

            elif b == '1111':
                tmp.append(1/2-1j*1/2)
            elif b == '1011':
                tmp.append(3/2-1j*1/2)
            elif b == '1110':
                tmp.append(1/2-1j*3/2)
            elif b == '1010':
                tmp.append(3/2-1j*3/2)
        result.extend(tmp)
    # print(bytes_check)
    return np.array(result)

def from_qam(s):
    tmp = ['','','','']
    # print("Complex Numbers : ", s)
    # print("Constellation : ", const)
    for c in s:
        for i, code in enumerate(codes):
            idx = np.argmin([abs(c-e) for e in const])
            tmp[i] += code[idx]
            # print("Best idx : ", idx)
            # print("Closest number : ", const[idx])
            # print("Closest seq : ", code[idx])
    
    res = []
    for r in tmp:
        res.append([r[i:i+8] for i in range(0, len(r), 8)])
        # print([r[i:i+8] for i in range(0, len(r), 8)])
    # print(res)
    return res

def list_to_strings(_list):
    strings = []
    for _bytes in _list:
        chars = []
        for byte in _bytes:
            u = int('0b' + byte, 2)
            chars.append(chr(u))
        strings.append(''.join(chars))
    return strings
