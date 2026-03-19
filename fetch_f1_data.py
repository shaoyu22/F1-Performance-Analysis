import requests
import pandas as pd
import os

# 1. Configuration (Setup the parameters)
# Purpose: Define target race details to keep the code organized and easy to modify.
YEAR = 2024
LOCATION = 'Japan'
SESSION = 'Race'

def main():
    # 2. Step 1: Get the Session Key
    # Purpose: Connect to the API to retrieve the unique ID for the 2024 Japan Grand Prix.
    session_url = "https://api.openf1.org/v1/sessions"
    session_params = {'year': YEAR, 'country_name': LOCATION, 'session_name': SESSION}
    
    print(f"--- Searching for {YEAR} {LOCATION} Session Key ---")
    session_res = requests.get(session_url, params=session_params)
    
    if session_res.status_code == 200 and session_res.json():
        session_key = session_res.json()[0]['session_key']
        print(f"Success! Session Key: {session_key}")
        
        # 3. Step 2: Fetch Lap Data
        # Purpose: Use the retrieved Key to download detailed lap times and sector performance.
        laps_url = f"https://api.openf1.org/v1/laps?session_key={session_key}"
        print(f"--- Fetching Lap Data from API ---")
        laps_res = requests.get(laps_url)
        
        if laps_res.status_code == 200:
            # 4. Step 3: Convert to DataFrame and Save
            # Purpose: Transform raw JSON into a table and save it as a CSV for our analysis.
            df = pd.DataFrame(laps_res.json())
            
            # Create data folder if it doesn't exist (Local environment safety)
            if not os.path.exists('data'):
                os.makedirs('data')
                
            df.to_csv('data/japan_2024_laps.csv', index=False)
            print(f"Done! File saved to data/japan_2024_laps.csv")
            print(f"Total Laps Recorded: {len(df)}")
        else:
            print("Failed to fetch lap data.")
    else:
        print("Could not find the session.")

if __name__ == "__main__":
    main()
