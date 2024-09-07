from data_cleaning import cleaned_data 

cleaned_data['Warriors FG%'] = cleaned_data['Warriors FG%'] * 100
cleaned_data['Warriors 3P%'] = cleaned_data['Warriors 3P%'] * 100
cleaned_data['Opp FG%'] = cleaned_data['Opp FG%'] * 100
cleaned_data['Opp 3P%'] = cleaned_data['Opp 3P%'] * 100


cleaned_data['FG% Difference'] = cleaned_data['Warriors FG%'] - cleaned_data['Opp FG%']
cleaned_data['3P% Difference'] = cleaned_data['Warriors 3P%'] - cleaned_data['Opp 3P%']
cleaned_data['FT Made Difference'] = cleaned_data['Warriors FT Made'] - cleaned_data['Opp FT Made']
cleaned_data['TRB Difference'] = cleaned_data['Warriors TRB'] - cleaned_data['Opp TRB']
cleaned_data['AST Difference'] = cleaned_data['Warriors AST'] - cleaned_data['Opp AST']
cleaned_data['STL Difference'] = cleaned_data['Warriors STL'] - cleaned_data['Opp STL']
cleaned_data['BLK Difference'] = cleaned_data['Warriors BLK'] - cleaned_data['Opp BLK']
cleaned_data['TOV Difference'] = cleaned_data['Warriors TOV'] - cleaned_data['Opp TOV']
cleaned_data['PF Difference'] = cleaned_data['Warriors PF'] - cleaned_data['Opp PF']

#print(cleaned_data.head())

#Select the final feature set
features = cleaned_data[['FG% Difference', '3P% Difference', 'FT Made Difference', 
                          'TRB Difference', 'AST Difference', 'STL Difference', 'BLK Difference', 
                          'TOV Difference', 'PF Difference']]

# Target variable
target = cleaned_data['Win/Loss']
