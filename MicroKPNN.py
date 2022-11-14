import sys
import os
import subprocess
import argparse

######################
## PARSE ARGUMENTS ###
######################
parser = argparse.ArgumentParser(description='MicroKPNN')

# Inputs
parser.add_argument('inputBiomData', type=str, help='path to data file (.biom)')
parser.add_argument('inputMetadata', type=str, help='path to meta data file(.csv)')
parser.add_argument('diseaseName', type=str, help='name of the phenotype')
parser.add_argument('outputDir', type=str, help='path to output folder (must exist)')
parser.add_argument('--taxonomy', type=int, help='number corresponding to the taxonomy', default = -1) 
parser.add_argument('--h', type=int, help='number corresponding to the number of pure hidden nodes', default = -1)

# Computing limits
parser.add_argument('--threads', type=int, help="Parallelization number of thread", default=1)

args = parser.parse_args()

# Create sub directories in output directory
if not os.path.exists(f"{args.outputDir}/NetworkInput"):
    cmd = f"mkdir {args.outputDir}/NetworkInput"
    check_result=subprocess.check_output(cmd, shell=True)
if not os.path.exists(f"{args.outputDir}/Results"):
    cmd = f"mkdir {args.outputDir}/Results"
    check_result=subprocess.check_output(cmd, shell=True)
print("create/Check existance of NetworkInput dir and Results dir in directory ", args.outputDir )

# Create Data.csv and ClassLable.csv 
cmd = f"python lib/data.py {args.inputBiomData} {args.inputMetadata} {args.diseaseName} {args.outputDir}"
check_result=subprocess.check_output(cmd, shell=True)

print("Create Data.csv and ClassLabel.csv Done!")

if args.taxonomy == -1 or args.h==-1:
    if not os.path.exists(f"{args.outputDir}/NetworkInput/kingdom10"):
        cmd = f"python lib/create_edges.py --inp {args.inputBiomData} --out {args.outputDir}"
        check_result=subprocess.check_output(cmd, shell=True)
    print("All edges has been created/checked")
    cmd = f"python lib/runforall.py --inp {args.outputDir}"
    check_result=subprocess.check_output(cmd, shell=True)
else:
    cmd = f"python lib/edges.py --inp {args.inputBiomData} --taxonomy {args.taxonomy} --h {args.h} --out {args.outputDir}/NetworkInput"
    check_result=subprocess.check_output(cmd, shell=True)
    print("EdgeList has been created")
    data= args.outputDir+"/NetworkInput/Data.csv"
    classLabels=args.outputDir+"/NetworkInput/ClassLabels.csv"
    edges= args.outputDir+"/NetworkInput/EdgeList.csv"
    outPath=args.outputDir + "/Results/"
    cmd = "python lib/KPNN_Function.py --alpha=0.001 --lambd=0.2 " + data + " " + edges + " " + classLabels + " " +outPath
    check_result=subprocess.check_output(cmd, shell=True)
print("Well Done")

