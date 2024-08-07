# Kidney disease classification

- [Dataset](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone/data)
- [Keras pre-trained models](https://keras.io/api/applications/)
- [MLflow](https://mlflow.org/docs/latest/index.html)

- MLFLOW environment variables:
    - `export MLFLOW_TRACKING_URI=<TRACK URI>`
    - `export MLFLOW_TRACKING_USERNAME=<USERNAME>`
    - `export MLFLOW_TRACKING_PASSWORD=<PASSWORD>`

- DVC commands:
    - Create the `dvc.yaml` file
    - Execute: `dvc init`
    - Execute: `dvc repro`
    - Generate dependency graph: `dvc dag`
    
    ![dvc dag](docs/img/dvc_dag.png)

- Deployment
    - Steps
        1. Build docker image
        2. Push the docker image to ECR
        3. Launch EC2
        4. Pull the image from ECR into EC2
        5. Launch docker image in EC2
    - Policy
        - `AmazonEC2ContainerRegistryFullAccess`
        - `AmazonEC2FullAccess`
    - Create ECR repo to store/save docker image
        - Save the URI: `566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken`
    - Create EC2 machine (Ubuntu)
    - Open EC2 and Install docker in EC2 Machine        
        ```bash
            # optinal

            sudo apt-get update -y
            sudo apt-get upgrade

            # required

            curl -fsSL https://get.docker.com -o get-docker.sh
            sudo sh get-docker.sh
            sudo usermod -aG docker ubuntu
            newgrp docker
        ```
    - Configure EC2 as self-hosted runner
        - setting `>` actions `>` runner `>` new self hosted runner `>` choose os `>` then run command one by one
    - Setup github secrets
        ```bash
        AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
        AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
        AWS_REGION=us-east-1
        AWS_ECR_LOGIN_URI=demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com
        ECR_REPOSITORY_NAME=simple-app
        ```