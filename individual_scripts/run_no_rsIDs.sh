#! /bin/bash

awk -F',' '$NF != ""' df_merged_intermediate.csv > mLOX_merged_with_python_script1.csv
