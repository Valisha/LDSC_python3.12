# merge_with_rsID.py
import pandas as pd
# import pyyaml

# Print the output name
print(snakemake.output[0])

# Load the original GCST file
mLOX_tsv = pd.read_csv(snakemake.input.tsv, sep='\t')

# Load the intersection result
mLOX_merged = pd.read_csv(snakemake.input.merged_bed, sep='\t', header=None, names=['chromosome', 'base_pair_location', 'end', 'rsID'])

# Drop the 'end' column from mLOX_merged (not needed)
mLOX_merged = mLOX_merged.drop(columns=['end'])

# Merge the two dataframes on 'chromosome' and 'base_pair_location'
merged_df = pd.merge(mLOX_tsv, mLOX_merged, how='left', on=['chromosome', 'base_pair_location'])

# Save the merged dataframe to a new file
merged_df.to_csv(snakemake.output[0], sep='\t', index=False)

print("Merging complete. The output has been saved to", snakemake.output[0])

