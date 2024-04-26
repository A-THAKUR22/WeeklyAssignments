import numpy as np

"""
    Scale input features using the provided scaler
    Returns:
        array-like: Scaled input features.
"""
def helper_func(input_features, scaler):
    input_features_array=np.array(input_features).reshape(1,-1)
    scaled_features=scaler.transform(input_features_array)
    return scaled_features