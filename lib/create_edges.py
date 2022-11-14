import os
import subprocess
import time
from time import gmtime, strftime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inp', type=str, required=True)
parser.add_argument('--out', type=str, required=True)
args = parser.parse_args()


taxa = {'0':'kingdom', '1':'phylum','2':'class', '3':'order', '4':'family', '5':'genus'}
meaninglessnodes = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']

#path=os.path.dirname(os.path.realpath(__file__))
for t in taxa.keys():
    for n in meaninglessnodes:
        cmd1 = 'mkdir '+ args.out+'/NetworkInput/' + taxa[t]+n 
        print('python lib/edges.py --inp ' + args.inp + ' --taxonomy ' +t+' --h '+n+' --out '+args.out+'/' + taxa[t]+n)

        cmd2 = 'python lib/edges.py --inp ' +args.inp + ' --taxonomy ' +t+' --h '+n+' --out '+args.out+'/NetworkInput/' + taxa[t]+n

        subprocess.check_output(cmd1, shell=True)
        subprocess.check_output(cmd2, shell=True)

