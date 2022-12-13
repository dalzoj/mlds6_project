import pandas as pd

def get_data(url):
  return pd.read_csv(url, index_col=0)