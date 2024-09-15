# __NBA Win-Loss Predictor for the Golden State Warriors__  

Contributors: Saahil Vohra and Sachith Chandran

### __Table of Contents__
* Introduction
* Features
* Modeling Approach
* Technologies Used
* Evaluation & Results
* Future Improvements
* Installation
* Usage
* Contributing
* License

### __Introduction__
The NBA Win-Loss Predictor is a machine learning project designed to forecast the regular season win-loss record of the Golden State Warriors for the 2024-25 NBA season. Using historical game data and team statistics, the project aims to predict outcomes for each matchup in the season. This project integrates comprehensive data collection, robust preprocessing, detailed feature engineering, and a Random Forest Classifier model to produce precise predictions.

This project focuses on enhancing predictive accuracy, building on past season data, and simulating potential outcomes for future games.

### __Features__
* Team & Opponent Statistics: Incorporates game stats such as field goals, assists, rebounds, and free throws for both the Warriors and their opponents.
* Historical Data: Utilizes nealrly a decade of historical performance data to enhance predictive power, wihle also adhering to the everchanging style of play.
* Machine Learning Model: A Random Forest Classifier was trained and tested to predict the outcome of each game.
* Win-Loss Simulation: The model simulates the full season and estimates the Warriors' win-loss record at the end of the season.
* Accuracy Benchmark: Achieved a accuracy of 63% when simulating the 2023-24 NBA season, a competitive rate compared to top sports analytics models that perform at 65-66% accuracy.
  
### __Modeling Approach__

##### Data Collection: 
Web scraping NBA game logs from Basketball Reference—the largest basketball data repository—using BeautifulSoup, and then reading the data into a pandas DataFrame.
##### Data Preprocessing:
Cleaning raw data; handling missing values, duplicates, and outliers; and feature engineering (e.g. 3PT% difference).
##### Model Training and Testing: 
Training and Testing a Random Forest Classifier using data from over 500 games.
##### Simulation: 
Simulating the 2023-24 Warriors, and providing game-by-game data to predict their win-loss record based on their schedule and team performance trends. 
##### Evaluation:
Accuracy of the model was evaluated and analyzed using confusion matrices and classification reports.

##### Technologies Used:
* Languages: Python
* Libraries:
  - pandas, numpy, scipy for data manipulation and analysis
  - scikit-learn for machine learning algorithms
  - requests, BeautifulSoup for web scraping and data collection
  - matplotlib, seaborn for data visualization (optional)
* Version Control: Git, GitHub

### Installation:
To run this project locally, follow these steps:

* Clone the repository:
git clone https://github.com/SaahilVohra/nba-win-loss-predictor.git  
cd nba-win-loss-predictor

* Create a virtual environment and activate it:  
python -m venv env  
source env/bin/activate  

* Install dependencies:  
pip install -r requirements.txt  

### Usage:
Once installed, the project can be used to predict the outcomes of future games and simulate the entire Warriors season. 
##### To simulate the season:

* Run the following files:  
  data_gathering.py  
  data_cleaning.py  
  feature_engineering.py  
  training_and_testing.py  

* Run the file 23-24_season_simulator.py:  
  input the relevant data game-by-game
  
### Future Improvements  

Advanced Feature Engineering: Integrating additional features like player injuries, travel fatigue, or team chemistry.  
Algorithm Tuning: Exploring alternative models such as XGBoost or neural networks.  
Incorporating Real-Time Data: Updating the model with real-time data during the NBA season for more dynamic predictions.  
Game Context: Considering in-game factors like clutch performance and foul trouble.  

### Contributing

Contributions are welcome! If you'd like to improve the model, add new features, or report bugs, feel free to:  

Fork the repository.  
Create a new branch.  
Make your changes.  
Submit a pull request.  



