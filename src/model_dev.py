# Develop Linear Regression model

from sklearn.linear_model import LinearRegression

class ModelDevelopment:
    
    def train_model(self, X_train, y_train):
        
        model = LinearRegression()
        
        model.fit(X_train, y_train)
        
        print("Model Training Completed")
        
        return model