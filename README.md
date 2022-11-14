# MicroKPNN
 knowledge-primed neural network for microbiome-based predictions
 
 The prior-knowledge used in MicroKPNN includes the metabolic activities of different bacterial species, taxonomy level and community information
 ### System requirements
 MicroKPNN was developed on Ubunto and all scripts are in python. 
 
 ### Installation
 
 first you have to create a conda environment and install the required packages as following:

 ```
 conda create -n MicroKPNN python=3.7 tensorflow=1.13 pandas=0.24 numpy=1.16 scipy=1.2 psutil=5.6
 conda activate MicroKPNN	
 conda install -c conda-forge pytables=3.5
 conda install -c bioconda biom-format 
 conda install networkx
 
 ###for Analysis part
 conda install -c anaconda scikit-learn
 conda install -c conda-forge matplotlib
 ```
 If you are not able to install the biom-format using above command, use the following one instead:
 ```
 conda install -c bioconda -c conda-forge biom-format
 ```
 
 Installation instructions::
 
 ```
 git clone https://github.com/mgtools/MicroKPNN.git
 ```
 ### Demo to use the MicroKPNN tool
 In this repo we have exampleDataset and also it's output in single_output and output directories.
 
 Input for this tool:
 1. a .biom file (eg. output of kracken bracken) which contains metadate for species (taxonomy level information) and relative abundance. yu can see ExampleDataset/bracken.biom to see how your input should be look like. for more info about biom dataset you can take a look at https://biom-format.org/
 2. a .csv file which has corresponding samples in biom file and also a column with head names "Sample Accession or Sample ID" which contain sample ids and a column name "Phenotype" that has phenotype information for each sample. be carefull the healthy ones should be written as "Healthy" (the first character should be capital and the other ones should not be capital) you can see ExampleDataset/Supplementary_Table.csv to see how your input should be look like.
 3. phenotype you want to use. 
 4. 
 optional inputs:
 
 4. --taxonomy <number>
 
     0: kingdom
     
     1: phylum
     
     2: class
     
     3: order
     
     4: famiy
     
     5: genus
 
 5. --h <number>: number of pure hidden nodes you want to use 
 
 6. --thread <number>: if you don't put any numbers by default it would be 1

 
 single_output version:
 
 
 ```
 python MicroKPNN.py ExampleDataset/bracken.biom ExampleDataset/Supplementary_Table.csv Obesity output --taxonomy 0 --h 10 --threads 2

 ```
 
 All combination output version:
 
 ```
  python MicroKPNN.py ExampleDataset/bracken.biom ExampleDataset/Supplementary_Table.csv Obesity output --threads 2
 ```

 ### Analysis
 depending on the number of runs and weather you wanna run it for 1 run or more than one run 
 it creates Analaysis dir in your output directory and put the results there. If you run for a single combination you would have a csv file in you Analysis directory which contains one line.
 If you run it for all the combination then in your Analysis would be contain a csv accuracy_results file that has all the combinations accuracy and also there is a plot directory that shos the comparison of different taxonomy with same pure hidden nodes number and also comparison of different number of pure hidden nodes in one taxonomy    
 ```
 python accuracy.py <for 1 combination or all combination> <numberofruns> <outputDir>
 ```
 
 ```
 python impNodes_boxplot.py output/NetworkDir/kingdom10 output/Results/kingdom10 output/Analysis/ 2
 ```
 ### Instructions on how to run MicorKPNNs on your data
Based on our results the combination od genus and ... would be better than the others ...
 
Mention the difference between running on the server with GPU and without GPU:
 it takes around 1 hour to run for one combination and also around 40 to 50 hour to run for all combinations
 

