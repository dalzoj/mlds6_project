import joblib
import shutil
from os import remove

def save_model(model, name='model'):
    with open('../mlds6_project/models/'+name+'.pkl', 'wb') as f:
        joblib.dump(model, f)
