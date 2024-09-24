import pandas as pd
import numpy as np
 
# Set random seed for reproducibility
np.random.seed(45)
 
# Parameters
num_rows = 100000

# 4 CORES, 8 GB RAM, 1Gbps (1000MB) 
# Generate random data
data = {
    'Device ID': range(1, num_rows + 1),
    'CPU Usage (%)': np.array([np.random.randint(101, 300) if i % 4000 == 0 else "" if i % 6000 == 0 else np.random.randint(20, 100) for i in range(num_rows)]),
    'Memory Usage (MB)': np.array([np.random.randint(8500, 10000) if i % 4000 == 0 else np.random.randint(500, 8000) for i in range(num_rows)]),
    'Disk Usage (%)': np.random.randint(10, 100, size=num_rows),
    'Network Activity (MB/s)': np.random.randint(0, 500, size=num_rows),
    'Network Activity (MB/s)': np.array([np.random.randint(1010, 1050) if i % 3000 == 0 else np.random.randint(0, 1000) for i in range(num_rows)]),
    'System Average Load (%)': np.random.randint(0, 100, size=num_rows),
    'Battery Level (%)': np.random.randint(0, 100, size=num_rows),
    'App Count': np.random.randint(1, 60, size=num_rows),
    'Background Processes': np.random.randint(1, 50, size=num_rows),
    'GPU Usage (%)': np.array([np.random.randint(101, 500) if i % 2500 == 0 else "" if i % 1200 == 0 else np.random.randint(0, 100) for i in range(num_rows)]),
    'Temperature (°C)': np.array([np.random.randint(150, 200) if i % 6000 == 0 else np.random.randint(30, 100) for i in range(num_rows)]),
    'Storage Available (GB)': np.random.randint(0, 500, size=num_rows),
    'Recent App': np.random.choice(['App A', 'App B', 'App C', 'App D', 'App E', 'App F', 'App G', 'App H', 'App I', 'App J'], size=num_rows),
    'Screen Brightness (%)': np.random.randint(0, 100, size=num_rows),
    'User Activity Level': np.random.choice(['Low', 'Medium', 'High'], size=num_rows),

}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Determine if the system crashed based on some conditions
df['System Crash (Yes/No)'] = np.where(
    (df['CPU Usage (%)'] > "90") | 
    (df['Memory Usage (MB)'] > 6500) | 
    (df['Disk Usage (%)'] > 85) | 
    (df['System Average Load (%)'] > 88) | 
    (df['Network Activity (MB/s)'] > 900),
    'Yes',
    'No'
)
 
# Save to CSV
df.to_csv('device_crash_dataset.csv', index=False)
 
print("Dataset generated and saved as 'device_crash_dataset.csv'.")
