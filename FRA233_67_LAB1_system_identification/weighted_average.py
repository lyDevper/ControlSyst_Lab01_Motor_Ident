import numpy as np
import pandas as pd

# Data for the table
data = {
    "Model": ["sin0d1", "sin1d0", "sin2d0", "ramp1d2", "ramp2d4", "ramp3d6", "pulse0d1", "pulse1d0", "pulse2d0", "stair1", "stair2", "stair3", "chirp1", "chirp2", "chirp3"],
    "motor_B": [2.63E-05, 2.07E-04, 2.10E-04, 7.36E-05, 6.75E-05, 6.01E-05, 4.61E-05, 5.37E-05, 1.76E-06, 3.93E-05, 5.12E-07, 3.96E-05, 1.99E-04, 3.91E-05, 1.98E-04],
    "motor_Eff": [0.957, 0.949, 0.970, 0.614, 0.759, 0.812, 0.996, 0.928, 0.972, 0.971, 0.997, 0.998, 0.906, 0.934, 0.932],
    "motor_J": [3.71E-05, 3.11E-05, 2.37E-05, 7.92E-04, 4.21E-04, 3.21E-04, 9.51E-05, 4.98E-05, 4.19E-05, 2.20E-05, 8.46E-06, 4.29E-05, 3.18E-05, 3.17E-05, 2.90E-05],
    "motor_Ke": [0.0564, 0.0433, 0.0415, 0.0334, 0.0505, 0.0517, 0.0540, 0.0539, 0.0588, 0.0580, 0.0607, 0.0567, 0.0481, 0.0532, 0.0445],
    "motor_Km": [0.0540, 0.0411, 0.0403, 0.0205, 0.0383, 0.0420, 0.0538, 0.0500, 0.0571, 0.0563, 0.0605, 0.0566, 0.0436, 0.0497, 0.0415],
    "R² Average": [0.894, 0.795, 0.826, 0.032, 0.403, 0.479, 0.748, 0.846, 0.887, 0.921, 0.910, 0.880, 0.774, 0.900, 0.806]
}

# Create DataFrame
df = pd.DataFrame(data)

# Filter out rows where R² < 0.8
filtered_df = df[df["R² Average"] >= 0.8]

# Calculate weighted averages for each column (excluding R² Average column)
weighted_averages = {}
for col in ["motor_B", "motor_Eff", "motor_J", "motor_Ke", "motor_Km"]:
    weighted_average = np.sum(filtered_df[col] * filtered_df["R² Average"]) / np.sum(filtered_df["R² Average"])
    weighted_averages[col] = weighted_average

# Calculate square-weighted averages for each column (excluding R² Average column)
square_weighted_averages = {}
for col in ["motor_B", "motor_Eff", "motor_J", "motor_Ke", "motor_Km"]:
    square_weighted_average = np.sum((filtered_df["R² Average"]**2) * filtered_df[col]) / np.sum(filtered_df["R² Average"]**2)
    square_weighted_averages[col] = square_weighted_average

# Create a DataFrame for the results
result_df = pd.DataFrame({
    "Weighted Average": weighted_averages,
    "Square-Weighted Average": square_weighted_averages
})

# Export the results to CSV
result_df.to_csv("motor_weighted_averages.csv")

# Print the results
print(result_df)
