import pickle
import numpy as np
from classes import MLFeatures


def compute_cluster(mlfs: list[MLFeatures]):
    t = np.zeros(len(mlfs[0]), dtype='float64')
    for m in mlfs:
        t += np.array(list(m.values()), dtype='float64')
    t /= len(mlfs)
    t = t[None, :]

    with open("gmm", "rb") as f:
        gmm = pickle.load(f)
    
    probs = gmm.predict_proba(t)
    max_indices = np.argmax(probs, axis=1)
    vector = np.zeros((probs.shape[0],), dtype=np.int64)
    vector[np.arange(probs.shape[0])] = max_indices

    return vector