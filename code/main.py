import os
import pandas as pd

from feature_extraction import extract_features
from feature_selection import select_features
from train import train
from utils import feature_file_exists, select_feature_file_exists

def main():
  """
    Main function
  """
  # Extract features
  if not feature_file_exists():
    extract_features()

  # Select features
  if not select_feature_file_exists():
    select_features()

  # Train model
  train()


if __name__ == '__main__':
  main()