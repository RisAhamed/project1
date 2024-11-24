from src.components.data_ingestion import DataIngestion


if __name__ =="__main__":
    # Creating an instance of the DataIngestion class
    data_ingestion = DataIngestion()
    # Calling the method to ingest data from the CSV file
    data_ingestion.initiate_data_ingestion()

