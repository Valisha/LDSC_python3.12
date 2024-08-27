#! /bin/python3

import pandas as pd

# Load the mLOX.tsv file
mLOX_tsv = pd.read_csv('GCST90328147.tsv', sep='\t')

# Load the mLOX_merged file
mLOX_merged = pd.read_csv('mLOX_dbSnp_merged.bed', sep='\t', header=None, names=['chromosome', 'base_pair_location', 'end', 'rsID'])

# Drop the 'end' column from mLOX_merged (not needed)
mLOX_merged = mLOX_merged.drop(columns=['end'])

# Merge the two dataframes on 'chromosome' and 'base_pair_location'
merged_df = pd.merge(mLOX_tsv, mLOX_merged, how='left', on=['chromosome', 'base_pair_location'])

# Save the merged dataframe to a new file
merged_df.to_csv('mLOX_merged_with_rsID.tsv', sep='\t', index=False)

print("Merging complete. The output has been saved to 'mLOX_merged_with_rsID.tsv'.")

