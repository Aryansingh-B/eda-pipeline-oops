from sklearn.datasets import fetch_california_housing
import pandas as pd

class ReadData:
    
    def get_data(self):
        housing = fetch_california_housing(as_frame==True)
        
        df = housing.frame
        
        print("Dataset Loaded Successfully")
        print(df.head()) 
        
        return df