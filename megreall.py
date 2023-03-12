import os
import fnmatch


data = os.listdir()
filenames = []
pattern = "*.txt"
for file in data:
    if fnmatch.fnmatch(file, pattern):
        filenames.append(file)

with open('combined.list', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())