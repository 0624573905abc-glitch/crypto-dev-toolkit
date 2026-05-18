import numpy as np

class CryptoGameProcessor:
    def __init__(self):
        self.data = np.array([])

    def load_data(self, new_data):
        self.data = np.concatenate((self.data, np.array(new_data)))

    def process_data(self):
        if self.data.size == 0:
            return
        mean_value = np.mean(self.data)
        std_dev_value = np.std(self.data)
        return mean_value, std_dev_value

    def optimize_processing(self):
        compressed_data = np.round(self.data, decimals=2)
        unique_values, counts = np.unique(compressed_data, return_counts=True)
        optimization_dict = dict(zip(unique_values, counts))
        return optimization_dict

    def reset_data(self):
        self.data = np.array([])