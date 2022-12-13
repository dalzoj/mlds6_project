import pandas as pd

def select_x_y(dataframe, y_column_name):
  df = pd.DataFrame(dataframe)
  clean_df = df.dropna(how='any')
  X_list = clean_df.columns.to_list()
  X_list.remove(y_column_name)
  return clean_df[X_list], clean_df[y_column_name]