import pandas as pd

# Define the chunk size
chunk_size = 1000  # Adjust based on your memory capacity

# Read the smaller input file in full
df_input = pd.read_csv("/n/scratch/users/v/vas485/mLOX/DATA/GCST90328147.tsv", sep="\t")
df_input['chromosome'] = 'chr' + df_input['chromosome'].astype(str)

# Initialize an empty DataFrame to store the final merged data
df_merged_all = pd.DataFrame()

counter = 0
# Process the reference file in chunks
for chunk in pd.read_csv("/n/scratch/users/v/vas485/mLOX/DATA/dbSnp_reference_rsIDs.bed", sep="\t", chunksize=chunk_size):
    # Rename columns for merging
    chunk.columns = ["chr", "start", "end", "rsID"]
    counter += 1
    print(counter)
    # Merge the chunk with the input DataFrame
    df_merged = pd.merge(df_input, chunk, how='left', left_on=['chromosome', 'base_pair_location'], right_on=['chr', 'start'])
    print(df_merged.iloc[0:5, 0:3])
    # Drop unnecessary columns and keep only the required columns
    df_merged = df_merged[['chromosome', 'base_pair_location', 'effect_allele', 'other_allele', 'beta', 'standard_error', 'effect_allele_frequency', 'p_value', 'z_score', 'rsID']]
    
    # Append the merged chunk to the final DataFrame
    df_merged_all = pd.concat([df_merged_all, df_merged], ignore_index=True)

    # Optional: Save intermediate results to disk to avoid data loss in case of failure
    df_merged_all.to_csv("df_merged_intermediate.csv", mode='a', header=False, index=False)

# After processing all chunks, save the final merged DataFrame to a CSV file
df_merged_all.to_csv("df_merged_final.csv", index=False)

print("Merging complete, final data saved.")

