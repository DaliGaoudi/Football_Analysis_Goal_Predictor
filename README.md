# Project details

This project is about creating an AI using ML that tries to predict whether a shot on goal will be a successfull goal or not.
The Model was trained on a dataset of shot events fetched from the https://github.com/statsbomb/open-data database. 
The model accepts as input the position where the ball was shot from, the angle the ball is taking towards the goal, the goalkeeper's position and the average of the opposing defenders' positions in respect of the ball and the shooter.

An EDA (Exploratory Data Analysis) has been done on the dataset to find out the relationships between the different variables and their impact on the prediction of the target variable ("goal").
A very big imbalance was found in the data which was fixed by SMOTE after comparing different sampling techniques to find out which one yields more accuracy.
Two models were used to be trained on the data: RandomForest and Light-Gradient-Boosting-Machine
