# MicroKPNN
 knowledge-primed neural network for microbiome-based predictions
 
 ### System requirements
 
 ### Installation
 biom :
  linux-64 v2.1.7
 ```
 conda create -n MicroKPNN python=3.7 tensorflow=1.13 pandas=0.24 numpy=1.16 scipy=1.2 psutil=5.6
 conda activate MicroKPNN	
 conda install -c conda-forge pytables=3.5
 conda install -c bioconda biom-format [conda install -c bioconda -c conda-forge biom-format
]
 conda install networkx
 
 ###for Analysis part
 conda install -c anaconda scikit-learn
 conda install -c conda-forge matplotlib
 ```
 
 ### Demo to use the MicroKPNN tool
 
 ```
 python MicroKPNN.py ExampleDataset/bracken.biom ExampleDataset/Supplementary_Table.csv Obesity output --taxonomy 0 --h 10 --threads 2

 ```

 ### Analysis
 depending on the number of runs and weather you wanna run it for 1 run or more than one run 
 it creates Analaysis dir in your output directory and put the results there. If you run for a single combination you would have a csv file in you Analysis directory which contains one line.
 If you run it for all the combination then in your Analysis would be contain a csv accuracy_results file that has all the combinations accuracy and also there is a plot directory that shos the comparison of different taxonomy with same pure hidden nodes number and also comparison of different number of pure hidden nodes in one taxonomy    
 ```
 python accuracy.py <for 1 combination or all combination> <numberofruns> <outputDir>
 ```
 
 ### Instructions on how to run MicorKPNNs on your data
Based on our results the combination od genus and ... would be better than the others ...
