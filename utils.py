import time
import numpy as np

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def time_function(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.execution_times.append(end_time - start_time)
            return result
        return wrapper

    def get_average_time(self):
        if not self.execution_times:
            return 0
        return np.mean(self.execution_times)

    def reset_times(self):
        self.execution_times.clear()

# Example usage
@PerformanceOptimizer().time_function
def heavy_computation(x):
    total = 0
    for i in range(1, x + 1):
        total += i ** 2
    return total

# Call the function to see performance logging
result = heavy_computation(10000)
avg_time = PerformanceOptimizer().get_average_time()
print(f"Result: {result}, Average Execution Time: {avg_time}")