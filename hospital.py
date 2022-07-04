from st_aggrid import AgGrid
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle

st.set_page_config(layout="wide")

# Functions for each of the pages
def Home():
    st.title('Hospitals In Kenya Web App')
    st.markdown("""
        Hospitals in Kenya web app is an application containing all health facilities in Kenya. 
        Each health facility is identified by a code followed by details describing the geographical location, facility type, ownership, and availability of the facility.
        """)
    st.markdown("""
        The aim of this app is to predict the best hospital to visit in an area using machine learning. There is a definite huge demand for the best Medicare for patients. The challenge most patients face in Kenya is how to choose the best hospital to visit among various hospitals in an area. 
        
        The KNN supervised machine learning approach is used to predict the best hospital for the patient according to the services they require on the basis of various attributes used in the dataset. 
        
        The research is based on healthcare facilities in Kenya. The healthcare facilities are classified into five categories representing KEPH levels. KEPH is an acronym for, Kenya Essential Package for Health (KEPH). The KEPH introduced six cohort levels of health service provision, with Level 1 being the Community Facilities, Level 2 being the Health Dispensaries, Level 3 being the Health Centers, Level 4 being the County Hospitals, Level 5 being the County Referral Hospitals and Level 6 being the National Referral Hospitals. For this app, we will only use five levels which include: Level 2, Level 3, Level 4, Level 5 and Level 6. The dataset contains all types of hospitals approved by the Ministry of Health in Kenya. 
        
        The reason as to why the healthcare facilities are classified into KEPH levels is because they represent the six different levels of health care service delivery in Kenya. 
    """)
    st.subheader('The six levels of health care service delivery in Kenya')
    image = Image.open('The-six-levels-of-health-care-service-delivery-in-Kenya.jpg')
    st.image(image, caption='Keph_levels in a nutshell')
    st.markdown("""
    Below are the services a patient should expect to receive from each level:
    
    LEVEL 1 – Community Facilities
    
    They are run by certified medical clinical officers.
    
    Some of the services:
    
    •	Treatment of minor ailments like diarrhoea
    
    •	Tuberculosis (TB) screening, home visits, contact tracing of TB patients and tracing of TB defaulters
    
    •	Screening of malnutrition
    
    •	Malaria rapid test
    
    •	Blood pressure and blood sugar testing
    
    •	HIV testing
    
    •	Health talks with pregnant women and observations of signs of danger
    
    •	Issuance of referral letters to other facilities
    
    """)
    st.markdown("""
    LEVEL 2 – Health Dispensaries
    
    These facilities are run by clinical officers:
    The dispensaries in the cities act like a health center (see level 3), with the difference that the dispensary does not have in-patient facilities.
    
    These are some of the services you will expect in a dispensary:
    
    •	Outpatient services
    
    •	VCT services
    
    •	Tuberculosis services
    
    •	Laboratory Services
    
    •	Well baby Clinics
    
    •	Antenatal and Postnatal services
    
    •	Pharmacy
    
    •	Counselling services
    
    •	Curative treatment
    
    •	They issue referral letters to other facilities
    """)
    st.markdown("""
    LEVEL 3 – Health Centers
    
    These are small hospitals with minimal facilities, yet they offer services like the big hospitals. They are run by at least one doctor, clinical officers and nurses.
    
    These are some of the services they offer:
    
    •	Maternity in-patient services with a ward
    
    •	Curative services
    
    •	Laboratory services
    
    •	Dental
    
    •	Counselling
    
    •	Pharmacy
    
    •	TB Clinics
    
    •	Diabetes & hypertension clinics
    
    •	Comprehensive care clinics for patients living with HIV
    
    •	Baby well clinics
    
    •	Antenatal and postnatal services
    
    •	They issue referral letters to other facilities
    """)
    st.markdown("""
    LEVEL 4 – County Hospitals
    
    These are hospitals that offer holistic services and are ran by a director who is a medic and at best a doctor by profession
    In many counties there’s just one hospital but in larger cities like Nairobi there are two
    
    They have in principle the same services as the Level 3 hospitals, plus X-Ray services They issue referral letters to other facilities

    LEVEL 5 – County Referral Hospitals
    These are the county referral hospitals formerly the provincial hospitals. They are run by Chief Executive Officers who are medic by profession and have over 100 beds capacity for their in-patient. They are also do research about health. In Nairobi Mama Lucy Hospital and Mbagathi Hospital both double up as county referral hospitals and Level 4 hospitals.

    Services include what other hospitals offer, plus
    
    •	Ultrasound
    
    •	CT-Scan
    
    •	Surgery
    
    •	Pharmacy
    
    •	Physiotherapy
    
    •	Orthopaedics
    
    •	Occupational Therapy
    
    •	They issue referral letters to other facilities

    LEVEL 6 – National Referral Hospitals
    
    In Kenya there are three Teaching and Research referral hospitals: Mathare Hospital, Kenyatta National Hospital, Moi Teaching and Referral Hospital and the National Spinal Injury Referral Hospital. Their range of services is the same as of on Level 5, but they offer specialised treatments to patients and are not only accessed by Kenyans but do serve East Africa and Central Africa.
    """)
    st.header('Hospitals Dataset')
    st.markdown("""Data source: OpenData portal""")

    Data = pd.read_csv("Kenya-hospitals.csv")
    print(Data.head())
    st.write(Data)

