import streamlit as st
import pickle
import numpy as np
import pandas as pd

# =======================================================
# 1. CUSTOM UI STYLING & THEMING (IIUM BRONZE/ORANGE ACCENT)
# =======================================================
st.set_page_config(
    page_title="Chicken Tenders | IS Project Portal", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS injection to upscale the sidebar font size and integrate thematic colors
st.markdown("""
    <style>
        /* Increase sidebar radio navigation selection text readability */
        div[data-testid="stSidebarNav"] {font-size: 1.3rem !important;}
        .stRadio div role {font-size: 1.4rem !important; font-weight: bold;}
        div[class*="stRadio"] p {font-size: 1.25rem !important; font-weight: 600 !important;}
        
        /* Main Title Color Styling */
        h1 { color: #E67E22 !important; } /* Clean Primary Orange header style */
        h2, h3 { color: #2C3E50 !important; }
        
        /* Metric block styling custom improvements */
        div[data-testid="stMetricValue"] { font-size: 2.5rem !important; font-weight: 700 !important; color: #16A085 !important; }
        
        /* Stylized Action Button styling */
        div.stButton > button:first-child {
            background-color: #E67E22 !important;
            color: white !important;
            font-size: 1.2rem !important;
            font-weight: bold !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 0.6rem 2rem !important;
            transition: all 0.3s ease;
        }
        div.stButton > button:first-child:hover {
            background-color: #D35400 !important; /* Darker orange on hover state */
            transform: scale(1.02);
        }
    </style>
""", unsafe_allow_html=True)

# Load the saved Random Forest model
try:
    with open('student_rf_model.sav', 'rb') as f:
        loaded_rf_model = pickle.load(f)
except FileNotFoundError:
    st.error("Error: 'student_rf_model.sav' not found. Please place it in the same directory as app.py.")

# Load the underlying dataset to verify real-world data references
try:
    data_df = pd.read_csv('Gaming_Academic_Performance.csv')
    dataset_loaded = True
except FileNotFoundError:
    dataset_loaded = False

# =======================================================
# 2. EXPANDED SIDEBAR NAVIGATION MENU (TEAM CHICKEN TENDERS)
# =======================================================
with st.sidebar:
    # High-visibility header box with explicit pure white overrides to prevent the silhouette effect
    st.markdown("""
        <div style="background-color: #E67E22; padding: 1.2rem; border-radius: 8px; text-align: center; margin-bottom: 1rem; box-shadow: 0px 4px 6px rgba(0,0,0,0.15);">
            <h2 style="color: #FFFFFF !important; font-family: 'Source Sans Pro', sans-serif; margin: 0; font-size: 1.65rem; font-weight: 800; text-shadow: 1px 1px 3px rgba(0,0,0,0.4); line-height: 1.2;">Intelligent System</h2>
            <p style="color: #FFFFFF !important; margin: 6px 0 0 0; font-weight: 600; font-size: 0.95rem; letter-spacing: 0.5px; opacity: 0.95; text-shadow: 1px 1px 1px rgba(0,0,0,0.2);">CHICKEN TENDERS</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🗺️ **SYSTEM MENU**")
    page = st.radio(
        label="Select Workspace Area:", 
        options=["📊 Dashboard & Analysis", "🔮 Predict Student Grade", "👥 Team Members"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.info("**BICS 2303 — Section 05**\n\nInstructor:\n**Dr. Marini Binti Othman**")

# ==========================================
# PAGE 1: DASHBOARD & ANALYSIS
# ==========================================
if "Dashboard" in page:
    st.title("🎓 Predictive Analysis of Gaming Habits on Academic Performance")
    st.subheader("Model Performance Summary Metrics")
    
    # Display clear evaluation summaries matching your console prints
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Proposed Random Forest R² Score", value="91.21%", delta="+4.15% vs Baseline")
    with col2:
        st.metric(label="Proposed Random Forest RMSE", value="6.6385", delta="-1.4137 (Lower Error)")
    with col3:
        st.metric(label="Baseline Decision Tree R² Score", value="87.06%")

    st.markdown("---")
    st.markdown("### 🎯 Structural Analytics Table")
    
    metrics_df = pd.DataFrame({
        'Evaluation Metric': ['Mean Squared Error (MSE)', 'Root Mean Squared Error (RMSE)', 'R-squared (R2) Score'],
        'Model 1: Single Decision Tree': [64.8381, 8.0522, 0.8706],
        'Model 2: Random Forest Ensemble': [44.0693, 6.6385, 0.9121]
    })
    st.table(metrics_df)

    st.markdown("---")
    st.markdown("### 📂 Grounded Dataset Auditing (`Gaming_Academic_Performance.csv`)")
    if dataset_loaded:
        st.write(f"✅ Successfully linked to data stream source. Total tracked records: **{data_df.shape[0]} students**.")
        # Interactive slider to inspect rows live
        row_inspect = st.slider("Select number of dataset records to view live:", min_value=5, max_value=50, value=5)
        st.dataframe(data_df.head(row_inspect))
    else:
        st.warning("⚠️ 'Gaming_Academic_Performance.csv' not detected in working directory. Showing historical metrics only.")

# ==========================================
# PAGE 2: INTERACTIVE GRADE PREDICTOR
# ==========================================
elif "Predict" in page:
    st.title("🔮 Interactive Student Grade Prediction Portal")
    st.write("Input custom student behaviors below to feed into the underlying 18-feature Random Forest pipeline.")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### **📝 Academic Metrics**")
        study_hours = st.number_input("Daily Study Hours (1.0 - 10.0):", min_value=1.0, max_value=10.0, value=5.5, step=0.5)
        attendance = st.number_input("Class Attendance % (60.0 - 100.0):", min_value=60.0, max_value=100.0, value=82.0, step=1.0)
        age = st.slider("Biological Age of Student:", min_value=16, max_value=24, value=20)
        
    with col2:
        st.markdown("#### **🎮 Gaming Habits**")
        gaming_hours = st.number_input("Daily Gaming Hours (0.0 - 8.0):", min_value=0.0, max_value=8.0, value=3.0, step=0.5)
        device_usage = st.number_input("Total Screen Time (Hours):", min_value=1.1, max_value=14.0, value=7.0, step=0.5)
        
        gender = st.selectbox("Gender Orientation:", ["Male", "Female"])
        gender_male = 1 if gender == "Male" else 0

    with col3:
        st.markdown("#### **🧠 Cognitive Indexes**")
        sleep_hours = st.number_input("Nightly Sleep Hours (4.0 - 9.0):", min_value=4.0, max_value=9.0, value=6.5, step=0.5)
        addiction_score = st.number_input("Gaming Addiction Score:", min_value=-5.0, max_value=25.0, value=10.0, step=1.0)
        reaction_time_ms = st.number_input("Stimulus Reflex Latency (ms):", min_value=150.0, max_value=350.0, value=265.0, step=5.0)

    # Defaulting One-Hot encoding structures to standard reference boundaries
    dummy_genre_casual = 0
    dummy_genre_fps = 1
    dummy_genre_rpg = 0
    dummy_genre_sports = 0
    dummy_genre_strategy = 0
    
    dummy_stress_low = 1
    dummy_stress_medium = 0
    dummy_stress_high = 0

    st.markdown("---")
    if st.button("Generate System Grade Prediction"):
        features = [
            age, gaming_hours, study_hours, sleep_hours, attendance, 
            device_usage, reaction_time_ms, addiction_score, gender_male, 
            dummy_genre_casual, dummy_genre_fps, dummy_genre_rpg, 
            dummy_genre_sports, dummy_genre_strategy, dummy_stress_low, 
            dummy_stress_medium, dummy_stress_high, 0
        ]
        
        prediction = loaded_rf_model.predict([features])[0]
        final_calculated_grade = round(prediction, 2)
        
        st.markdown(f"""
            <div style="background-color: #FDF2E9; border-left: 6px solid #E67E22; padding: 1.5rem; border-radius: 6px; margin-top: 1rem;">
                <h3 style="margin: 0; color: #D35400;">🔮 Random Forest Estimation Result</h3>
                <p style="font-size: 1.5rem; margin: 0.5rem 0 0 0; font-weight: bold; color: #2C3E50;">
                    Predicted Final Grade Mark: <span style="color: #E67E22;">{final_calculated_grade} / 100</span>
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        if final_calculated_grade >= 80:
            st.success("🎉 Student Profile matches high academic achievement thresholds.")
        elif final_calculated_grade >= 50:
            st.info("📋 Student Profile maintains a stable passing average baseline.")
        else:
            st.error("⚠️ Warning: Student metrics flag academic performance risk boundaries.")

# ==========================================
# PAGE 3: TEAM MEMBERS (CHICKEN TENDERS)
# ==========================================
elif "Team" in page:
    st.title("👥 Project Development Team")
    st.markdown("### **Group Name: Chicken Tenders**")
    st.write("Project group members for BICS 2303 — Section 05:")
    
    st.markdown("---")
    
    # Clean two-column layout presenting names and project context layout
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🍗 **Group Members List:**
        * **Muhammad Amir Haziq bin Khairulnizam** (Matric No: 2413641)
        * **Muhammad Aiman bin Mohamad Salehudin** (Matric No: 2412635)
        * **Adib Danial Bin Mohamad Jani** (Matric No: 2412129)
        * **Farhan Adib Bin Zamri** (Matric No: 2417295)
        * **Muhammad Adib Fikri bin Haidzir** (Matric No: 2310005)
        """)
        
    with col2:
        st.markdown("""
        <div style="background-color: #F8F9F9; border-radius: 8px; padding: 1.5rem; border-top: 4px solid #E67E22; margin-top: 1.5rem;">
            <h4 style="color: #E67E22; margin-top: 0;">ICT Intelligent Systems Portal</h4>
            <p style="color: #7F8C8D; font-size: 0.95rem; line-height: 1.5; margin: 0;">
                This workspace has been dynamically developed by Team <b>Chicken Tenders</b> to satisfy the partial completion 
                criteria for the Intelligent Systems core project parameters under the guidance of <b>Dr. Marini Binti Othman</b>.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    st.success("✨ All members contributed equally to the research, analysis, and execution of this machine learning system framework.")