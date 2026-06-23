# Remove multicollinearity using VIF

import pandas as  pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

class VIFCalculation:
    def calculate_vif(self, df):
         
         X = df.drop("MedHouseVal", axis=1)
         vif_data = pd.DataFrame()
         vif_data["Feature"] = X.columns
         
         vif_data["VIF"] = [
             variance_inflation_factor(X.values, i)
             for i in range(X.shape[1])
         ]
         
         print(vif_data)
         
         return vif_data