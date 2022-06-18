from st_aggrid import AgGrid
import streamlit as st
import pandas as pd
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

st.title('Hospitals In Kenya Web App')
st.markdown("""
    Hospitals in Kenya web app is an application containing all health facilities in Kenya. Each health facility is identified by a code followed by details describing the geographical location, administrative location, ownership, and availability of the facility.
""")
st.header('Hospitals Dataset')
st.markdown("""Data source: OpenData portal""")

Data = pd.read_csv("Kenya-hospitals.csv")
print(Data.head())
st.write(Data)

st.title("Advanced Search")
st.markdown("""For the advanced search we will use the filter feature to determine the best facility in an area using the most important features as per the feature importance bar chart""")
df = pd.read_csv("Kenya-hospitals.csv")
AgGrid(df)

st.title("Machine Learning")
st.markdown("""A machine learning model was used to predict the best hospital in an Area. The target variable used was the Keph Level""")
st.subheader('The six levels of health care service delivery in Kenya')
image = Image.open('The-six-levels-of-health-care-service-delivery-in-Kenya.png')
st.image(image, caption='Keph_levels in a nutshell')

st.subheader('Keph_levels Bar Chart ')
image = Image.open('Keph_level.png')
st.image(image, caption='Graphical representation of hospitals in Kenya grouped by Keph_levels')

st.markdown("""The graph below shows the most important features in predicting the best hospital in an area""")
st.subheader('Feature importance')
image = Image.open('Feature_importance.png')
st.image(image, caption='Feature importance bar chart')
st.markdown("""The best features in predicting the best hospital in an area include:

1.Location: County

2.Facility type category

3.Availability :Openwhole day, open weekends

4.Owner type
""")

st.subheader('Models used')
df = pd.DataFrame({
          'Classifier': ['KNeighborsClassifier', 'SVCclassifier', 'DecisionTreeClassifier'],
          'Accuracy': ['0.99', '0.93', '0.87']
  })

df
