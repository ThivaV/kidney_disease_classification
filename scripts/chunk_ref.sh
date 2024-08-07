#!/bin/bash

# define variables
SOURCE="end_to_end_deep_learning_with_mlflow-dvc-dagshub-and-deployment.tar.gz"
DESTINATION="../docs/ref/end_to_end_deep_learning_with_mlflow-dvc-dagshub-and-deployment"
PART_PREFIX="end_to_end_deep_learning_with_mlflow-dvc-dagshub-and-deployment_part_"
PART_SIZE="20M"

# split the archive into smaller parts
split -b $PART_SIZE $SOURCE $PART_PREFIX

# cleanup the tar.gz file
rm $SOURCE

mv end_to_end_deep_learning_with_mlflow-dvc-dagshub-and-deployment_part_* $DESTINATION