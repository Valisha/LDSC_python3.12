#! /bin/bash

module load gcc/9.2.0 snakemake/7.32.3 bedtools/2.30.0 
module load python/3.10.11

snakemake -s Snakefile1 -p --cores 4
