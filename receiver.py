import numpy as np
from utils import read_file, write_final, compare, compute_score
from conversion import from_qam, list_to_strings

content = read_file("output.txt")
content = [complex(c) for c in content]

comps = from_qam(content)
strings = list_to_strings(comps)
finalText = compare(strings)

write_final(finalText)
compute_score()