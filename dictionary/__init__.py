import os

__author__ = 'fuadsuyudi@gmail.com'

path = os.path.dirname(__file__)

def get(dict_file):
    with open(os.path.join(path, dict_file), 'r') as f:
        read_data = f.read().splitlines()
    return read_data