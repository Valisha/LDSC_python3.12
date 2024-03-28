# LDSC_python3.12
Re-wrote LDSC tool for Shared heritability analysis for python3.12.
## Test

./munge_sumstats_vshah.py --out meta_20240328 --merge-alleles /path/to/eur_w_ld_chr/w_hm3.snplist --N 769475 --sumstats /path/to/european_ancestry.sumstats.tsv 

./munge_sumstats_vshah.py --out mLOY_20240328 --merge-alleles /path/to/eur_w_ld_chr/w_hm3.snplist --N 10000 --sumstats /path/to/mLOY.sumstats.tsv

### top 10 lines of both the summary statistics files

##### mLOY
snpid   hg18chr bp      a1      a2      or      se      pval    info    CEUaf
rs1569419       1       2996602 T       C       1.06    50.725099999999998      1.1E-12 0.977773        0.23352899999999999
rs2651932       1       3098661 G       A       1.08    31.5947 1.9000000000000001E-8   0.97676399999999997     8.920399999999995E-2
##### european_ancestry
chromosome      base_pair_location      effect_allele   other_allele    beta    standard_error  effect_allele_frequency p_value het_i2  het_p_value     n_samples       n_cases n_studies       rsid    variant_id
1       13668   A       G       -0.201445       0.371546        0.00596744      0.587694        NA      NA      307051  2095    1       rs2691328       1_13668_G_A
1       14773   T       C       0.19144 0.218039        0.0141618       0.379939        NA      NA      307051  2095    1       rs878915777     1_14773_C_T

The key to make this pipline work is mostly having the file headers right, the uploaded pipeline here should work for python3.12 if the summary statistics are in the correct format 

./ldsc.py --rg /path/to/mLOY.sumstats.gz,/path/to/european_ancestry.sumstats.gz --ref-ld-chr /path/to/eur_w_ld_chr/ --w-ld-chr /path/to/eur_w_ld_chr/ --out eur_mLOY_20240328
