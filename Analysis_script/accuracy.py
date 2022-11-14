from __future__ import print_function
import sys
import os
import subprocess
import argparse
import time
from time import gmtime, strftime
import pandas as pd
import csv
import numpy as np
from sklearn import metrics
from statistics import mean
import matplotlib.pyplot as plt


######################
## PARSE ARGUMENTS ###
######################
parser = argparse.ArgumentParser(description='MicroKPNN')

# Inputs
parser.add_argument('oneORall_combinations', type=int, help='weather we have one combination or all combinations of taxonomy and hidden nodes')
parser.add_argument('Number_of_runs', type=int, help='Number of runs we have')
parser.add_argument('outputDir', type=str, help='path to output directory')

args = parser.parse_args()
if not os.path.exists(f"../{args.outputDir}/Analysis"):
    cmd = f"mkdir ../{args.outputDir}/Analysis"
    check_result=subprocess.check_output(cmd, shell=True)

if args.oneORall_combinations == 1:
    runs = ["run_"+str(i) for i in range(1,args.Number_of_runs+1)]
    runs_auc = []
    for r in runs:
        yHat_path = f"../{args.outputDir}/Results/{r}/tf_yHat_test.csv"
        yHat_file = open(yHat_path)
        yHat_csvreader = csv.reader(yHat_file)
        yHat_header = []
        yHat_header = next(yHat_csvreader)
        yHat = []
        for row in yHat_csvreader:
            yHat.append(float(row[0]))

        yTrue_path = f"../{args.outputDir}/Results/{r}/tf_yTrue_test.csv"
        yTrue_file = open(yTrue_path)
        yTrue_csvreader = csv.reader(yTrue_file)
        yTrue_header = []
        yTrue_header = next(yTrue_csvreader)
        yTrue = []
        for row in yTrue_csvreader:
            yTrue.append(float(row[0]))
        yTrue = np.array(yTrue)
        yHat = np.array(yHat)
        fpr, tpr, thresholds = metrics.roc_curve(yTrue, yHat, pos_label = 1)
        auc = metrics.auc(fpr, tpr)
        runs_auc.append(auc)
    data = ["your combination choice"] + runs_auc + [mean(runs_auc)]
    datas = []
    datas.append(data)
    columns = ['file']+runs+['avg']
    df = pd.DataFrame(datas, columns=columns)


    df.to_csv(f"../{args.outputDir}/Analysis/auc_results.csv", index=False)



