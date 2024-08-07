#!/bin/bash

# define variables
SOURCE="../docs/ref/end_to_end_deep_learning_with_mlflow-dvc-dagshub-and-deployment/end_to_end_deep_learning_with_mlflow-dvc-dagshub-and-deployment_part_*"
PART_PREFIX="end_to_end_deep_learning_with_mlflow-dvc-dagshub-and-deployment_part_"

# concatenate the parts
cat $SOURCE > ../docs/ref/end_to_end_deep_learning_with_mlflow-dvc-dagshub-and-deployment/end_to_end_deep_learning_with_mlflow-dvc-dagshub-and-deployment.tar.gz

# cleanup splits after the tar.gz file creation
rm ${PART_PREFIX}*