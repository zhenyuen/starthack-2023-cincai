import pickle
import numpy as np


def compute_cluster(features):
    with open("gmm", "rb") as f:
        gmm = pickle.load(f)
    
    probs = gmm.predict_proba(features)
    max_indices = np.argmax(probs, axis=1)
    vector = np.zeros((probs.shape[0],), dtype=np.int64)
    vector[np.arange(probs.shape[0])] = max_indices

    return vector

    