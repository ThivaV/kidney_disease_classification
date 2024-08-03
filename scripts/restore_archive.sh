#!/bin/bash

# define variables
SOURCE="../data/master_data/kidney_disease_ct_scan_dataset_part_*"
PART_PREFIX="kidney_disease_ct_scan_dataset_part_"

# concatenate the parts
cat $SOURCE > ../data/master_data/kidney_disease_ct_scan_dataset.tar.gz

# cleanup splits after the tar.gz file creation
rm ${PART_PREFIX}*