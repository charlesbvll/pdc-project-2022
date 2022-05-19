import numpy as np
from utils import read_file, write_final, compute_score, compare
from conversion import from_qam, from_qam_to_list, comps_to_string, list_to_strings

content = read_file("output.txt")
content = [complex(c) for c in content]

_list = from_qam_to_list(content)
strings = list_to_strings(_list)
finalText = compare(strings)

# Without comparaison
# comps = from_qam(content)
# finalText = comps_to_string(comps)

write_final(finalText)

compute_score()