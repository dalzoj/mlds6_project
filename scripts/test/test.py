import joblib
import os

MODEL_PATH = '../../mlds6_project/models/knn_model.pkl'


with open(MODEL_PATH, 'rb') as f:
    model = joblib.load(f)

print(model.predict([[32,1,38.5,52.5,7.7,22.1,7.5,6.93,3.23,106,12.1,69]]))
