import numpy as np
import itertools

const = [3/2+1j*3/2, 3/2+1j*1/2, 1/2+1j*3/2, 1/2+1j*1/2,
         3/2-1j*3/2, 3/2-1j*1/2, 1/2-1j*3/2, 1/2-1j*1/2,
         -3/2-1j*3/2, -3/2-1j*1/2, -1/2-1j*3/2,  -1/2-1j*1/2, 
         -3/2+1j*3/2, -3/2+1j*1/2, -1/2+1j*3/2, -1/2+1j*1/2]

codes = [['0000', '0001', '0010', '0011',   '0100', '0101', '0110', '0111',    '1000', '1001', '1010', '1011',    '1100', '1101', '1110', '1111'],
         ['0001', '0101', '0000', '0011',   '0110', '0100', '1010', '0111',    '1001', '1101', '1000', '1011',    '1110', '1100', '0010', '1111'],
         ['0101', '0100', '0001', '0111',   '1010', '0110', '1000', '1011',    '1101', '1100', '1001', '1111',    '0010', '1110', '0000', '0011'],
         ['0100', '0110', '0101', '0111',   '1000', '1010', '1001', '1011',    '1100', '1110', '1101', '1111',    '0000', '0010', '0001', '0011'],
         
         ['0110', '1010', '0100', '1011',   '1001', '1000', '1101', '1111',    '1110', '0010', '1100', '0011',    '0001', '0000', '0101', '0111'],
         ['1010', '1000', '0110', '1011',   '1101', '1001', '1100', '1111',    '0010', '0000', '1110', '0011',    '0101', '0001', '0100', '0111'],
         ['1000', '1001', '1010', '1111',   '1100', '1101', '1110', '0011',    '0000', '0001', '0010', '0111',    '0100', '0101', '0110', '1011'],
         ['1001', '1101', '1000', '1111',   '1110', '1100', '0010', '0011',    '0001', '0101', '0000', '0111',    '0110', '0100', '1010', '1011'],
         
         ['1101', '1100', '1001', '0011',   '0010', '1110', '0000', '0111',    '0101', '0100', '0001', '1011',    '1010', '0110', '1000', '1111'],
         ['1100', '1110', '1101', '0011',   '0000', '0010', '0001', '0111',    '0100', '0110', '0101', '1011',    '1000', '1010', '1001', '1111'],
         ['1110', '0010', '1100', '0111',   '0001', '0000', '0101', '1011',    '0110', '1010', '0100', '1111',    '1001', '1000', '1101', '0011'],
         ['0010', '0000', '1110', '0111',   '0101', '0001', '0100', '1011',    '1010', '1000', '0110', '1111',    '1101', '1001', '1100', '0011']]  

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
            tmp.append(const[int("".join(str(k) for k in b), 2)])
        result.extend(tmp)
    # print(bytes_check)
    return np.array(result)

def from_qam(s):
    tmp = ['']*len(codes)
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