def Advanced_Search():
    st.title("Advanced Search")
    st.markdown("""For this section we will use the filter feature to filter through the most important attributes in the dataset according to the feature importance chart. """)
    df = pd.read_csv("Kenya-hospitals.csv")
    AgGrid(df)

    st.markdown("""
        
        Which means to determine the best hospital to visit you will have to:
        
        1. Identify the service you require from the KEPH level service display on the home page and input the KEPH level
         
        2. Input your county, sub county, constituency and ward to get the facility closest to you. 
         
        3. Input the category of facility you wish to visit 
        
        Side note: Most level 2 facilities are either in the category, Medical clinic or stand alone or dispensary and they are mostly private practice. Level 3 facilities are either in the category Health centre, Nursing home or Medical Center. Level 4, Level 5 and Level 6 are all in the category Hospitals 
         
        4. Based on the time you want to visit you will input your desired availability eg. open whole day
        
        5. Finally, input the owner of the facility you would wish to visit
    """)

def Search_using_input_features():
    st.markdown("""For this section we will use the most input features to filter through the data according to the feature importance chart """)
    st.sidebar.header('User Input Features')
    Data = pd.read_csv("Kenya-hospitals.csv")
    st.sidebar.header('Facility Info')
    st.sidebar.header('Administrative unit')
    County = st.sidebar.selectbox('County', Data["County"].unique())
    Sub_county = st.sidebar.text_input('Sub_county')
    Constituency = st.sidebar.text_input('Constituency')
    Ward = st.sidebar.text_input('Ward')
    st.sidebar.header('Facility Details')
    Keph_level = st.sidebar.selectbox('Keph_level', ('Level 2', 'Level 3', 'Level 4', 'Level 5', 'Level 6'))
    Facility_type_category = st.sidebar.selectbox('Facility_type_category', (
    'DISPENSARY', 'HEALTH CARE', 'HOSPITALS', 'MEDICAL CENTER', 'MEDICAL CLINIC', 'NURSING HOME', 'STAND ALONE',
    'Primary health care services'))
    Owner_type = st.sidebar.selectbox('Owner_type', (
    'Faith Based Organization', 'Ministry of Health', 'Non-Governmental Organizations', 'Private Practice'))
    st.sidebar.header('Availability')
    Open_whole_day = st.sidebar.selectbox('Open_whole_day', ('Yes', 'No'))
    Open_public_holidays = st.sidebar.selectbox('Open_public_holidays', ('Yes', 'No'))
    Open_weekends = st.sidebar.selectbox('Open_weekends', ('Yes', 'No'))
    Open_late_night = st.sidebar.selectbox('Open_late_night', ('Yes', 'No'))
    df_selected_team = Data[(Data.County.str.contains(County)) & (Data.Sub_county.str.contains(Sub_county)) & (Data.Constituency.str.contains(Constituency)) & (Data.Ward.str.contains(Ward)) & (Data.Keph_level.str.contains(Keph_level)) & (Data.Facility_type_category.str.contains(Facility_type_category)) & (Data.Owner_type.str.contains(Owner_type)) & (Data.Open_whole_day.str.contains(Open_whole_day)) & (Data.Open_public_holidays.str.contains(Open_public_holidays)) & (Data.Open_weekends.str.contains(Open_weekends)) & (Data.Open_late_night.str.contains(Open_late_night))]
    st.dataframe(df_selected_team)

    st.markdown("""
        Which means to determine the best hospital to visit you will have to:
        
        1. Identify the service you require from the KEPH level service display on the home page and input the KEPH level
         
        2. Input your county, sub county, constituency and ward to get the facility closest to you. 
         
        3. Input the category of facility you wish to visit
         
         Side note: Most level 2 facilities are either in the category, Medical clinic or stand alone or dispensary and they are mostly private practice. Level 3 facilities are either in the category Health centre, Nursing home or Medical Center. Level 4, Level 5 and Level 6 are all in the category Hospitals 
         
        4. Based on the time you want to visit you will input your desired availability
        
        5. Finally, input the owner of the facility you would wish to visit
    """)

