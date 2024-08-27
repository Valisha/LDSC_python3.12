
######## Snakemake header ########
import sys; sys.path.insert(0, "/n/app/snakemake/3.12.0/lib/python3.6/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05(XA\x00\x00\x00/n/scratch/users/v/vas485/mLOX/DATA/GCST90328148/GCST90328148.tsvq\x06XR\x00\x00\x00/n/scratch/users/v/vas485/mLOX/DATA/GCST90328148/GCST90328148.tsv.dbSnp.merged.bedq\x07e}q\x08(X\x06\x00\x00\x00_namesq\t}q\n(X\x03\x00\x00\x00tsvq\x0bK\x00N\x86q\x0cX\n\x00\x00\x00merged_bedq\rK\x01N\x86q\x0euh\x0bh\x06h\rh\x07ubX\x06\x00\x00\x00outputq\x0fcsnakemake.io\nOutputFiles\nq\x10)\x81q\x11X\x1d\x00\x00\x00GCST90328148_dbSnp_merged.tsvq\x12a}q\x13h\t}q\x14sbX\x06\x00\x00\x00paramsq\x15csnakemake.io\nParams\nq\x16)\x81q\x17}q\x18h\t}q\x19sbX\t\x00\x00\x00wildcardsq\x1acsnakemake.io\nWildcards\nq\x1b)\x81q\x1c}q\x1dh\t}q\x1esbX\x07\x00\x00\x00threadsq\x1fK\x01X\t\x00\x00\x00resourcesq csnakemake.io\nResources\nq!)\x81q"(K\x01K\x01e}q#(h\t}q$(X\x06\x00\x00\x00_coresq%K\x00N\x86q&X\x06\x00\x00\x00_nodesq\'K\x01N\x86q(uh%K\x01h\'K\x01ubX\x03\x00\x00\x00logq)csnakemake.io\nLog\nq*)\x81q+}q,h\t}q-sbX\x06\x00\x00\x00configq.}q/X\x04\x00\x00\x00ruleq0X\x0f\x00\x00\x00merge_with_rsIDq1ub.')
######## Original script #########
# merge_with_rsID.py
import pandas as pd

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

