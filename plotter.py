import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



loaded_data = np.load("All-Data-M2/500k/data_500k_0p.npz")

measured_frequencies = loaded_data['arr1']  # Access array1
amplitudes_db = loaded_data['arr2']  # Access array2
loaded_data.close() # It's good practice to close the file




# Plotting the Bode plot
plt.figure(figsize=(10, 6))
plt.scatter(measured_frequencies, amplitudes_db, label='Measured Data')  # Added label for clarity
plt.plot(measured_frequencies, amplitudes_db, linestyle='-', label='Interpolated Curve')  # Added linestyle for a continuous line

plt.title("Bode Plot")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dB)")
plt.xscale("log")  # Ensure x-axis is logarithmic
plt.grid(True)
plt.legend()  # Show the legend to identify the data
plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()