def Machine_Learning():
    st.title("Machine Learning")
    st.markdown(
        """A machine learning model was used to predict whether a patient should visit a Level 2 or a level 3 or a Level 4 or a Level 5 or a Level 6 medical facility hence predicting the best hospital in an Area based on a given set of attributes. The Keph Level column was chosen as the target variable. This is because the Keph levels represent the six levels of health care service delivery in Kenya""")

    st.subheader('Keph_levels Bar Chart ')
    image = Image.open('Keph_level.png')
    st.image(image, caption='Graphical representation of hospitals in Kenya grouped by Keph_levels')

    st.markdown("""
        These are the attributes that were used to train and test the model: They were classified into three:
    
        1. Administrative unit/ Location: County codes 
    
        2. Facility information: Facility type category, Owner type, Regulatory body
        
        3. Availability: Open whole day, Open public holidays, Open weekends, Open late night  
        
        On the basis of these attributes, we predict which hospital is optimal for the patients. The KNN classifies which hospital is optimal and which is not for the patient according to their needs.
    """)
    st.markdown("""The graph below shows the most important features in predicting the best hospital in an area""")
    st.subheader('Feature importance')
    image = Image.open('Feature_importance.png')
    st.image(image, caption='Feature importance bar chart')
    st.markdown("""The best features in predicting the best hospital in an area include (in order of importance):""")
    st.markdown("""
        1.Location: County

        2.Facility type category

        3.Open whole day
         
        4.open weekends

        5.Owner type
    """)

    st.subheader('Models used')
    df = pd.DataFrame({
        'Classifier': ['KNeighborsClassifier', 'SVCclassifier', 'DecisionTreeClassifier'],
        'Accuracy': ['0.99', '0.93', '0.87']
    })

    df

    st.markdown("""
        The KNN model achieved a 99.0% accuracy score at predicting the Level of facility that is most suitable for the patient given the full feature set that was used to train and test the model. Followed by the SVC model at 93.0% accuracy and lastly the decision tree model at 87.0% accuracy.
     
        This means that given the patient location, the category of the facility they want to visit, the patients availability and the owner of the facility the patient wishes to visit. our model is able to predict the level of the facility that is most suitable.
        
        Therefore, to predict the best hospital to visit a patient can input the Level of facility the  model has predicted, the location they chose, the category they chose, the availability they chose, the owner type they chose to get a list of facilities in their area that fit their description 
     """)

def prediction_features():
    def input_features():
        st.sidebar.header('Input Features')
        input_df = pd.read_csv("Kenya-hospitals_cleaned.csv")
        county_codes = st.sidebar.selectbox('country_codes',input_df["county_codes"].unique())
        facility_category = st.sidebar.selectbox('Facility_category', ('DISPENSARY', 'HEALTH CARE', 'HOSPITALS', 'MEDICAL CENTER', 'MEDICAL CLINIC', 'NURSING HOME', 'STAND ALONE', 'Primary health care services'))
        owner = st.sidebar.selectbox('Owner', ('Faith Based Organization', 'Ministry of Health', 'Non-Governmental Organizations', 'Private Practice'))
        whole_day = st.sidebar.selectbox('whole_day', ('Yes', 'No'))
        public_holidays = st.sidebar.selectbox('public_holidays', ('Yes', 'No'))
        weekends = st.sidebar.selectbox('weekends', ('Yes', 'No'))
        late_night = st.sidebar.selectbox('late_night', ('Yes', 'No'))
        data = {'county_codes': county_codes,
            'facility_category': facility_category,
            'owner': owner,
            'whole_day':  whole_day,
            'open_public_holidays': public_holidays,
            'open_weekends': weekends,
            'late_night': late_night}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = input_features()
    #st.dataframe(input_df)

    # Ordinal feature encoding
    hospital = pd.read_csv('Kenya-hospitals_cleaned.csv')
    hospitals = hospital.drop(columns=['KEPH'], axis=1)
    Df = pd.concat([input_df, hospitals], axis=0)
    encode = ['Facility_category','Owner', 'whole_day', 'public_holidays', 'weekends', 'late_night']

    for col in encode:
        dummy = pd.get_dummies(Df[col], prefix=col)
        Df = pd.concat([Df,dummy], axis=1)
        del Df[col]
        Df = Df[:1]

    # Reads in saved classification model
    load_clf = pickle.load(open('hospitals_clf.pkl', 'rb'))
    # Apply model to make predictions
    prediction = load_clf.predict(Df)
    prediction_proba = load_clf.predict_proba(Df)
    st.subheader('Prediction')
    hospital_levels = np.array(['Level 2', 'Level 3', 'Level 4', 'Level 5', 'Level 6'])
    st.write(hospital_levels[prediction])

    st.subheader('Prediction Probability')
    st.write(prediction_proba)

# Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Advanced Search', 'Search Using Input Features', 'Machine Learning', 'Prediction Features'])

# Navigation options
if options == 'Home':
    Home()
elif options == 'Advanced Search':
    Advanced_Search()
elif options == 'Search Using Input Features':
    Search_using_input_features()
elif options == 'Machine Learning':
    Machine_Learning()
elif options == 'Prediction Features':
    prediction_features()
