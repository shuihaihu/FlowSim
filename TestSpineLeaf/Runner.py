__author__ = 'lich'

import os

for mean in [10, 100, 300, 500]:
    for a in [1, 5, 10]:
        os.system("python TestSimulator.py -S 100 -L %d -a %d" % (mean, a))
