import os

from datetime import datetime
from project_path import features_path

def get_datetime_suffix():
  """
    Get the timestamp suffix
  """
  return datetime.now().strftime('_%Y%m%d_%H%M%S')

def file_exists(filepath):
  """
    Check file exists
  """
  return os.path.isfile(filepath)

def feature_file_exists():
  """
    Determine feature files exists
  """
  return file_exists(features_path + '/train.csv')

def select_feature_file_exists():
  """
    Selected feature files exists
  """
  return file_exists(features_path + '/selected_train.csv')