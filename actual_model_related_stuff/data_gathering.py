import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

def get_season_data(season_year):
    url = f'https://www.basketball-reference.com/teams/GSW/{season_year}/gamelog/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    table = soup.find('table', {'id': 'tgl_basic'})
        
    table_str = str(table)
    table_io = StringIO(table_str)
    
    game_log = pd.read_html(table_io)[0]
    
    # Print column names to check
    #print(f'Columns for {season_year}:', game_log.columns)

    selected_columns = [
        ('Unnamed: 5_level_0', 'W/L'), 
        ('Team', 'FG%'), 
        ('Team', '3P%'), 
        ('Team', 'FT'), 
        ('Team', 'TRB'), 
        ('Team', 'AST'), 
        ('Team', 'STL'), 
        ('Team', 'BLK'), 
        ('Team', 'TOV'), 
        ('Team', 'PF'),
        ('Opponent', 'FG%'), 
        ('Opponent', '3P%'), 
        ('Opponent', 'FT'), 
        ('Opponent', 'TRB'), 
        ('Opponent', 'AST'), 
        ('Opponent', 'STL'), 
        ('Opponent', 'BLK'), 
        ('Opponent', 'TOV'), 
        ('Opponent', 'PF')
    ]
    
    game_log = game_log[selected_columns]
    
    # Rename columns for clarity
    game_log.columns = [
        'Win/Loss', 
        'Warriors FG%', 'Warriors 3P%', 'Warriors FT Made', 'Warriors TRB', 'Warriors AST', 'Warriors STL', 'Warriors BLK', 'Warriors TOV', 'Warriors PF',
        'Opp FG%', 'Opp 3P%', 'Opp FT Made', 'Opp TRB', 'Opp AST', 'Opp STL', 'Opp BLK', 'Opp TOV', 'Opp PF'
    ]
    
    # Convert 'W/L' column to binary format
    game_log[('Win/Loss')] = game_log[('Win/Loss')].apply(lambda x: 1 if x == 'W' else 0)

    return game_log

# List of seasons to collect data for
seasons = [ '2018', '2019', '2020', '2021', '2022', '2023']
all_seasons_data = []

for season in seasons:
    season_data = get_season_data(season)
    if season_data is not None:
        all_seasons_data.append(season_data)

# Check if data collection was successful
if all_seasons_data:
    # Combine all seasons' data into one df and save to csv file
    combined_data = pd.concat(all_seasons_data, ignore_index=True)
    combined_data.to_csv('warriors_all_seasons_gamelog_with_opponents.csv', index=False)

    print('Data collection complete')
else:
    print('No data collected')
