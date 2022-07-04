import pandas as pd
# Ordinal feature encoding
hospital = pd.read_csv('Kenya-hospitals_cleaned.csv')
Df = hospital.copy()
county = 'County'
county_mapper= {'Mombasa': 1, 'Kwale': 2, 'Kilifi': 3, 'Tana River': 4, 'Lamu': 5, 'Taita Taveta': 6, 'Garissa': 7,
                'Wajir': 8, 'Mandera': 9, 'Marsabit': 10, 'Isiolo': 11, 'Meru': 12, 'Tharaka Nithi': 13, 'Embu': 14,
                'Kitui': 15, 'Machakos': 16, 'Makueni': 17, 'Nyandarua': 18, 'Nyeri': 19, 'Kirinyaga': 20,
                'Muranga': 21, 'Kiambu': 22, 'Turkana': 23, 'West Pokot': 24, 'Samburu': 25, 'Trans Nzoia': 26,
                'Uasin Gishu': 27, 'Elgeyo Marakwet': 28, 'Nandi': 29, 'Baringo': 30, 'Laikipia': 31, 'Nakuru': 32,
                'Narok': 33, 'Kajiado': 34, 'Kericho': 35, 'Bomet': 36, 'Kakamega': 37, 'Vihiga': 38, 'Bungoma': 39,
                'Busia': 40, 'Siaya': 41, 'Kisumu': 42, 'Homa Bay': 43, 'Migori': 44, 'Kisii': 45, 'Nyamira': 46,
                'Nairobi': 47}


def county_encode(val):
    return county_mapper[val]


Df['County'] = Df['County'].apply(county_encode)

facility_category = 'Facility_category'
facility_mapper = {'DISPENSARY': 0, 'HEALTH CENTRE': 1, 'HOSPITALS': 2, 'MEDICAL CENTER': 3, 'MEDICAL CLINIC': 4, 'NURSING HOME': 5, 'STAND ALONE': 6, 'Primary health  care services': 7, 'None': 8}


def facility_category_encode(val):
    return facility_mapper[val]


Df['Facility_category'] = Df['Facility_category'].apply(facility_category_encode)

owner = 'Owner'
Owner_mapper = {'Faith Based Organization': 0, 'Ministry of Health': 1, 'Non-Governmental Organizations': 2, 'Private Practice': 3}


def Owner_encode(val):
    return Owner_mapper[val]


Df['Owner'] = Df['Owner'].apply(Owner_encode)


whole_day = 'whole_day'
whole_day_mapper = {"Yes": 1, "No": 0}


def whole_day_encode(val):
    return whole_day_mapper[val]


Df['whole_day'] = Df['whole_day'].apply(whole_day_encode)

public_holidays = 'public_holidays'
public_holidays_mapper = {"Yes": 1, "No": 0}


def public_holidays_encode(val):
    return public_holidays_mapper[val]


Df['public_holidays'] = Df['public_holidays'].apply(public_holidays_encode)

weekends = 'weekends'
weekends_mapper = {"Yes": 1, "No": 0}


def weekends_encode(val):
    return weekends_mapper[val]


Df['weekends'] = Df['weekends'].apply(weekends_encode)

late_night = 'late_night'
late_night_mapper = {"Yes": 1, "No": 0}


def late_night_encode(val):
    return late_night_mapper[val]


Df['late_night'] = Df['late_night'].apply(late_night_encode)
target = 'KEPH'
target_mapper = {'Level 2': 0, 'Level 3': 1, 'Level 4': 2, 'Level 5': 3, 'Level 6': 4}


def target_encode(val):
    return target_mapper[val]


Df['KEPH'] = Df['KEPH'].apply(target_encode)
# Separating X and y
X = Df.drop('KEPH', axis=1)
Y = Df['KEPH']

# Build random forest model
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier()
clf.fit(X, Y)

# Saving the model
import pickle
pickle.dump(clf, open('clf.pkl', 'wb'))
