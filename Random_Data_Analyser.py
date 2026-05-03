import numpy as np

data = np.random.randint(1, 70, 100)


print("\n==============================")
print("   NUMPY DATA ANALYSIS REPORT")
print("==============================\n")
print(f"Mean:\t\t{np.mean(data):.2f}")
print(f"Median:\t\t{np.median(data):.2f}")
print(f"Std Dev:\t{np.std(data):.2f}")
print(f"Max Value:\t{np.max(data)}")
print(f"Min value:\t{np.min(data)}")

