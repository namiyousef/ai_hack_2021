# libraries
import numpy as np


def scale_data(data, mode="standard"):
    """
    scales data and outputs the scaling values (scales using standard scaler)

    Dependencies:
    -------------
    import numpy as np

    """
    n_attr = data.shape[1]
    scalers = np.zeros([2, n_attr])
    if mode == "standard":
        scalers[0, :] = data.mean(axis=0)
        scalers[1, :] = data.std(axis=0)
        scaled = (data - scalers[0, :]) / scalers[1, :]
    elif mode == "minmax":
        scalers[0, :] = data.min(axis=0)
        scalers[1, :] = data.max(axis=0) - scalers[0, :]
        scaled = (data - scalers[0, :]) / scalers[1, :]
    elif mode == "maxabs":
        scalers[0, :] = 0
        scalers[1:] = abs(data).max(axis=0)
        scaled = (data) / scalers[1, :]
    elif mode == "robust":
        scalers[0, :] = data.median(axis=0)
        scalers[1, :] = data.quantile(0.75, axis=0) - data.quantile(0.25, axis = 0)
        scaled = (data - scalers[0, :]) / scalers[1, :]

    return scaled, scalers