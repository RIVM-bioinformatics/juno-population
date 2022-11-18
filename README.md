# Juno-Population

A pipeline to investigate population structures.

## About this project
The Juno-population pipeline automates [popPUNK](https://www/poppunk.net). It is primarily used to categorize Streptococcus pneumoniae into Global Pneumococcal Sequence Clusters, though the pipeline can also support other species with popPUNK databases.

## Prerequisites
* **Linux environment**
* **(mini)conda**
* **Python3.8** Python is the scripting language used to create the pipeline

## Installation
1. Clone the repository.
```
git clone https://github.com/RIVM-bioinformatics/juno-population.git
```
2. Go to Juno directory.
```
cd juno-population
```
3. Create & activate mamba environment.
```
conda env update -f envs/mamba.yaml
```
```
conda activate mamba
```

4. Create & activate juno environment.
```
mamba env update -f envs/population_master.yaml
```
```
conda activate juno_population
```

7. Example of run:
```
python population.py -i [input] -o [output] --db [popPUNK_database]
```

## Parameters & Usage
### Command for help
* ```-h, --help``` Shows the help of the pipeline

### Required parameters
* ```-i, --input``` Path to a directory with fasta files or path to the output directory of the Juno-Assembly pipeline. It is important to link to the directory and not the files.

**One of the following**
* ```-b --db``` The name of (or path to) the popPUNK database, no trailing '/' when specifying a path. It overrides information provided with the --species argument.
* ```-s --species``` Full scientific name of the species. Use all lowercase and underscores between the parts of a name, not spaces (e.g. streptococcus_pneumoniae). This is a convenience function to find and set the popPUNK database. Only Streptococcus pneumoniae is currently supported within the RIVM bio-informatics environment. Extra species can be supported by including them in ```database_locations.py```.

### Optional parameters
* ```-o, --output```    Path to the directory that is used for the output. If none is given the default will be an output directory in the juno-population folder.
* ```--external-clustering```    Add if external cluster definitions should be used to name the clusters (see popPUNK and GPSC documentation). A ```{db_name}_external_clusters.csv``` file should be present in the popPUNK database directory when using this flag.
* ```-n --dryrun```     If you want to run a dry run use one of these parameters

### The base command to run this pipeline
```
python population.py -i [path/to/fasta_files/] --db [path/to/poppunk_db]
```
### Two examples of running this pipeline

When you want to provide a popPUNK database:
```
python population.py -i path/to/fasta_files/ -o output/ --db path/to/GPS_v6
```

When analyzing a supported species and the popPUNK database contains a cluster definition file that should be used:
```
python population.py -i path/to/fasta_files/ -o output/ -s streptococcus_pneumoniae --external-clustering
```

## Explanation of the output
* **log:** Log with output and error file from the cluster and for each Snakemake rule/step that is performed.
* **results_per_sample:** Directory with output produced by popPUNK for each sample.
* **q_files:** Directory containing the input for ```poppunk_assign```. Subsequent analysis by other popPUNK modules (e.g. ```poppunk_visualise``` or building a MST on large datasets) may require these files.
* **poppunk_clusters.csv:** Summary file with cluster definitions for each sample within the results_per_sample folder.

# TODO
* License
* Contact
* Previous information (see below)

# Previous information
Before running the pipeline be sure to initialize the submodules:
```bash
git submodule update --init --recursive
```
## Contribution guidelines
Juno pipelines use a [feature branch workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow). To work on features, create a branch from the `main` branch to make changes to. This branch can be merged to the main branch via a pull request. Hotfixes for bugs can be committed to the `main` branch.

Please adhere to the [conventional commits](https://www.conventionalcommits.org/) specification for commit messages. These commit messages can be picked up by [release please](https://github.com/googleapis/release-please) to create meaningful release messages.
