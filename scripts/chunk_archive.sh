#!/bin/bash

# define variables
SOURCE="../data/master_data/kidney_disease_ct_scan_dataset.tar.gz"
DESTINATION="../data/master_data/"
PART_PREFIX="part_"
PART_SIZE="20M"

# split the archive into smaller parts
split -b $PART_SIZE $SOURCE $PART_PREFIX

# cleanup the tar.gz file
rm $SOURCE

mv part_* $DESTINATION