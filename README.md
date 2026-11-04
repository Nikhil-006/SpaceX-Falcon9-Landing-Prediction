# 🚀 SpaceX Falcon 9 First Stage Landing Prediction

## IBM Data Science Professional Certificate – Capstone Project

### Project Overview

This project analyzes historical SpaceX Falcon 9 launch data to predict whether the first-stage booster will land successfully.

The project uses Python, SQL, data visualization, and machine learning to identify patterns that influence landing success.

## 🎯 Objectives

* Analyze historical SpaceX Falcon 9 launch data.
* Explore landing success patterns.
* Perform data cleaning and exploratory data analysis.
* Analyze launch data using SQL.
* Build an interactive launch-site map.
* Develop an interactive dashboard.
* Train machine learning models to predict landing outcomes.

## 🛠️ Technologies Used

* Python
* Pandas and NumPy
* Matplotlib and Seaborn
* SQL and SQLite
* Plotly and Dash
* Folium
* Scikit-learn
* Jupyter Notebook
* GitHub

## 📊 Dataset

The project uses the SpaceX Falcon 9 dataset provided through IBM Skills Network learning materials.

* Total launch records: 90
* Total features: 19
* Successful landings: 60
* Unsuccessful landings: 30
* Overall landing success rate: 66.67%

## 🔍 Project Workflow

1. Data Collection
2. Data Loading and Preprocessing
3. Exploratory Data Analysis
4. SQL Analysis
5. Interactive Map Development
6. Interactive Dashboard Development
7. Machine Learning Model Development
8. Model Evaluation

## 🤖 Machine Learning Models

Three machine learning algorithms were implemented:

| Model                        | Test Accuracy |
| ---------------------------- | ------------: |
| Logistic Regression          |        77.78% |
| Decision Tree                |        94.44% |
| Support Vector Machine (SVM) |        77.78% |

### Best Model

Decision Tree Classifier

* Test Accuracy: 94.44%
* 5-Fold Cross-Validation Accuracy: 84.44%

The Decision Tree achieved the highest test accuracy and cross-validation average among the three models.

## 🗺️ Interactive Visualizations

The project includes:

* Exploratory data analysis graphs.
* Interactive Folium launch-site map.
* Plotly Dash dashboard.
* Machine learning evaluation charts.

## 📁 Project Files

* `01_SpaceX_API_Data_Collection.ipynb` – Data collection notebook
* `02_Load_SpaceX_Dataset.ipynb` – Dataset loading and preprocessing
* `03_EDA_Visualization.ipynb` – Exploratory data analysis
* `04_EDA_SQL.ipynb` – SQL analysis
* `05_Folium_Interactive_Map.ipynb` – Interactive map
* `06_Machine_Learning_Prediction.ipynb` – Model development
* `07_Test_SpaceX_Model.ipynb` – Model testing
* `app.py` – Interactive dashboard application
* `spacex_landing_model.pkl` – Trained machine learning model
* `spacex_launch_map.html` – Interactive launch-site map
* `SpaceX_Falcon9_Final_Report.docx` – Final project report
* `SpaceX_Falcon9_Project_Presentation.pptx` – Project presentation

## 📌 Conclusion

The project demonstrates how data science and machine learning can be applied to analyze and predict Falcon 9 first-stage landing outcomes.

The Decision Tree model achieved 94.44% accuracy on the held-out test dataset. Further improvements can be explored using larger datasets and additional features.

This project is an educational prototype and is not intended for real-world launch decisions.

## 👨‍💻 Author

**Nikhil Agrawal**

B.Tech – Computer Science and Engineering

Bharati Vidyapeeth College of Engineering, Pune

## 📜 Acknowledgement

IBM Data Science Professional Certificate – Capstone Project.
