import pandas as pd
from src.config.config import RAW_DATA_PATH


###✅ Industry style

class DataIngestion:

    def load_data(self):
        df = pd.read_csv(RAW_DATA_PATH)
        return df
    
# 🚀 if __name__ == "__main__":
# Means:
# Run this code only when this file is executed directly.

# if __name__ == "__main__":

#     ingestion = DataIngestion()

#     df = ingestion.load_data()

#     print(df.head())
    
    
#(good for learning only)

# df=pd.read_csv(RAW_DATA_PATH)
# print(df.head())