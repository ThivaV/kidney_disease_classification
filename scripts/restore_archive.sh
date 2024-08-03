#!/bin/bash

# define variables
SOURCE="../data/master_data/part_*"
PART_PREFIX="part_"

# concatenate the parts
cat $SOURCE > ../data/master_data/restored_archive.tar.gz

# cleanup splits after the tar.gz file creation
rm ${PART_PREFIX}*