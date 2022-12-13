import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def get_dtypes(list_in, dataframe):
  return [str(dataframe[i].dtypes) for i in list_in]

def transformation(categorical_list, numeric_list):
  transformer = ColumnTransformer(
      transformers=[
          ("categorical", OneHotEncoder(), categorical_list),
          ("numeric", StandardScaler(), numeric_list),
          ]
          )
  return transformer

def data_preprocessing(df_x, df_y):
    df_x = pd.DataFrame(df_x)
    df_y = pd.DataFrame(df_y)
    dtypes_list = get_dtypes(df_x.columns.tolist(), df_x)
    categorical_list = []
    numeric_list = []
    for i in range(len(dtypes_list)):
        if dtypes_list[i] != 'int64' and dtypes_list[i] != 'float64': categorical_list.append(df_x.columns.tolist()[i])
        else: numeric_list.append(df_x.columns.tolist()[i])
    return transformation(categorical_list, numeric_list).fit_transform(df_x), df_y.to_numpy().flatten()
