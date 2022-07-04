import streamlit as st
import pandas as pd
import numpy as np
import time

st.sidebar.write("Select your option:")
st.sidebar.title("Background Information")
st.title('Hospitals In Kenya Web App')
st.header('Hospitals Dataset')

Data = pd.read_csv(r"C:\Users\User\Desktop\Hospital Recommendor\Kenya-hospitals.csv")
print(Data.head())
st.write(Data)

st.sidebar.title("Advanced Search")
st.sidebar.header('Facility Info')
#Checkbox for Hospitals
Facility_name = st.sidebar.selectbox("Select Hospital", Data["Name"].unique())
Facility_code = st.sidebar.selectbox("Select Code", Data["Code"].unique())

st.sidebar.header('Administrative unit')
County = st.sidebar.selectbox("Select County", Data["County"].unique())
Sub_county = st.sidebar.selectbox("Select Sub county", Data["Sub_county"].unique())
Constituency = st.sidebar.selectbox("Select Constituency", Data["Constituency"].unique())
Ward = st.sidebar.selectbox("Select ward", Data["Ward"].unique())

st.sidebar.header('Facility Details')

def user_input_features():
    Keph_level = st.sidebar.selectbox('Keph_level', ('Level 2', 'Level 3', 'Level 4', 'Level 5', 'Level 6'))

    Facility_type_category = st.sidebar.selectbox("Select Code", Data["Code"].unique())ONE', 'Primary healthcare services'))

    Owner_type = st.sidebar.selectbox('Owner_type', ('Faith Based Organization', 'Ministry of Health', 'Non-Governmental Organizations', 'Private Practice'))

    Data = {'Keph_level': [Keph_level],

            'Facility_type_category': [Facility_type_category],

            'Owner_type': [Owner_type]}

    features = pd.DataFrame(Data)

    return features

input_df = user_input_features()

st.sidebar.header('Availability')
def user_input_features():
    Open_whole_day = st.sidebar.checkbox('Open_whole_day', ('Yes', 'No'))

    Open_public_holidays = st.sidebar.checkbox('Open_public_holidays', ('Yes', 'No'))

    Open_weekends = st.sidebar.checkbox('Open_weekends', ('Yes', 'No'))

    Open_late_night = st.sidebar.checkbox('Open_late_night', ('Yes', 'No'))

    Data = {'Open_whole_day': [Open_whole_day],

            'Open_public_holidays': [Open_public_holidays],

            'Open_weekends': [Open_weekends],

            'Open_late_night': [Open_late_night]}

    features = pd.DataFrame(Data)

    return features


input_df = user_input_features()