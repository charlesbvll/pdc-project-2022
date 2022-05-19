import numpy as np
from utils import read_file, serialize_complex
from conversion import QAM

qam = QAM(256)

initial_str = read_file("initial.txt") 

result = qam.encode(initial_str[0])

serialize_complex(result, "input.txt")