import json
import matplotlib.pyplot as plt
from PIL import Image

path = "./matches/3943043.json" 

with open(path, 'r', encoding="utf8") as file:
    game_data = json.load(file)

events = []
for event in game_data:
    event_type = event.get('type', 'Unknown')
    timestamp = event.get('timestamp','Unknown')
    if event_type["name"] == "Pass":
        player = event.get('player', 'Unknown')["name"]
        try:
            recipient = event.get('pass', 'Unknown')["recipient"]["name"]
            events.append(event)  
        except KeyError:
            pass

count = 0
player_passes = []
for event in events:
    if event.get('player','Unknown')["id"] == 316046:
        player_passes.append(event)
        print("yamal passed")
        count = count + 1
print(count)


pitch_img = "./assets/pitch.png"

pitch_image = Image.open(pitch_img)

fig, ax = plt.subplots(figsize=(10, 7))

ax.imshow(pitch_image, extent=[0, 120, 0, 80])

for pas in player_passes:
    start_x, start_y = pas.get("location", "Unknown")
    end_x, end_y = pas.get("pass", "Unknown")["end_location"]
    ax.arrow(start_x, start_y, end_x - start_x, end_y - start_y, head_width=1, head_length=1, fc='red', ec='red')

ax.set_xlim(0, 120)
ax.set_ylim(0, 80)

plt.show()    
