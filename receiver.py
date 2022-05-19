import numpy as np
from utils import read_file, write_final, compute_score, compare
from conversion import QAM, comps_to_string, list_to_strings

qam = QAM(256)

content = read_file("output.txt")
content = [complex(c) for c in content]

_list = qam.decode_to_list(content)
strings = list_to_strings(_list)
finalText = compare(strings)

# Without comparaison
# comps = qam.decode(content)
# finalText = comps_to_string(comps)

write_final(finalText)

compute_score()