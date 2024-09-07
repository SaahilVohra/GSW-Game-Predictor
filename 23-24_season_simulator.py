import pandas as pd
from collections import deque
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

model = joblib.load('nba_model.pkl')
print(type(model))

### Model trained, now time to work on new (unseen) data.

# Load warriors 22-23 season
season_2022_23_data = pd.read_csv('warriors_22-23_season.csv')

# Only want the warriors' stats from last 20 games
last_20_games = season_2022_23_data[['Warriors FG%', 'Warriors 3P%', 'Warriors FT Made', 'Warriors TRB', 'Warriors AST', 'Warriors STL', 'Warriors BLK', 'Warriors TOV', 'Warriors PF']].tail(20)

recent_games = deque(maxlen=20)

for index, game in last_20_games.iterrows():
    recent_games.append(game)

predictions = []
actuals = []

# Load warriors stats for 23-24 season
full_warriors_stats_df = pd.read_csv('warriors_23-24_season.csv')

for game_index in range(82):
    # Input opponent data as a comma-separated string
    opponent_input = input(f"Game {game_index + 1} - Enter opponent stats as a comma-separated string (FG%, 3P%, FT Made, TRB, AST, STL, BLK, TOV, PF): ")
    #convert string to a list of floats
    opponent_data_list = list(map(float, opponent_input.split(',')))
    
    # Opponent data taken from list above
    opponent_data = {
        'Opp FG%': opponent_data_list[0],
        'Opp 3P%': opponent_data_list[1],
        'Opp FT Made': opponent_data_list[2],
        'Opp TRB': opponent_data_list[3],
        'Opp AST': opponent_data_list[4],
        'Opp STL': opponent_data_list[5],
        'Opp BLK': opponent_data_list[6],
        'Opp TOV': opponent_data_list[7],
        'Opp PF': opponent_data_list[8],
    }

    # Compute rolling averages of the last 20 games for the Warriors
    rolling_averages = pd.DataFrame(recent_games).mean()

    # Get the stats for the current game
    current_game_stats = full_warriors_stats_df.iloc[game_index]

    # add current game stats to dictionary
    full_warriors_stats = {
        'Warriors FG%': current_game_stats['Warriors FG%'],
        'Warriors 3P%': current_game_stats['Warriors 3P%'],
        'Warriors FT Made': current_game_stats['Warriors FT Made'],
        'Warriors TRB': current_game_stats['Warriors TRB'],
        'Warriors AST': current_game_stats['Warriors AST'],
        'Warriors STL': current_game_stats['Warriors STL'],
        'Warriors BLK': current_game_stats['Warriors BLK'],
        'Warriors TOV': current_game_stats['Warriors TOV'],
        'Warriors PF': current_game_stats['Warriors PF'],
    }

    # Calculate differences
    differences = {
        'FG% Difference': rolling_averages['Warriors FG%'] - opponent_data['Opp FG%'],
        '3P% Difference': rolling_averages['Warriors 3P%'] - opponent_data['Opp 3P%'],
        'FT Made Difference': rolling_averages['Warriors FT Made'] - opponent_data['Opp FT Made'],
        'TRB Difference': rolling_averages['Warriors TRB'] - opponent_data['Opp TRB'],
        'AST Difference': rolling_averages['Warriors AST'] - opponent_data['Opp AST'],
        'STL Difference': rolling_averages['Warriors STL'] - opponent_data['Opp STL'],
        'BLK Difference': rolling_averages['Warriors BLK'] - opponent_data['Opp BLK'],
        'TOV Difference': rolling_averages['Warriors TOV'] - opponent_data['Opp TOV'],
        'PF Difference': rolling_averages['Warriors PF'] - opponent_data['Opp PF'],
    }

    # Convert the differences data into a DataFrame for prediction
    input_df = pd.DataFrame([differences])

    #print(input_df)

    # Predict the outcome of the current game
    prediction = model.predict(input_df)[0]
    print('Prediction: ' + str(prediction))

    # Store the prediction
    predictions.append(prediction)

    # After prediction, manually input the actual result
    actual_result = int(input(f"Game {game_index + 1} - Actual Win/Loss (1 for win, 0 for loss): "))
    actuals.append(actual_result)

    # Update stack with the new game stats
    recent_games.append(pd.Series(full_warriors_stats))

    #calculate and print accuracy after each game
    accuracy = accuracy_score(actuals, predictions)
    print(f"Model Accuracy on 2023-24 Season: {accuracy * 100:.2f}%")

# After the loop, calculate total accuracy of the model
accuracy = accuracy_score(actuals, predictions)

# Print the list of predictions vs actual results
print("Predictions vs Actual Results:")
for i, (pred, actual) in enumerate(zip(predictions, actuals)):
    print(f"Game {i+1}: Prediction = {pred}, Actual = {actual}")

# Print the final accuracy
print(f"Model Accuracy on 2023-24 Season: {accuracy * 100:.2f}%")


# Generate confusion matrix
conf_matrix = confusion_matrix(actuals, predictions)
print("\nConfusion Matrix:")
print(conf_matrix)

# Generate classification report
class_report = classification_report(actuals, predictions, target_names=['Loss', 'Win'])
print("\nClassification Report:")
print(class_report)
