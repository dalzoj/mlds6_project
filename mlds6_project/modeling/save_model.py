import joblib

def save_model(model, name='model'):
    with open('mlds6_project/models/'+name+'.pkl', 'wb') as f:
        joblib.dump(model, f)
