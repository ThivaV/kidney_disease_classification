from src.kidney_disease_classification import logger
from src.kidney_disease_classification.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.kidney_disease_classification.pipeline.prepare_base_model import PrepareBaseModelTrainingPipeline
from src.kidney_disease_classification.pipeline.model_training import ModelTrainingPipeline
from src.kidney_disease_classification.pipeline.model_evaluation import EvaluationPipeline

STAGE_NAME = 'data ingestion'

try:
    logger.info(f'\n\n------- stage {STAGE_NAME} started -------')
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'------- stage {STAGE_NAME} completed -------')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'prepare base model'

try:
    logger.info(f'\n\n------------ stage {STAGE_NAME} started ------------------')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'------------ stage {STAGE_NAME} completed ----------------')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'training'

try:
    logger.info(f'\n\n------------ stage {STAGE_NAME} started ------------------')
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f'------------ stage {STAGE_NAME} completed ----------------')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'evaluation'

try:
    logger.info(f'\n\n------------ stage {STAGE_NAME} started ------------------')
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f'------------ stage {STAGE_NAME} completed ----------------')
except Exception as e:
    logger.exception(e)
    raise e