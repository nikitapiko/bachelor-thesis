import re
import pandas as pd

# Path to your Robot Framework log file
log_file_path = 'output.xml'

# Initialize an empty list to store headlines
headlines_data = []

# Regular expression to capture the headline and URL
pattern = re.compile(r'(.*?) - (https?://[^\s]+)')

# Open and read the log file
with open(log_file_path, 'r') as file:
    for line in file:
        # Look for lines that contain headline and URL
        match = pattern.search(line)
        if match:
            headline_text = match.group(1).strip()
            headline_url = match.group(2).strip()
            # Append to the list
            headlines_data.append({'newsHeadline': headline_text, 'URL': headline_url})

# Create a DataFrame from the list
df = pd.DataFrame(headlines_data)

# Save to CSV
output_csv_path = 'headlines.csv'
df.to_csv(output_csv_path, index=False)

print(f"Headlines have been saved to {output_csv_path}")
