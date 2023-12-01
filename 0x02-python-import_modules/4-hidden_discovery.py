#!/usr/bin/python3
import sys
import os
import hidden_4

folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "hidden_4_F")

sys.path.append(folder_path)

if __name__ == "__main__":
    names = dir(hidden_4)
for name in names:
    if name[:2] != "__":
        print(name)
