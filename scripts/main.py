from mlds6_project.data.get_data import get_data
from mlds6_project.preprocessing.select_x_y import select_x_y
from mlds6_project.preprocessing.data_preprocessing import data_preprocessing
from mlds6_project.modeling.get_train_test_data import get_train_test_data
from mlds6_project.modeling.knn_model import knn_model
from mlds6_project.evaluation.evaluate_model import evaluate_model
from IPython.display import display

url = '../dataset/hepatitis_data.csv'

df = get_data(url)

X, y = select_x_y(df, 'Category')

#X, y = data_preprocessing(x,y)

X_train, X_test, y_train, y_test = get_train_test_data(X, y, 0.2, 0)

model = knn_model(X_train, y_train)

accuracy_train, accuracy_test = evaluate_model(model, X_train, X_test, y_train, y_test)

print(f'Precisión de entrenamiento: {accuracy_train}')
print(f'Precisión de prueba: {accuracy_test}')




import joblib
MODEL_PATH = '../mlds6_project/models/knn_model.pkl'
with open(MODEL_PATH, 'rb') as f:
    model_two = joblib.load(f)

print(model_two.predict([[32,1,38.5,52.5,7.7,22.1,7.5,6.93,3.23,106,12.1,69]]))