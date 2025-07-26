from tensorflow import keras
import numpy as np
from Feature_Extractor import extract_features

def get_prediction(url, model_path):
    print("Loading the model...")
    model = keras.models.load_model(model_path)

    print("Extracting features from url...")
    url_features = extract_features(url)
    print(url_features)

    print("Making prediction...")
    # Convert to NumPy array and reshape if needed
    url_features = np.array([url_features])  # shape becomes (1, 16) instead of just list of list
    prediction = model.predict(url_features)

    i = prediction[0][0] * 100
    i = round(i, 3)
    print("There is", i, "% chance, the url is malicious!")

    return i
