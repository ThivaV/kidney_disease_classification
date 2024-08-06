from src.kidney_disease_classification import logger
from src.kidney_disease_classification.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.kidney_disease_classification.pipeline.prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'Data ingestion stage'

try:
    logger.info(f'------- stage {STAGE_NAME} started -------')
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'------- stage {STAGE_NAME} completed -------')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Prepare base model'

try:
    logger.info(f'------------ stage {STAGE_NAME} started ------------------')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'------------ stage {STAGE_NAME} completed ----------------')
except Exception as e:
    logger.exception(e)
    raise e