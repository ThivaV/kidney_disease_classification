from src.kidney_disease_classification import logger
from src.kidney_disease_classification.pipeline.data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f'------- stage {STAGE_NAME} started -------')
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'------- stage {STAGE_NAME} completed -------')
except Exception as e:
    logger.exception(e)
    raise e