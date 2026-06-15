import streamlit as st
import pandas as pd
import joblib

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Employee Salary Prediction System",
    page_icon="💼",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main-header {
    text-align: center;
    padding: 10px;
}

.salary-card {
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD MODEL
# =====================================================

@st.cache_resource
def load_model():
    return joblib.load(
        "model/best_salary_prediction_model.pkl"
    )

try:
    model = load_model()

except FileNotFoundError:
    st.error(
        "Model file not found. Please train the model first."
    )
    st.stop()

except Exception as e:
    st.error(
        f"Error loading model: {e}"
    )
    st.stop()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("💼 Employee Salary Prediction")

st.sidebar.markdown("---")

st.sidebar.subheader("Models Used")

st.sidebar.write("""
• Linear Regression

• Decision Tree Regressor

• Random Forest Regressor
""")

st.sidebar.markdown("---")

st.sidebar.subheader("Best Model")

st.sidebar.success("Linear Regression")

st.sidebar.metric(
    "R² Score",
    "0.9848"
)

st.sidebar.metric(
    "MAE",
    "₹25,662"
)

st.sidebar.markdown("---")

st.sidebar.subheader("Key Salary Factors")

st.sidebar.write("""
1. Years of Experience

2. Skill Score

3. Education Level

4. Certifications

5. Company Type
""")

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class='main-header'>
<h1>💼 Employee Salary Prediction System</h1>
<p>Predict employee salaries using Machine Learning</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =====================================================
# MODEL PERFORMANCE
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Best Model",
        "Linear Regression"
    )

with col2:
    st.metric(
        "R² Score",
        "0.9848"
    )

with col3:
    st.metric(
        "MAE",
        "₹25,662"
    )

st.markdown("---")

# =====================================================
# INPUT SECTION
# =====================================================

col1, col2 = st.columns(2)

# =====================================================
# EMPLOYEE INFORMATION
# =====================================================

with col1:

    st.subheader("👤 Employee Information")

    age = st.slider(
        "Age",
        min_value=21,
        max_value=60,
        value=25
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    education = st.selectbox(
        "Education Level",
        [
            "Bachelor's",
            "Master's",
            "PhD"
        ]
    )

# =====================================================
# PROFESSIONAL INFORMATION
# =====================================================

with col2:

    st.subheader("🏢 Professional Information")

    years_of_experience = st.slider(
        "Years of Experience",
        min_value=0,
        max_value=40,
        value=2
    )

    skill_score = st.slider(
        "Skill Score",
        min_value=1,
        max_value=10,
        value=5
    )

    certifications = st.number_input(
        "Number of Certifications",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )

    work_hours = st.slider(
        "Work Hours Per Week",
        min_value=20,
        max_value=60,
        value=40
    )

    job_role = st.selectbox(
        "Job Role",
        [
            "Data Analyst",
            "Developer",
            "Designer",
            "Manager",
            "Quality Compliance Tester"
        ]
    )

    company_type = st.selectbox(
        "Company Type",
        [
            "MNC",
            "Medium",
            "Startup"
        ]
    )

st.markdown("---")

# =====================================================
# PREDICT BUTTON
# =====================================================

if st.button(
    "🚀 Predict Salary",
    use_container_width=True
):

    # =================================================
    # VALIDATION
    # =================================================

    errors = []

    if years_of_experience > age:
        errors.append(
            "Years of experience cannot exceed age."
        )

    if age - years_of_experience < 16:
        errors.append(
            "Age and experience combination appears unrealistic."
        )

    if errors:

        for error in errors:
            st.error(error)

        st.stop()

    # =================================================
    # ENCODING
    # =================================================

    input_data = {

        "Age": age,
        "YearsOfExperience": years_of_experience,
        "SkillScore": skill_score,
        "Certifications": certifications,
        "WorkHoursPerWeek": work_hours,

        "Gender_Male": 0,

        "EducationLevel_Master's": 0,
        "EducationLevel_PhD": 0,

        "JobRole_Designer": 0,
        "JobRole_Developer": 0,
        "JobRole_Manager": 0,
        "JobRole_Quality Compliance Tester": 0,

        "CompanyType_Medium": 0,
        "CompanyType_Startup": 0
    }

    # Gender

    if gender == "Male":
        input_data["Gender_Male"] = 1

    # Education

    if education == "Master's":
        input_data["EducationLevel_Master's"] = 1

    elif education == "PhD":
        input_data["EducationLevel_PhD"] = 1

    # Job Role

    if job_role == "Designer":
        input_data["JobRole_Designer"] = 1

    elif job_role == "Developer":
        input_data["JobRole_Developer"] = 1

    elif job_role == "Manager":
        input_data["JobRole_Manager"] = 1

    elif job_role == "Quality Compliance Tester":
        input_data[
            "JobRole_Quality Compliance Tester"
        ] = 1

    # Company Type

    if company_type == "Medium":
        input_data["CompanyType_Medium"] = 1

    elif company_type == "Startup":
        input_data["CompanyType_Startup"] = 1

    # =================================================
    # PREDICTION
    # =================================================

    try:

        input_df = pd.DataFrame([input_data])

        prediction = model.predict(input_df)

        predicted_salary = prediction[0]

        st.success(
            "Salary prediction generated successfully."
        )

        st.metric(
            "💰 Predicted Annual Salary",
            f"₹ {predicted_salary:,.0f}"
        )

        # =============================================
        # SALARY CATEGORY
        # =============================================

        if predicted_salary < 300000:

            st.warning(
                "📈 Salary Category: Entry Level"
            )

        elif predicted_salary < 700000:

            st.info(
                "📊 Salary Category: Mid Level"
            )

        else:

            st.success(
                "🏆 Salary Category: Senior Level"
            )

        # =============================================
        # INSIGHTS
        # =============================================

        st.subheader("📋 Prediction Insights")

        st.write(
            f"""
            Based on:

            • Age: {age}

            • Experience: {years_of_experience} years

            • Skill Score: {skill_score}/10

            • Certifications: {certifications}

            • Education: {education}

            • Job Role: {job_role}

            • Company Type: {company_type}

            The model estimates an annual salary of
            **₹ {predicted_salary:,.0f}**.
            """
        )

        # =============================================
        # ENCODED DATA VIEW
        # =============================================

        with st.expander(
            "🔍 View Encoded Input Data"
        ):
            st.dataframe(input_df)

    except Exception as e:

        st.error(
            f"Prediction failed: {e}"
        )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "Built using Python, Pandas, Scikit-Learn and Streamlit"
)