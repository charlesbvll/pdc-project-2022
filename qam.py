from math import sqrt

import numpy as np

class QAM:
    def __init__(self, m):
        self.m = m
        self.const, self.code = self.make_const_code(m)
        self.K = 10

    def make_const_code(self, m):
        const = []
        code = []
        quad = int(m/4)
        sq = sqrt(m)
        N = int(sqrt(quad))
        for k in range(4):
            for i in range(N):
                for j in range(N):
                    s1 = -1 if k < 2 else 1
                    s2 = -1 if k % 2 == 0 else 1 
                    re = s1*(2*j+1)*(3/2)*(1/(sq-1))
                    im = s2*(2*i+1)*(3/2)*(1/(sq-1))
                    bits = bin(quad*k + N*i + j)[2:]
                    byte = '00000000'[len(bits):] + bits
                    const.append(complex(re, im))
                    code.append(byte)

        return const, code

    def encode(self, s):
        result = []
        tmp = ''
        N = int(np.log2(self.m))
        for c in s:
            bits = bin(ord(c))[2:]
            byte = ('0'*8)[len(bits):] + bits
            tmp += byte

        sep = [tmp[i:i+N] for i in range(0, len(tmp), N)]

        # Determine phase
        for _ in range(self.K):
            result.append(complex(1, 0))

        for byte in sep:
            result.append(self.const[int("".join(str(k) for k in byte), 2)])
        return np.array(result)

    def decode(self, s):
        phase = s[0:self.K-1]
        s = s[self.K: len(s)]
        tmp = ''
        theta = -np.angle(sum(phase))
        for c in s:
            shifted = c*np.exp(1j*(theta))
            idx = np.argmin([abs(shifted-e) for e in self.const])
            tmp += self.code[idx]
        return [tmp[i:i+8] for i in range(0, len(tmp), 8)]
