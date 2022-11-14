import pandas as pd
import networkx as nx
import csv
import argparse
import numpy as np
import sys
from biom import load_table

parser = argparse.ArgumentParser()
parser.add_argument('--inp', type=str, required=True)
parser.add_argument('--taxonomy', type=int, required=True)
parser.add_argument('--h', type=int, required=True)
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()


datas =  load_table(args.inp)
G = nx.read_gml("default_DATA/WT_spiec-easi.filtered.annotated.gml")
metabolite_file = "default_DATA/NJS16_metabolite_species_association.txt"


edges = []

# hierarchy
species_df = datas.metadata_to_dataframe('observation')
species = species_df.loc[:,["taxonomy_5","taxonomy_6"]].values
species = [s[0]+"|"+s[1] for s in species]
taxonomy_nodes = species_df["taxonomy_"+str(args.taxonomy)]

for i in range(len(species)):
        parent = taxonomy_nodes[i]
        parent = ''.join(parent.split(' '))
        parent =  ''.join(parent.split(','))
        parent =  ''.join(parent.split('('))
        parent =  ''.join(parent.split(')'))
        parent =  ''.join(parent.split('['))
        parent =  ''.join(parent.split(']'))
        parent =  ''.join(parent.split('&'))
        parent =  ''.join(parent.split('+'))
        edges.append((parent, species[i]))
    
print("number of taxonomys")
print(len(list(set(taxonomy_nodes))))


#community partition
gspecies = []
gpartition = []
for n in G.nodes:
    gspecies.append(G.nodes[n]["Species"])
    gpartition.append(G.nodes[n]["leidenpartition"])

community_nodes = []
for s in species:
    for i in range(len(gspecies)):
        new_s=s.split("|")[1][3:]
        if new_s == gspecies[i]:
            edges.append((gpartition[i], s))
            community_nodes.append(gpartition[i])
            break

print("number of communities")
print(len(list(set(community_nodes))))


# metabolte

metabolite = []
with open(metabolite_file, newline = '') as metabolites:
    metabolite_reader = csv.reader(metabolites, delimiter='\t') 
    for m in metabolite_reader:
        metabolite.append(m)
metabolite_nodes = []
for s in species:
    new_s=s.split("|")
    new_s = new_s[0][3:]+" "+new_s[1][3:]
    new_s = new_s.replace('_', ' ')
    for m in metabolite:
        if m[2] == new_s:
            parent = m[0] + ' ' + m[1]
            parent = ''.join(parent.split(' '))
            parent =  ''.join(parent.split(','))
            parent =  ''.join(parent.split('('))
            parent =  ''.join(parent.split(')'))
            parent =  ''.join(parent.split('['))
            parent =  ''.join(parent.split(']'))
            parent =  ''.join(parent.split('&'))
            parent =  ''.join(parent.split('+'))
            edges.append((parent,s))
            metabolite_nodes.append(parent)
print('number of metabolites')
print(len(list(set(metabolite_nodes))))


#hidden with no meaning

meaningless_nodes = []
for i in range(args.h):
    for s in species:
        parent = 'h' + str(i)
        meaningless_nodes.append(parent)
        edges.append((parent, s))
print("number of hidden nodes with no meaning")
print(len(list(set(meaningless_nodes))))

#output layer

output_edges = []

for r in edges:
    output_edges.append(('output', r[0]))

output_edges = list(set(output_edges))

newedges = output_edges + edges

parents = []
children = []
newedges = list(set(newedges))
for r in newedges:
    parents.append(r[0])
    children.append(r[1])
print("number of edges")
print(len(children))

taxonomy_nodes = list(set(taxonomy_nodes))
taxonomy_df = pd.DataFrame({'nodes':taxonomy_nodes})
taxonomy_df.to_csv(args.output + '/taxonomyNodes.csv', index = False)

community_nodes = list(set(community_nodes))
community_df = pd.DataFrame({'nodes': community_nodes})
community_df.to_csv(args.output + '/communityNodes.csv', index = False)

metabolite_nodes = list(set(metabolite_nodes))
metabolite_df = pd.DataFrame({'nodes':metabolite_nodes})
metabolite_df.to_csv(args.output + '/metaboliteNodes.csv', index = False)

meaningless_nodes = list(set(meaningless_nodes))
meaningless_df = pd.DataFrame({'nodes': meaningless_nodes})
meaningless_df.to_csv(args.output + '/meaninglessNodes.csv', index = False)


df = pd.DataFrame({'parent':parents, 'child':children})
df.to_csv(args.output + '/EdgeList.csv', index = False)

