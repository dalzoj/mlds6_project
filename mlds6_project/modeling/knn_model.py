from sklearn.neighbors import KNeighborsClassifier
from mlds6_project.modeling.save_model import save_model

def knn_model(X_train_data, y_train_data):
    knn_model = KNeighborsClassifier(
        algorithm='auto',
        n_neighbors=1,
        weights='uniform'
    )
    knn_model.fit(X_train_data, y_train_data)
    save_model(knn_model,'knn_model')
    return knn_model