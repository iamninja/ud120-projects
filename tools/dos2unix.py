#!/usr/bin/env python
"""
convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py
"""
import os

FILES = [
    "word_data.pkl",
    "email_authors.pkl",
    "../outliers/practice_outliers_net_worths.pkl",
    "../outliers/practice_outliers_ages.pkl",
    "../final_project/final_project_dataset.pkl"
]

def correct_endlines(file_name):
    """Replace crlf linefeeds with lf"""
    content = ''
    outsize = 0
    file_name_old = file_name + "_old"
    os.rename(file_name, file_name_old)
    with open(file_name_old, "rb") as infile:
        content = infile.read()
    with open(file_name, "wb") as output:
        for line in content.splitlines():
            outsize += len(line) + 1
            output.write(line + str.encode('\n'))

    os.remove(file_name_old)
    print("Done. Saved %s bytes." % (len(content)-outsize))

for file in FILES:
    correct_endlines(file)
    