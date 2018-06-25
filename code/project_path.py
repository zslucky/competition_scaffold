import os

# find cwd
this_file_path = os.path.abspath(__file__)
cwd = os.path.abspath(os.path.join(this_file_path, os.pardir, os.pardir))

# data root
data_path = os.path.join(cwd, 'data')
dataset_path = os.path.join(data_path, 'dataset')
features_path = os.path.join(data_path, 'features')
selected_features_path = os.path.join(data_path, 'selected_features')

# code root
code_path = os.path.join(cwd, 'code')

# code root
submit_path = os.path.join(cwd, 'submit')