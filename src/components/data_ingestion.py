
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os,sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered into data Ingestion")
        try :
            df = pd.read_csv(r"notebook\stud.csv")
            logging.info("Read the data")
            os.makedirs('artifacts',exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path,index = False,header =True)
            train_set,test_set = train_test_split(df,test_size=0.3,random_state=42)
            train_set.to_csv(self.data_ingestion_config.train_data_path,index = False,header =True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index = False,header =True)
            logging.info("Data Ingestion is completed")
            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
                             
            
        except  Exception as e:
            raise CustomException(e,sys) from e