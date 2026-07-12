from src.data.ingestion import DataIngestion

ingestion=DataIngestion()
df=ingestion.load_data()
print(df.head())