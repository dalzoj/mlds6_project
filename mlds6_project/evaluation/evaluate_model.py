from sklearn.metrics import accuracy_score

def evaluate_model(model, X_train_data, X_test_data, y_train_data, y_test_data):
  y_train_pred = model.predict(X_train_data)
  y_test_pred = model.predict(X_test_data)
  return accuracy_score(y_train_data, y_train_pred), accuracy_score(y_test_data, y_test_pred)