This repository contains 3 files in total

**1. heart_stroke_dataset.csv**

This is the original heart-stroke dataset selected from Kaggle.

**Dataset description:** 

Total number of attributes:12  

Total number of records: 43,400 patient records. 

**Column Description:** 

The dataset includes attributes - gender, age, marital status, work and residence, hypertension, heart disease, average glucose level measured, Body Mass Index (BMI), smoking status and experience of stroke.  

In this dataset, the target variable(stroke) is coded as 1 for positive (having stroke) and 0 for negative (not having stroke). 

The dataset consists of both categorical and continuous variables. 
 
Categorical: gender, marital status, work and residence, hypertension, heart disease, smoking status, stroke. 

Continuous: age, average glucose level, BMI. 

 

**2. ltaduru_final_project.py**

This is a python file which contains the code for cleaning the original data and transforming it used in the pipeline. It exports the transformed data into a csv file.
Along with data transformation, this generates a count plot for the data attributes and export it into image with JPG format

**3. BigQuery_Data_Visualization.ipynb**

This is a python notebook file from google colaboratory where the data from Big Query is further used to make visualization plots 
