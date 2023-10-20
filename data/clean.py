import pandas as pd

# Load the dataset
df = pd.read_csv('cleaned_who_road_deaths.csv')

# Drop the 'Time' column
df.drop('Time', axis=1, inplace=True)

# Save the dataframe back to the CSV, overwriting it
df.to_csv('cleaned_who_road_deaths.csv', index=False)

print("Time column removed and file saved!")
