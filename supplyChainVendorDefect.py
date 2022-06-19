#Step 1 - Import the required modules
import pandas as pd
from sklearn.tree import DecisionTreeRegressor # Import Decision Tree Algorithm
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR #import for support vector regressor


#Step 2 - Read the data source
# Load the training data into Pandas DataFrame
SourceData=pd.read_csv("Supplier_Past_Performance.csv")
# Load the test data
Testdata=pd.read_csv("Defect_Predict.csv")


#Step 3  - Declare the independent and dependent train data from the sample
# Drop depedent variable from training dataset
SourceData_train_independent= SourceData.drop(["Defect Percentage(in %)"], axis=1)
# New dataframe with only independent variable value for training dataset
SourceData_train_dependent=SourceData["Defect Percentage(in %)"].copy()


#Step 4  - Scale the independent test and train data
sc_X = StandardScaler()
# scale the independent training dataset variables
X_train=sc_X.fit_transform(SourceData_train_independent.values)
# scale the independent test dataset
X_test=sc_X.transform(Testdata.values)
# scaling is not required for dependent variable
y_train=SourceData_train_dependent


#Step 5  - Fit the test data in maching learning model - Support Vector Regressor
#Now we will feed the independent and dependent train data i.e. X_train and y_train respectively to train the Support Vector Machine model
svm_reg = SVR(kernel="linear", C=1)
# fit and train the model
svm_reg.fit(X_train, y_train) 
predictions = svm_reg.predict(X_test)
print("Defect percent prediction by Support Vector model for the order value of 95827 GBP with 851 pallets sent 55 days before delivery data is " ,round(predictions[0],2) , "%")


#Step 6 - Fit the test data in maching learning model - Decision Tree Model
#In the same way,we will feed the training dataset (independent and dependent variable value) to the Decision Tree model
tree_reg = DecisionTreeRegressor()
# fit and train the model
tree_reg.fit(X_train, y_train) 
# Predict the value of dependent variable
decision_predictions = tree_reg.predict(X_test) 
print("Defect percent prediction by Decision Tree model for the order value of 95827 GBP with 851 pallets sent 55 days before delivery data is " ,round(decision_predictions[0],2) , "%")
