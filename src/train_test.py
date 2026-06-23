# Train-test split

from sklearn.model_selection import train_test_split

class DataSplit:
    
    def split_data(self, X, y):
        
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
            
        )
        
        return X_train, X_test, y_train, y_test