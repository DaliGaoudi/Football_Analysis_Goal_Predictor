import joblib
import pandas as pd

# Load the trainde model using pickle
model = joblib.load('random_forest_modelEDA.pk1')

new_shot = [[114.5,37.5,6.041522986797286,1.1347914444368148,110.81428571428572,36.92857142857143,109.4,42.9]]


new_shot_df = pd.DataFrame(new_shot, columns=['x', 'y', 'distance', 'angle', 'defenders_position_x', 'defenders_position_y', 'gk_pos_x', 'gk_pos_y'])

prediction = model.predict(new_shot_df)
print(f"Prediction: {'Goal' if prediction[0] == 1 else 'No Goal'}")

probabilities = model.predict_proba(new_shot_df)
print(probabilities)
print(prediction)

goal_probability = probabilities[0][1]  
print(f"Probability of goal: {goal_probability:.2f}")