import numpy as np
from utils import read_file, serialize_complex
from conversion import to_qam


initial_str = read_file("initial.txt") 

result = to_qam(initial_str[0])

serialize_complex(result, "input.txt")