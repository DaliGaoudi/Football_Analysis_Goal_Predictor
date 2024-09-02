import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from PIL import Image
import joblib

def read_csv_to_dataframe(csv_filename):
    try:
        df = pd.read_csv(csv_filename)

        print(df)
        
        return df
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{csv_filename}' is empty.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        return None
    

def train(df):
    ##Data split
    X = df[['x', 'y', 'distance', 'angle', 'defenders_position_x', 'defenders_position_y', 'gk_pos_x', 'gk_pos_y']]
    y = df['goal']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Random Forest Classifier
    model = RandomForestClassifier(class_weight='balanced', random_state=42)
    model.fit(X_train, y_train)


    # Predict on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))

    joblib.dump(model, 'random_forest_model.pk1')
    
    ## uncomment whats below this to see the graphs
    '''
    # Get feature importance from the model
    importance = model.feature_importances_
    features = X.columns

    # Plot the importance of each feature
    plt.barh(features, importance)
    plt.xlabel("Feature Importance")
    plt.title("Feature Importance in Shot Prediction")
    plt.show()
    print("features")
    # Visualize successful vs unsuccessful shots on the pitch
    image_path = "./assets/pitch.png"
    pitch_image = Image.open(image_path)

    fig, ax = plt.subplots(figsize=(10, 7))  

    ax.imshow(pitch_image, extent=[0, 120, 0, 80])

    for i, (index, row) in enumerate(X_test.iterrows()):
        # Color based on prediction
        if y_pred[i] == 1:  # Use i to index y_pred
            ax.scatter(row['x'], row['y'], color='green')  # Green for goals
            print(f"Plotting goal for index {index}")
        else:
            ax.scatter(row['x'], row['y'], color='red')  # Red for misses
            print(f"Plotting miss for index {index}")

    plt.title('Predicted Shot Outcomes')
    plt.show() 
    print("plt is there") '''  

if len(sys.argv) != 2:
    print("Usage: python script_name.py <csv_filename>")
else:
    csv_filename = sys.argv[1]
    df = read_csv_to_dataframe(csv_filename)
    train(df)