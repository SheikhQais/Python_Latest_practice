import numpy as np
from scipy import stats

Speed = [78,77,79,87,88,82,78,74,90,89,112,67,102,77]
print("Mean:", np.mean(Speed))
print("Median:", np.median(Speed))
print("Mode:", stats.mode(Speed, keepdims=True).mode[0])