import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir, "preproinsulin-seq.txt")

with open(file_path, "r") as file:
    data = file.read()

cleaned = re.sub(r"ORIGIN|//|\d+|\s+", "", data).lower()

with open(os.path.join(base_dir, "preproinsulin-seq-clean.txt"), "w") as file:
    file.write(cleaned)

lsinsulin = cleaned[:24]
binsulin = cleaned[24:54]
cinsulin = cleaned[54:89]
ainsulin = cleaned[89:110]

with open(os.path.join(base_dir, "lsinsulin-seq-clean.txt"), "w") as file:
    file.write(lsinsulin)

with open(os.path.join(base_dir, "binsulin-seq-clean.txt"), "w") as file:
    file.write(binsulin)

with open(os.path.join(base_dir, "cinsulin-seq-clean.txt"), "w") as file:
    file.write(cinsulin)

with open(os.path.join(base_dir, "ainsulin-seq-clean.txt"), "w") as file:
    file.write(ainsulin)

print(f"preproinsulin-seq-clean.txt produced verified with having {len(cleaned)} chars")
print(f"lsinsulin-seq-clean.txt produced with {len(lsinsulin)} chars")
print(f"binsulin-seq-clean.txt produced with {len(binsulin)} chars")
print(f"cinsulin-seq-clean.txt produced with {len(cinsulin)} chars")
print(f"ainsulin-seq-clean.txt produced with {len(ainsulin)} chars")