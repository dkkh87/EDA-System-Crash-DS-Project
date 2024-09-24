import pandas as pd
import numpy as np
 
# Set random seed for reproducibility
np.random.seed(45)
 
# Parameters
num_rows = 50000

# 4 CORES, 8 GB RAM, 1Gbps (1000MB) 
# Generate random data
data = {
    'Device ID': range(1, num_rows + 1),
    'CPU Usage (%)': np.array([np.round(np.random.uniform(101, 300), 3) if i % 4000 == 0 else "" if i % 6000 == 0 else np.round(np.random.uniform(20,30), 3) if i % 23 == 0 else np.round(np.random.uniform(19,70), 3) if i % 17 == 0 else np.round(np.random.uniform(1, 100), 3) for i in range(num_rows)]),
    'Memory Usage (MB)': np.array([np.random.randint(8500, 10000) if i % 4000 == 0  else np.random.randint(700 ,3700) if i % 23 == 0 else np.random.randint(434, 6678) if i % 19 == 0 else np.random.randint(800, 4978) if i % 57 == 0 else np.random.randint(500, 8000) if i % 59 == 0 else np.random.randint(3200, 8000) for i in range(num_rows)]),
    'Disk Usage (%)': np.array([np.random.randint(101, 125) if i % 3000 == 0  else np.random.randint(0, 100) if i % 23 == 0 else np.random.randint(0, 70) if i % 19 == 0 else np.random.randint(35, 45) if i % 57 == 0 else np.random.randint(0, 85) if i % 59 == 0 else np.random.randint(65, 100) for i in range(num_rows)]),
    'Network Activity (MB/s)': np.array([np.random.randint(1010, 1050) if i % 3000 == 0  else np.random.randint(377, 597) if i % 23 == 0 else np.random.randint(0, 1000) if i % 19 == 0 else np.random.randint(0, 450) if i % 57 == 0 else np.random.randint(200, 1000) if i % 59 == 0 else np.random.randint(0, 1000) for i in range(num_rows)]),
    'System Average Load (%)': np.random.randint(0, 100, size=num_rows),
    'Battery Level (%)': np.random.randint(0, 100, size=num_rows),
    'App Count': np.random.randint(1, 60, size=num_rows),
    'Background Processes': np.random.randint(1, 50, size=num_rows),
    'GPU Usage (%)': np.array([np.random.randint(101, 500) if i % 2500 == 0 else "" if i % 1200 == 0 else np.random.randint(23, 53) if i % 23 == 0 else np.random.randint(0, 100) if i % 19 == 0 else np.random.randint(5, 65) if i % 77 == 0 else np.random.randint(20, 100) if i % 59 == 0 else np.random.randint(0, 100) for i in range(num_rows)]),
    'Temperature (°C)': np.array([np.round(np.random.uniform(150, 200), 3) if i % 6000 == 0 else np.round(np.random.uniform(20,50), 3) if i % 23 == 0 else np.round(np.random.uniform(23,73), 3) if i % 17 == 0 else np.round(np.random.uniform(30, 100), 3) for i in range(num_rows)]),
    'Storage Available (GB)': np.random.randint(0, 500, size=num_rows),
    'Recent App': np.random.choice(['Amazon', 'Spotify', 'Netflix', 'Youtube', 'Tiktok', 'Snapchat', 'Twitter', 'Instagram', 'WhatsApp', 'Facebook', 'Audible', 'Candy Crush Saga', 'Signal', 'Reddit'], size=num_rows),
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

random_rows = df.sample(n=1000, random_state=25)
df = pd.concat([df, random_rows])

# Save to CSV
df.to_csv('../../eda/device_crash_dataset.csv', index=False)
 
print("Dataset generated and saved as '../../eda/device_crash_dataset.csv'.")
