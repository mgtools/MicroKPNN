from biom import load_table
import pandas as pd
import numpy as np
import sys
import argparse

parser = argparse.ArgumentParser(description='Abundance profile Input')

# Inputs
parser.add_argument('inputData', type=str, help='path to data file (.biom)')
parser.add_argument('inputMetaData', type=str, help='path to meta data file (.csv)')
parser.add_argument('diseaseName', type=str, help='phenotypes name')
parser.add_argument('output', type=str, help='output directory')
#print(sys.argv)
args = parser.parse_args()
#print(args)


### read metadata file and creates classLabel.csv file

df = pd.read_csv(args.inputMetaData, usecols = ['Sample Accession or Sample ID','Phenotype'])
healthydf = df.loc[df['Phenotype'] == 'Healthy']
diseasedf = df.loc[df['Phenotype'] == args.diseaseName]

if healthydf.shape[0]>diseasedf.shape[0]:
    healthydf = healthydf.sample( n = diseasedf.shape[0])

healthydf['Phenotype'] = healthydf['Phenotype'].replace('Healthy',0)
diseasedf['Phenotype'] = diseasedf['Phenotype'].replace(args.diseaseName,1)
classLabel_df = pd.concat([healthydf, diseasedf], axis=0)
classLabel_df = classLabel_df.rename(columns={"Sample Accession or Sample ID":"barcode", "Phenotype":"output"})
classLabel_df.to_csv(args.output+'/NetworkInput/ClassLabels.csv', index = False)


### read biom file and creates Data.csv file

table = load_table(args.inputData)
species_df = table.metadata_to_dataframe('observation')
species_ids = species_df.loc[:,["taxonomy_5","taxonomy_6"]].values
genusspecies_ids = [s[0]+"|"+s[1] for s in species_ids]
sample_ids = table.ids('sample')
data = []
for s in sample_ids:
    srow = table.data(s) 
    data.append(srow)
sample_ids = [s for s in sample_ids]
data = np.transpose(data)
data_df = pd.DataFrame(data = data, index = genusspecies_ids, columns = sample_ids)
data_df = data_df[~data_df.index.duplicated(keep='first')]
data_df = data_df[np.array(classLabel_df["barcode"])]
sum_col=data_df.sum(axis=0)
for col in data_df.columns:
    data_df[col]=data_df[col]/sum_col[col]
data_df.to_csv(args.output+'/NetworkInput/Data.csv')



