from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
if __name__ =="__main__":
    # Creating an instance of the DataIngestion class
    data_ingestion = DataIngestion()
    # Calling the method to ingest data from the CSV file
    train_path,test_path = data_ingestion.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr ,pickel_file= data_transformation.initiate_data_transformation(train_path,test_path)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))