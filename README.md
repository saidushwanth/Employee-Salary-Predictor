This project predicts whether an individual earns more than $50K per year based on census data, using a machine learning model trained on the UCI Adult Income Dataset. It includes model training, accuracy optimization using GridSearchCV, and a responsive web app built with Streamlit for real-time predictions.
website link:https://employee-salary-predictor-f7e2ujjgwaklefqcmr2yup.streamlit.app/


🔍 Project Highlights
✅ Data Source: UCI Adult Income Dataset (also known as "Census Income" dataset)

✅ Preprocessing: Label encoding of categorical features, removal of nulls & unneeded columns

✅ Models Tried:

Logistic Regression

K-Nearest Neighbors

Random Forest

Support Vector Machine (SVM)

Gradient Boosting (Best Performing)

✅ Model Optimization: GridSearchCV for hyperparameter tuning

✅ Best Accuracy: ~XX% using Gradient Boosting Classifier (replace with your score)

✅ Deployment: Interactive prediction app using Streamlit

✅ Model Persistence: Final trained model saved as best_model.pkl

🚀 How to Run Locally
Clone the repository:

bash
Copy
Edit
git clone https://github.com/saidushwanth/salary-prediction-app.git
cd salary-prediction-app
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
🧠 Features Used for Prediction
Age

Workclass

Marital Status

Occupation

Relationship

Race

Gender

FNLWGT (Census weighting)

Education Level (numeric)

Capital Gain

Capital Loss

Hours Worked Per Week

Native Country

📁 Files
File/Folder	Description
SALARYPREDICTION.ipynb	Jupyter Notebook with preprocessing, training, and evaluation
best_model.pkl	Saved GradientBoosting model after tuning
app.py	Streamlit-based frontend for prediction
adult 3.csv	Cleaned dataset used for model training
requirements.txt	Python dependencies for this project

📷 Screenshot
(Include a screenshot of your Streamlit UI if you’d like!)

🙋‍♂️ Author
Meesala Sai Dushwanth Kumar
Bachelor's in Computer Science & Technology
IIEST Shibpur | 2026 expected graduation

