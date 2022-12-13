from sklearn.model_selection import train_test_split
import numpy as np

def get_train_test_data(X_data, y_data, test_value=0.2, random_state=0):
  X_data = np.array(X_data)
  y_data = np.array(y_data)
  X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=test_value, random_state=random_state, stratify=y_data)
  return X_train, X_test, y_train, y_test