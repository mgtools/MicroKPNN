# MicroKPNN
 knowledge-primed neural network for microbiome-based predictions
 
 ### System requirements
 
 ### Installation
 ```
 conda create -n MicroKPNN python=3.7 tensorflow=1.13 pandas=0.24 numpy=1.16 scipy=1.2 psutil=5.6
 conda activate MicroKPNN	
 conda install -c conda-forge pytables=3.5
 conda install -c bioconda biom-format
 conda install networkx
 ```
 
 ### Demo to use the MicroKPNN tool
 
 ```
 python MicroKPNN.py ExampleDataset/bracken.biom ExampleDataset/Supplementary_Table.csv Obesity output --taxonomy 0 --h 10 --threads 2

 ```

 ### Analysis
 
 ### Instructions on how to run KPNNs on your data
