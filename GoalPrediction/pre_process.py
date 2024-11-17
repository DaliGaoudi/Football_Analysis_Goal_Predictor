import numpy as np 
import pandas as pd
import json

path = "./matches/3943043.json"

goal_x, goal_y_min, goal_y_max = 120, 36, 44

def distance_to_goal(x,y):
    return np.sqrt((goal_x - x)**2 + (40 - y)**2)

def shot_angle(shot_x, shot_y):
    return np.arctan2(goal_y_max - shot_y, goal_x - shot_x) - np.arctan2(goal_y_min - shot_y, goal_x - shot_x)

def defenders_positions(event):
    surr_players = event.get("shot", "Unknown")["freeze_frame"] 
    defenders = []
    positions = []
    for i, pl in enumerate(surr_players):
        if surr_players[i]["teammate"] == False:
            defenders.append(pl)
    for defender in defenders:
        positions.append(defender.get("location","Unknown"))
    return positions

def average_positions(positions):
    if positions:
        avg_x = sum([pos[0] for pos in positions]) / len(positions)
        avg_y = sum([pos[1] for pos in positions]) / len(positions)
        return avg_x, avg_y
    else:
        return (0,0)    

with open(path, 'r', encoding="utf8") as file:
    game_data = json.load(file)

shot_events = []
for event in game_data:
    if event.get("type" , "Unknown")["name"] == "Shot":
        shot_events.append(event)
''' 
shots_data = [
"pos" : x,y
"distance" : ds
"angle" : an
"defenders_x" : x
"defenders_y" : y
is_goal = bool
"gk_pos_x"  : x
"fk_pos_y" : y
]
''' 

shots_data = []
for event in shot_events:
    shot_id = event.get("id","Unknown")
    shot_x, shot_y = event.get("location" ,"Unknown")
    distance = distance_to_goal(shot_x,shot_y)
    angle = shot_angle(shot_x,shot_y)
    gk_pos_x, gk_pos_y = event.get("shot", "Unknown")["freeze_frame"][0]["location"] 
    is_goal = event.get("shot", "Unknown")["outcome"]["id"] == 97   

    positions = defenders_positions(event)
    avg_x, avg_y = average_positions(positions)


    shots_data.append({
    "x" : shot_x,
    "y" : shot_y,
    "distance" : distance,
    "angle" : angle,
    "defenders_position_x" : avg_x,
    "defenders_position_y" : avg_y,
    "gk_pos_x" : gk_pos_x,
    "gk_pos_y" : gk_pos_y,
    "goal" : 1 if is_goal else 0,
})        

df = pd.DataFrame(shots_data)
csv_filename = path.split(".")[1].replace("/","") + ".csv"
df.to_csv(csv_filename,index=False)
