import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("best_model.pkl")

# Custom page config
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💼",
    layout="wide"
)

# --- Header section ---
st.markdown("""
    <style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #00FFF5;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-header {
        text-align: center;
        color: #EEEEEE;
        font-size: 18px;
        margin-top: -10px;
        margin-bottom: 30px;
    }
    .stButton>button {
        border-radius: 10px;
        background-color: #00ADB5;
        color: white;
        border: none;
        height: 50px;
        font-size: 18px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💼 AI-powered Employee Salary Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">🔍 Enter employee attributes and predict if the salary is over $50K!</div>', unsafe_allow_html=True)
st.markdown("---")

# --- Mapping dictionaries ---
workclass_map = {'Private': 0, 'Self-emp-not-inc': 1, 'Self-emp-inc': 2, 'Federal-gov': 3, 'Local-gov': 4, 'State-gov': 5, 'Without-pay': 6}
marital_status_map = {'Never-married': 0, 'Married-civ-spouse': 1, 'Divorced': 2, 'Separated': 3, 'Widowed': 4, 'Married-spouse-absent': 5}
occupation_map = {'Tech-support': 0, 'Craft-repair': 1, 'Other-service': 2, 'Sales': 3, 'Exec-managerial': 4, 'Prof-specialty': 5, 'Handlers-cleaners': 6, 'Machine-op-inspct': 7, 'Adm-clerical': 8}
relationship_map = {'Wife': 0, 'Own-child': 1, 'Husband': 2, 'Not-in-family': 3, 'Other-relative': 4, 'Unmarried': 5}
race_map = {'White': 0, 'Black': 1, 'Asian-Pac-Islander': 2, 'Amer-Indian-Eskimo': 3, 'Other': 4}
gender_map = {'Male': 0, 'Female': 1}
native_country_map = {'United-States': 0, 'India': 1, 'Mexico': 2, 'Philippines': 3, 'Germany': 4, 'Other': 5}

# --- Input Form Layout ---
with st.container():
    st.markdown("## 🧾 Basic Information")
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("🎂 Age", 17, 90, 30)
        fnlwgt = st.number_input("📦 FNLWGT", 10000, 1000000, 300000)
        educational_num = st.slider("🎓 Educational Number", 1, 16, 10)
        workclass = st.selectbox("🏢 Workclass", list(workclass_map.keys()))
        marital_status = st.selectbox("💍 Marital Status", list(marital_status_map.keys()))
    with col2:
        occupation = st.selectbox("🧑‍💼 Occupation", list(occupation_map.keys()))
        relationship = st.selectbox("👨‍👩‍👧 Relationship", list(relationship_map.keys()))
        race = st.selectbox("🌎 Race", list(race_map.keys()))
        gender = st.selectbox("⚧ Gender", list(gender_map.keys()))
        native_country = st.selectbox("🗺️ Native Country", list(native_country_map.keys()))

st.markdown("---")

with st.container():
    st.markdown("## ⏰ Income & Work Details")
    col3, col4 = st.columns(2)
    with col3:
        capital_gain = st.number_input("📈 Capital Gain", 0, 99999, 0)
        capital_loss = st.number_input("📉 Capital Loss", 0, 5000, 0)
    with col4:
        hours_per_week = st.slider("🕒 Hours per Week", 1, 99, 40)

# --- Prediction ---
if st.button("🚀 Predict Salary"):
    input_data = pd.DataFrame([{
        'age': age,
        'fnlwgt': fnlwgt,
        'educational-num': educational_num,
        'workclass': workclass_map[workclass],
        'marital-status': marital_status_map[marital_status],
        'occupation': occupation_map[occupation],
        'relationship': relationship_map[relationship],
        'race': race_map[race],
        'gender': gender_map[gender],
        'capital-gain': capital_gain,
        'capital-loss': capital_loss,
        'hours-per-week': hours_per_week,
        'native-country': native_country_map[native_country]
    }])
    
    prediction = model.predict(input_data)[0]
    label = ">50K" if prediction == 1 else "<=50K"
    st.success(f"🎯 **Predicted Salary Category: `{label}`**")
