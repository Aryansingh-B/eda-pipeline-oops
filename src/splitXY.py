# Separate features and target

class SplitXY:
    
    def split(self, df):
        
        X = df.drop("MedHouseVal", axis=1)
        
        y = df["MedHouseVal"]
        
        return X,y