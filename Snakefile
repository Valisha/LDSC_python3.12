# Load the config.yaml file
# configfile: "/n/scratch/users/v/vas485/mLOX/DATA/SCRIPTS/config.yaml"

# Extract the variables from the config file
# MAIN_INPUT = config['main_input']
MAIN_INPUT = "/n/scratch/users/v/vas485/mLOX/DATA/GCST90328150/GCST90328150.bed"
db_SNP_INPUT = "/n/scratch/users/v/vas485/mLOX/DATA/dbSnps/dbSnp153_sort_nochr.bed"
INPUT_TSV = "/n/scratch/users/v/vas485/mLOX/DATA/GCST90328150/GCST90328150.tsv"
# DB_SNP_INPUT = config['db_snp_input']
# CORES = config['resources']['cores']
# MEMORY = config['resources']['memory']
# THREADS = config['resources']['threads']

rule all:
    input:
        "GCST90328150_dbSnp_merged.tsv"
rule cut_bed:
    input:
        MAIN_INPUT
    output:
        MAIN_INPUT + ".cut.bed"
    shell:
        """
        cut -f1,2,3,4 {input} > {output}
        """

rule add_end_column:
    input:
        MAIN_INPUT + ".cut.bed"
    output:
        MAIN_INPUT + ".with.end.bed"
    shell:
        """
        awk 'BEGIN{{OFS="\t"}} {{print $1, $2, $2+1}}' {input} > {output}
        """

rule sort_bed:
    input:
        MAIN_INPUT + ".with.end.bed"
    output:
        MAIN_INPUT + ".with.end.sort.bed"
    shell:
        """
        sort -k1,1 -k2,2n -k3,3n {input} > {output}
        """

#rule remove_chr_prefix:
#    input:
#        MAIN_INPUT + ".sort.bed"
#    output:
#        MAIN_INPUT + ".sort.nochr.bed"
#    shell:
#        """
#        sed 's/^chr//' {input} > {output}
#        """


rule bedtools_intersect:
    input:
        bed=db_SNP_INPUT,
        a_file=MAIN_INPUT + ".with.end.sort.bed"
    output:
        MAIN_INPUT + ".dbSnp.merged.bed"
    shell:
        """
        bedtools intersect -b {input.a_file} -a {input.bed} -sorted > {output}
        """

rule merge_with_rsID:
    input:
        tsv=INPUT_TSV,
        merged_bed=MAIN_INPUT + ".dbSnp.merged.bed"
    output:
        "GCST90328150_dbSnp_merged.tsv"
    script:
        "/n/scratch/users/v/vas485/mLOX/DATA/SCRIPTS/merge_with_rsID.py"

# bedtools intersect -a ../dbSnps/dbSnp153_sort_nochr.bed -b ../GCST90328147/mLOX_with_end_sorted.bed -sorted
#        """
#        import pandas as pd
#
#        ### print the output name 
#        print(snakemake.output[0])
#        # Load the original GCST file
#        mLOX_tsv = pd.read_csv(snakemake.input.tsv, sep='\t')
#
#        # Load the intersection result
#        mLOX_merged = pd.read_csv(snakemake.input.merged_bed, sep='\t', header=None, names=['chromosome', 'base_pair_location', 'end', 'rsID'])
#
#        # Drop the 'end' column from mLOX_merged (not needed)
#        mLOX_merged = mLOX_merged.drop(columns=['end'])
#
#        # Merge the two dataframes on 'chromosome' and 'base_pair_location'
#        merged_df = pd.merge(mLOX_tsv, mLOX_merged, how='left', on=['chromosome', 'base_pair_location'])
#
#        # Save the merged dataframe to a new file
#        merged_df.to_csv(snakemake.output[0], sep='\t', index=False)
#
#        print("Merging complete. The output has been saved to", snakemake.output[0])
#        """

