import json
import numpy as np
import pickle

__locations = None
__data_columns = None
__model = None

def getestimatedprice(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())  # Fixed lower() call
    except ValueError:
        loc_index = -1  # Corrected exception handling

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1  # Set the location one-hot encoding

    return round(__model.predict([x])[0], 2)

def getlocationnames():
    return __locations

def load_saved_artifacts():
    print("Loading Artifacts...")
    global __data_columns
    global __locations
    global __model  # Added global reference for __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    
    print("Artifacts Loaded Successfully.")

if __name__ == "__main__":
    load_saved_artifacts()
    print(getlocationnames())
    print(getestimatedprice('Indira Nagar', 1000, 3, 3))
    print(getestimatedprice('1st Phase JP Nagar',1000, 3, 3))
