from __future__ import print_function
#!/usr/bin/env python
import sys
import os
import subprocess
import time
from time import gmtime, strftime
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--inp', type=str, required=True)
parser.add_argument('--alpha', type=str, required=True)
parser.add_argument('--lambd', type=str, required=True)
parser.add_argument('--dropOut', type=str, required=True)
args = parser.parse_args()


taxa = ['kingdom', 'phylum', 'class', 'order', 'family', 'genus']
meaninglessnodes = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']


data= args.inp+"/NetworkInput/Data.csv"
classLabels=args.inp+"/NetworkInput/ClassLabels.csv"
for t in taxa:
    for n in meaninglessnodes:
        edges= args.inp+"/NetworkInput/" + t + n + "/EdgeList.csv"
        print(edges)
        outPath=args.inp + "/Results/" + t + n
        cmd = "python lib/KPNN_Function.py --alpha="+args.alpha+" --lambd="+args.lambd+" --dropOut="+args.dropOut+" "+ data + " " + edges + " " + classLabels + " " +outPath
        subprocess.check_output(cmd, shell=True)
        print(t + n)


