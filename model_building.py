import pandas as pd
# Ordinal feature encoding
hospital = pd.read_csv('Kenya-hospitals_cleaned.csv')
Df = hospital.copy()
target = 'KEPH'
encode = ['Facility_category', 'Owner', 'whole_day', 'public_holidays', 'weekends', 'late_night']

for col in encode:
    dummy = pd.get_dummies(Df[col], prefix=col)
    Df = pd.concat([Df, dummy], axis=1)
    del Df[col]
    Df = Df[:1]

target_mapper = {'Level 2': 0, 'Level 3': 1, 'Level 4': 2, 'Level 5': 3, 'Level 6': 4}


def target_encode(val):
    return target_mapper[val]


Df['KEPH'] = Df['KEPH'].apply(target_encode)
# Separating X and y
X = Df .drop('KEPH', axis=1)
Y = Df['KEPH']

# Build random forest model
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier()
clf.fit(X, Y)

# Saving the model
import pickle
pickle.dump(clf, open('hospitals_clf.pkl', 'wb'))