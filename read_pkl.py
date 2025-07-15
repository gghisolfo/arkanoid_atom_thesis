import pickle
import sys

# Prende il percorso del file dalla riga di comando
file_path = sys.argv[1]

with open(file_path, 'rb') as f:
    data = pickle.load(f)

print(data)