else:
    taxa= ['kingdom', 'phylum', 'class', 'order', 'family', 'genus']
    meaninglessnodes = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
    runs = ["run_"+str(i) for i in range(1,args.Number_of_runs+1)]

    kingdom = { "data": [], 'CTEs':[], 'error':[], 'labels':['10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] }
    phylum = { "data": [], 'CTEs':[], 'error':[], 'labels':['10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] } 
    classes = { "data": [], 'CTEs':[], 'error':[], 'labels':['10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] }
    order = { "data": [], 'CTEs':[], 'error':[], 'labels':['10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] }
    family = { "data": [], 'CTEs':[], 'error':[], 'labels':['10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] }
    genus = { "data": [], 'CTEs':[], 'error':[], 'labels':['10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] }

    n_10 = { "data": [], 'CTEs':[], 'error':[], 'labels':['kingdom', 'phylum', 'class', 'order', 'family', 'genus'] }
    n_20 = { "data": [], 'CTEs':[], 'error':[], 'labels':['kingdom', 'phylum', 'class', 'order', 'family', 'genus'] }
    n_30 = { "data": [], 'CTEs':[], 'error':[], 'labels':['kingdom', 'phylum', 'class', 'order', 'family', 'genus'] }
    n_40 = { "data": [], 'CTEs':[], 'error':[], 'labels':['kingdom', 'phylum', 'class', 'order', 'family', 'genus'] }
    n_50 = { "data": [], 'CTEs':[], 'error':[], 'labels':['kingdom', 'phylum', 'class', 'order', 'family', 'genus'] }
    n_60 = { "data": [], 'CTEs':[], 'error':[], 'labels':['kingdom', 'phylum', 'class', 'order', 'family', 'genus'] }
    n_70 = { "data": [], 'CTEs':[], 'error':[], 'labels':['kingdom', 'phylum', 'class', 'order', 'family', 'genus'] }
    n_80 = { "data": [], 'CTEs':[], 'error':[], 'labels':['kingdom', 'phylum', 'class', 'order', 'family', 'genus'] }
    n_90 = { "data": [], 'CTEs':[], 'error':[], 'labels':['kingdom', 'phylum', 'class', 'order', 'family', 'genus'] }
    n_100 = { "data": [], 'CTEs':[], 'error':[], 'labels':['kingdom', 'phylum', 'class', 'order', 'family', 'genus'] }

    datas = []
    for t in taxa:
        for n in meaninglessnodes:
            runs_auc = []
            for r in runs:
                yHat_path = f"{../args.outputDir}/Results/{t}{n}/{r}/tf_yHat_test.csv"
                yHat_file = open(yHat_path)
                yHat_csvreader = csv.reader(yHat_file)
                yHat_header = []
                yHat_header = next(yHat_csvreader)
                yHat = []
                for row in yHat_csvreader:
                    yHat.append(float(row[0]))

                yTrue_path = f"../{args.outputDir}/Results/{t}{n}/{r}/tf_yTrue_test.csv"
                yTrue_file = open(yTrue_path)
                yTrue_csvreader = csv.reader(yTrue_file)
                yTrue_header = []
                yTrue_header = next(yTrue_csvreader)
                yTrue = []
                for row in yTrue_csvreader:
                    yTrue.append(float(row[0]))

                yTrue = np.array(yTrue)
                yHat = np.array(yHat)
                fpr, tpr, thresholds = metrics.roc_curve(yTrue, yHat, pos_label = 1)
                auc = metrics.auc(fpr, tpr)
                runs_auc.append(auc)
            data = [t+n] + runs_auc + [mean(runs_auc)]
            datas.append(data)
        
            if t == 'kingdom':
                kingdom['data'].append(np.array(runs_auc))
                kingdom['CTEs'].append(np.mean(runs_auc))
                kingdom['error'].append(np.std(runs_auc))
            if t == 'phylum':
                phylum['data'].append(np.array(runs_auc))
                phylum['CTEs'].append(np.mean(runs_auc))
                phylum['error'].append(np.std(runs_auc))
            if t == 'class':
                classes['data'].append(np.array(runs_auc))
                classes['CTEs'].append(np.mean(runs_auc))
                classes['error'].append(np.std(runs_auc))
            if t == 'order':
                order['data'].append(np.array(runs_auc))
                order['CTEs'].append(np.mean(runs_auc))
                order['error'].append(np.std(runs_auc))
            if t == 'family':
                family['data'].append(np.array(runs_auc))
                family['CTEs'].append(np.mean(runs_auc))
                family['error'].append(np.std(runs_auc))
            if t == 'genus':
                genus['data'].append(np.array(runs_auc))
                genus['CTEs'].append(np.mean(runs_auc))
                genus['error'].append(np.std(runs_auc))
            if n == '10':
                n_10['data'].append(np.array(runs_auc))
                n_10['CTEs'].append(np.mean(runs_auc))
                n_10['error'].append(np.std(runs_auc))
            if n == '20':
                n_20['data'].append(np.array(runs_auc))
                n_20['CTEs'].append(np.mean(runs_auc))
                n_20['error'].append(np.std(runs_auc))
            if n == '30':
                n_30['data'].append(np.array(runs_auc))
                n_30['CTEs'].append(np.mean(runs_auc))
                n_30['error'].append(np.std(runs_auc))
            if n == '40':
                n_40['data'].append(np.array(runs_auc))
                n_40['CTEs'].append(np.mean(runs_auc))
                n_40['error'].append(np.std(runs_auc))
            if n == '50':
                n_50['data'].append(np.array(runs_auc))
                n_50['CTEs'].append(np.mean(runs_auc))
                n_50['error'].append(np.std(runs_auc))
            if n == '60':
                n_60['data'].append(np.array(runs_auc))
                n_60['CTEs'].append(np.mean(runs_auc))
                n_60['error'].append(np.std(runs_auc))
            if n == '70':
                n_70['data'].append(np.array(runs_auc))
                n_70['CTEs'].append(np.mean(runs_auc))
                n_70['error'].append(np.std(runs_auc))
            if n == '80':
                n_80['data'].append(np.array(runs_auc))
                n_80['CTEs'].append(np.mean(runs_auc))
                n_80['error'].append(np.std(runs_auc))
            if n == '90':
                n_90['data'].append(np.array(runs_auc))
                n_90['CTEs'].append(np.mean(runs_auc))
                n_90['error'].append(np.std(runs_auc))
            if n == '100':
                n_100['data'].append(np.array(runs_auc))
                n_100['CTEs'].append(np.mean(runs_auc))
                n_100['error'].append(np.std(runs_auc))



    columns = ['file']+runs+['avg']
    df = pd.DataFrame(datas, columns=columns)


    df.to_csv(f"../{args.outputDir}/Analysis/auc_results.csv", index=False)

    labels = [kingdom, phylum, classes, order, family, genus, n_10, n_20, n_30, n_40, n_50, n_60, n_70, n_80, n_90, n_100]
    labels_str = ['kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'n_10', 'n_20', 'n_30', 'n_40', 'n_50', 'n_60', 'n_70', 'n_80', 'n_90', 'n_100']

    def plots(label, label_str):
        x_pos = np.arange(len(label['labels']))
        fig, ax = plt.subplots()
        ax.bar(x_pos, label['CTEs'], yerr=label['error'], align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('AUC')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(label['labels'])
        ax.set_title(label_str+' AUC')
        ax.yaxis.grid(True)
        # Save the figure and show
        plt.tight_layout()
        plt.savefig(f"../args.ouputDir/Analysis/plots/{label_str}_plot.png")

    for i in range(len(labels)):
        plots(labels[i], labels_str[i])
