#! /bin/python3

import pandas as pd

df_reference = pd.read_csv("/n/scratch/users/v/vas485/mLOX/DATA/dbSnp_reference_rsIDs.bed", sep = "\t")
df_input = pd.read_csv("/n/scratch/users/v/vas485/mLOX/DATA/GCST90328147.tsv", sep = "\t")
print("data read")
print(df_reference.iloc[0:5,0:2]) 
print(df_input.iloc[0:5, 0:2])

df_reference.columns = ["chr", "start", "end", "rsID"]
print(df_reference.columns)
print(df_input.columns)
# Merge on the chromosome and base pair location columns
df_input['chromosome'] = 'chr' + df_input['chromosome'].astype(str)
df_merged = pd.merge(df_input, df_reference, how='left', left_on=['chromosome', 'base_pair_location'], right_on=['chr', 'start'])
print(df_merged.iloc[0:5, 0:4])

# Drop unnecessary columns and keep only the required columns
df_merged = df_merged[['chromosome', 'base_pair_location', 'effect_allele', 'other_allele', 'beta', 'standard_error', 'effect_allele_frequency', 'p_value', 'z_score', 'rsID']]

# Display the merged DataFrame
print(df_merged.iloc[0:5, 0:4])

df_merged.to_csv("df_merged.csv")
