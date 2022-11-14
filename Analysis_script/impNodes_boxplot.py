from pandas import*
import csv
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
import pandas as pd
import subprocess
import argparse

parser = argparse.ArgumentParser(description='MicroKPNN')

# Inputs

parser.add_argument('inputNetworkDir', type=str, help='path to directory containing edges info')
parser.add_argument('inputResultDir', type=str, help='path to directory containing runs')
parser.add_argument('outputDir', type=str, help='path to directory wants the results saved')
parser.add_argument('number_of_runs', type=int, help='number_of_runs')

args = parser.parse_args()

path = "run_"
nodeactivation = []
for i in range(1,args.number_of_runs+1):
    rpath = args.inputResultDir+"/"+path+str(i) + "/tf_NumGradMeans.csv"
    rfile = open(rpath)
    r_csvreader = csv.reader(rfile)
    header = next(r_csvreader)

    if i == 1:
        for row in r_csvreader:
            nodeactivation.append([row[0], abs(float(row[1]))])
    else:
        j = 0
        for row in r_csvreader:
            nodeactivation[j][1] += abs(float(row[1]))
            j+=1

for i in range(len(nodeactivation)):
    nodeactivation[i][1] /= args.number_of_runs
    nodeactivation[i][1] = str(nodeactivation[i][1])

df = pd.DataFrame(nodeactivation, columns = header)
df.to_csv(args.outputDir+"/avg_tf_NumGradMeans.csv", index = False)

#####################################################################
plt.figure(figsize=(1,1))
plt.rcParams.update({'font.size': 24})

taxonomy_path = f"{args.inputNetworkDir}/taxonomyNodes.csv"
metabolite_path = f"{args.inputNetworkDir}/metaboliteNodes.csv"
meaningless_path = f"{args.inputNetworkDir}/meaninglessNodes.csv"
community_path = f"{args.inputNetworkDir}/communityNodes.csv"

taxonomy_csvreader = read_csv(taxonomy_path)["nodes"].tolist() 
metabolite_csvreader = read_csv(metabolite_path)["nodes"].tolist()
meaningless_csvreader = read_csv(meaningless_path)["nodes"].tolist()
community_csvreader = read_csv(community_path)["nodes"].tolist()
for i in range(len(community_csvreader)):
    community_csvreader = str(community_csvreader)

taxonomy=[]
metabolite=[]
meaningless=[]
community=[]

#for i in range(1,6):
run_path = args.outputDir+"/avg_tf_NumGradMeans.csv"
run_file = open(run_path)
run_csvreader = csv.reader(run_file)
run_header=[]
run_header=next(run_csvreader)
for row in run_csvreader:
    if row[0] in taxonomy_csvreader:
        taxonomy.append(abs(float(row[1])))
    elif row[0] in metabolite_csvreader:
        metabolite.append(abs(float(row[1])))
    elif row[0] in meaningless_csvreader:
        meaningless.append(abs(float(row[1])))
    elif row[0] in community_csvreader:
        community.append(abs(float(row[1])))

taxonomy.sort()
metabolite.sort()
meaningless.sort()
community.sort()

taxonomy.reverse()
metabolite.reverse()
meaningless.reverse()
community.reverse()

taxonomy = taxonomy[:20]
metabolite = metabolite[:20]
meaningless = meaningless[:20]
community = community[:20]


data = [taxonomy, metabolite, meaningless, community]

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

# Creating axes instance
bp = ax.boxplot(data, patch_artist = True,
                notch ='True', vert = 0)

colors = ['b', 'r',
          'y', 'g']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='k',
                linewidth = 1.5,
                linestyle =":")

# changing color and linewidth of
# caps
for cap in bp['caps']:
    cap.set(color ='k',
            linewidth = 2)

# changing color and linewidth of
# medians
for median in bp['medians']:
    median.set(color ='k',
               linewidth = 3)

# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D',
              color ='k',
              alpha = 0.5)

# x-axis labels
ax.set_yticklabels(['taxonomy', 'metabolite',
                    'meaningless', 'community'])


# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.tight_layout()

plt.savefig(args.outputDir+"/score_plot.png")


