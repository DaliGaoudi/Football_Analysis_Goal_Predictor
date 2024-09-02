import joblib
import pandas as pd

model = joblib.load('random_forest_model.pk1')

new_shot = [[115.0, 36.0, 10.2, 10.0, 108.3, 0.2, 120.0, 40.0]]

new_shot_df = pd.DataFrame(new_shot, columns=['x', 'y', 'distance', 'angle', 'defenders_position_x', 'defenders_position_y', 'gk_pos_x', 'gk_pos_y'])

prediction = model.predict(new_shot_df)
print(f"Prediction: {'Goal' if prediction[0] == 1 else 'No Goal'}")