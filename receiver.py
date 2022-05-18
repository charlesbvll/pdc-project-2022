import numpy as np
from utils import read_file, write_final, compute_score
from conversion import from_qam, comps_to_string

content = read_file("output.txt")
content = [complex(c) for c in content]

comps = from_qam(content)
finalText = comps_to_string(comps)

write_final(finalText)
compute_score()