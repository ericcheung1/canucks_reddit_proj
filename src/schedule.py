import os
import pandas as pd
import datetime as dt

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
schedule = pd.read_csv(os.path.join(project_root, 'data', 'van_schedule24_25.csv'))
schedule.columns = ['GP', 'Date', 'Time', 'Home/Away', 'Opponent']
schedule['Datetime_str'] = schedule['Date'].astype(str) + ' ' + schedule['Time'].astype(str)
schedule['Eastern_Timestamp'] = pd.to_datetime(schedule['Datetime_str'], format='%Y-%m-%d %I:%M %p').dt.tz_localize('US/Eastern')
schedule['Local_Time'] = schedule['Eastern_Timestamp'].dt.tz_convert('US/Pacific').dt.strftime('%I:%M %p')
schedule['UTC_Timestamp'] = schedule['Eastern_Timestamp'].dt.tz_convert('UTC')
schedule['Home/Away'] = schedule['Home/Away'].fillna('Vs.')
schedule['Year'] = schedule['Eastern_Timestamp'].dt.year
schedule['Month'] = schedule['Eastern_Timestamp'].dt.strftime('%b')
schedule['Day'] = schedule['Eastern_Timestamp'].dt.strftime('%d')
# print(schedule.sample(5))
cleaned_schedule = schedule[['GP', 'Day', 'Month', 'Year', 'UTC_Timestamp', 'Date', 'Local_Time', 'Home/Away', 'Opponent']].copy()
print(cleaned_schedule.sample(5))
cleaned_schedule.to_csv(os.path.join(project_root, 'data', 'formatted_van_schedule24_25.csv'), index=False)