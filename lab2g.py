#!/usr/bin/env python3

# Author:Priyanshu Sargra
# Author ID:119660223
# Date Created:2025/02/03

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
