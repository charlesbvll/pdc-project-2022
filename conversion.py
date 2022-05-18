import itertools

import numpy as np

from utils import make_const_code

const, code = make_const_code(256)

def to_qam(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        byte = '00000000'[len(bits):] + bits
        result.append(const[int("".join(str(k) for k in byte), 2)])
    return np.array(result)

def from_qam(s):
    tmp = ''
    theta = np.angle(s[0])
    for c in s:
        shifted = abs(c)*np.exp(1j*theta)
        idx = np.argmin([abs(shifted-e) for e in const])
        tmp += code[idx]
    return [tmp[i:i+8] for i in range(0, len(tmp), 8)]

def comps_to_string(_bytes):
    chars = []
    for byte in _bytes:
        u = int('0b' + byte, 2)
        chars.append(chr(u))
    return ''.join(chars)
