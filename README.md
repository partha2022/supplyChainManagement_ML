## **supplyChainManagement_ML**

**Author:** Parthasarathi Swain


### Project Overview

- **Background:** The business would like to predict the defective piece percentage in delivery from the supplier. If the defective piece percentage predicted is below the threshold level, then a quality check will not be performed. Let us consider that if the defect piece percentage in the delivery is more than 0.4%, then explicit incoming inspection is needed to ensure the quality of the end product.  



- **Problem Statement:** The business would like to predict the defective piece percentage in delivery from the supplier for more business outcomes. The goal is to help to focus on quality check on only particular purchase orders delivery, to control the end-product quality, and optimize inspection costs.



- **Solution Statement:** A combined "classification-then-regression" machine learning algorithm where the classification algorithm predicts whether a particular product will be delayed or not and then the regression algorithm will predict the length of delay on the subset of the data which the classification predicts will be delayed. This mimicks a streamlined, prioritized decision process of a supply chain manager. This will help to focus on quality check on only particular purchase orders delivery, to control the end-product quality, and optimize inspection costs. It will also enable to uncover the variables/parameters which are influencing the defective deliveries of few materials at times and work collaboratively with the supplier to address it



- **Benchmark Model:** Default SciKit-Learn RandomForestClassifier and RandomForestRegressor will be used as benchmarks/baseline. Several models will then be explored to improve over the benchmark including other ensemble and tree-based models, Support-Vector Machines (SVM), XGBoost.  



- **Evaluation Metrics:** Recall and F1-score will be used for classification while R-squared and RMSE will be used for the regression part of the combined model  



### Requirements: software and libraries used
- I was running python 3.6.1 on a 64-bit windows system
- The rest of the libraries can be installed using either anaconda or pip distributions


#### Install/Download the following libraries and apis 
1. python 3.6.1 
2. certifi==2021.5.30
3. pandas
4. numpy
5. matplotlib
6. seaborn
7. time
8. datetime
9. pandas_profiling
12. os
13. sklearn
14. yellowbrick
15. imblearn
16. googlemaps


