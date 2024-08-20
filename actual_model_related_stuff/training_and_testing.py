from feature_engineering import cleaned_data, features, target 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Split the data into training and testing sets 
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)


# Initialize an instance of the Random Forest Classifier model (100 decision trees)
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight = 'balanced')

# Train model
model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Print classification report
report = classification_report(y_test, y_pred)
print('Classification Report:')
print(report)

# Print confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)

#save model
joblib.dump(model, 'nba_model.pkl')