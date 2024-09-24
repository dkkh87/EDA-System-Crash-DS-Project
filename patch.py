
diff --git a/dataset/script/data_generator.py b/dataset/script/data_generator.py
index 33818d4..24b3030 100644
--- a/dataset/script/data_generator.py
+++ b/dataset/script/data_generator.py
@@ -11,17 +11,16 @@ num_rows = 1000000
 # Generate random data
 data = {
     'Device ID': range(1, num_rows + 1),
-    'CPU Usage (%)': np.array([np.round(np.random.uniform(101, 300), 3) if i % 4000 == 0 else "" if i % 6000 == 0 else np.round(np.random.uniform(20, 100), 3) for i in range(num_rows)]),
-    'Memory Usage (MB)': np.array([np.random.randint(8500, 10000) if i % 4000 == 0 else np.random.randint(500, 8000) for i in range(num_rows)]),
-    'Disk Usage (%)': np.random.randint(10, 100, size=num_rows),
-    'Network Activity (MB/s)': np.random.randint(0, 500, size=num_rows),
-    'Network Activity (MB/s)': np.array([np.random.randint(1010, 1050) if i % 3000 == 0 else np.random.randint(0, 1000) for i in range(num_rows)]),
+    'CPU Usage (%)': np.array([np.round(np.random.uniform(101, 300), 3) if i % 4000 == 0 else "" if i % 6000 == 0 else np.round(np.random.uniform(20,30), 3) if i % 23 == 0 else np.round(np.random.uniform(19,70), 3) if i % 17 == 0 else np.round(np.random.uniform(1, 100), 3) for i in range(num_rows)]),
+    'Memory Usage (MB)': np.array([np.random.randint(8500, 10000) if i % 4000 == 0  else np.random.randint(700 ,3700) if i % 23 == 0 else np.random.randint(434, 6678) if i % 19 == 0 else np.random.randint(800, 4978) if i % 57 == 0 else np.random.randint(500, 8000) if i % 59 == 0 else np.random.randint(3200, 8000) for i in range(num_rows)]),
+    'Disk Usage (%)': np.array([np.random.randint(101, 125) if i % 3000 == 0  else np.random.randint(0, 100) if i % 23 == 0 else np.random.randint(0, 70) if i % 19 == 0 else np.random.randint(35, 45) if i % 57 == 0 else np.random.randint(0, 85) if i % 59 == 0 else np.random.randint(65, 100) for i in range(num_rows)]),
+    'Network Activity (MB/s)': np.array([np.random.randint(1010, 1050) if i % 3000 == 0  else np.random.randint(377, 597) if i % 23 == 0 else np.random.randint(0, 1000) if i % 19 == 0 else np.random.randint(0, 450) if i % 57 == 0 else np.random.randint(200, 1000) if i % 59 == 0 else np.random.randint(0, 1000) for i in range(num_rows)]),
     'System Average Load (%)': np.random.randint(0, 100, size=num_rows),
     'Battery Level (%)': np.random.randint(0, 100, size=num_rows),
     'App Count': np.random.randint(1, 60, size=num_rows),
     'Background Processes': np.random.randint(1, 50, size=num_rows),
-    'GPU Usage (%)': np.array([np.random.randint(101, 500) if i % 2500 == 0 else "" if i % 1200 == 0 else np.random.randint(0, 100) for i in range(num_rows)]),
-    'Temperature (°C)': np.array([np.random.randint(150, 200) if i % 6000 == 0 else np.random.randint(30, 100) for i in range(num_rows)]),
+    'GPU Usage (%)': np.array([np.random.randint(101, 500) if i % 2500 == 0 else "" if i % 1200 == 0 else np.random.randint(23, 53) if i % 23 == 0 else np.random.randint(0, 100) if i % 19 == 0 else np.random.randint(5, 65) if i % 77 == 0 else np.random.randint(20, 100) if i % 59 == 0 else np.random.randint(0, 100) for i in range(num_rows)]),
+    'Temperature (°C)': np.array([np.round(np.random.uniform(150, 200), 3) if i % 6000 == 0 else np.round(np.random.uniform(20,50), 3) if i % 23 == 0 else np.round(np.random.uniform(23,73), 3) if i % 17 == 0 else np.round(np.random.uniform(30, 100), 3) for i in range(num_rows)]),
     'Storage Available (GB)': np.random.randint(0, 500, size=num_rows),
     'Recent App': np.random.choice(['Amazon', 'Spotify', 'Netflix', 'Youtube', 'Tiktok', 'Snapchat', 'Twitter', 'Instagram', 'WhatsApp', 'Facebook', 'Audible', 'Candy Crush Saga', 'Signal', 'Reddit'], size=num_rows),
     'Screen Brightness (%)': np.random.randint(0, 100, size=num_rows),
@@ -44,9 +43,9 @@ df['System Crash (Yes/No)'] = np.where(
 )
 
 random_rows = df.sample(n=1000, random_state=25)
-df = df.append(random_rows, ignore_index=True)
+df = pd.concat([df, random_rows])
 
 # Save to CSV
-df.to_csv('device_crash_dataset.csv', index=False)
+df.to_csv('../../eda/device_crash_dataset.csv', index=False)
  
-print("Dataset generated and saved as 'device_crash_dataset.csv'.")
+print("Dataset generated and saved as '../../eda/device_crash_dataset.csv'.")
diff --git a/eda/crash_data_eda.py b/eda/crash_data_eda.py
index 5bf22ce..da6c686 100644
--- a/eda/crash_data_eda.py
+++ b/eda/crash_data_eda.py
@@ -22,22 +22,25 @@ print(df.describe())
 print ("======================= NULL  ================================")
 print(df.isnull().sum())
 
+print ("======================= DUPLICATES  ================================")
+print(df[df.duplicated()])
+
 print ("======================= HISTOGRAM  ================================")
-sns.histplot(df["CPU Usage (%)"], bins=15)
+sns.histplot(df["CPU Usage (%)"], bins=70)
 plt.title("CPU USAGE HISTOGRAM")
 plt.show()
-sns.histplot(df["Memory Usage (MB)"], bins = 15)
+sns.histplot(df["Memory Usage (MB)"], bins = 70)
 plt.title("MEMORY USAGE HISTOGRAM")
 plt.show()
-sns.histplot(df["Disk Usage (%)"], bins = 15)
+sns.histplot(df["Disk Usage (%)"], bins = 70)
 plt.title("DISK USAGE HISTOGRAM")
 plt.show()
-sns.histplot(df["Network Activity (MB/s)"], bins = 15)
+sns.histplot(df["Network Activity (MB/s)"], bins = 70)
 plt.title("NETWORK USAGE HISTOGRAM")
 plt.show()
-sns.histplot(df["Temperature (°C)"], bins = 15)
-plt.title("NETWORK USAGE HISTOGRAM")
+sns.histplot(df["Temperature (°C)"], bins = 100)
+plt.title("Temperature HISTOGRAM")
 plt.show()
-sns.histplot(df["GPU Usage (%)"], bins = 15)
-plt.title("NETWORK USAGE HISTOGRAM")
+sns.histplot(df["GPU Usage (%)"], bins = 70)
+plt.title("GPU USAGE HISTOGRAM")
 plt.show()