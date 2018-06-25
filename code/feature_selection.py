import pandas as pd

from utils import feature_file_exists
from project_path import features_path

# chi2_Kbest_num = 175

## Example do selectedKBest by using chi2
# def chi2_transform(df_train, df_test):
  """
    Selected Kbest use chi2 algorthim
  """
  # pass


def do_multi_selection(df_train, df_test):
  """
    Do multi selection here
  """
  # Generate chi2 selected
  # chi2_transform(df_train, df_test)
  pass


def select_features():
  """
    Extract features
    The entry function
  """
  print('feature selecting...')

  if not feature_file_exists():
    return

  df_train = pd.read_csv(features_path + '/train.csv')
  df_test = pd.read_csv(features_path + '/test.csv')

  do_multi_selection(df_train, df_test)

  print('feature select finished.')
