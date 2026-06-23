# Saving the model

import joblib

class SaveModel:
    
    def save(self, model):
        
        joblib.dump(model, "linear_regression.pkl")
        
        print("Model Saved Successfully")
    