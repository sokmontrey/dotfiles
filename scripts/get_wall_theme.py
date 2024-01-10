import os
import sys
import json
import subprocess

walls_path = os.path.expanduser('~/download/wallpaper/')
all_walls = os.listdir(walls_path)

index = 0
wall_config_path = os.path.expanduser('~/.config/scripts/wallpaper_index.json')
if not os.path.exists(wall_config_path):
    with open(wall_config_path, 'w') as f:
        f.write('{"index": 0}')
        f.close()
else:
    with open(wall_config_path, 'r') as f:
        index = json.load(f)['index']
        f.close()

wall_name = all_walls[index]
theme_path = os.path.expanduser('~/.config/themes/')
subprocess.run(['wpg', '-a', walls_path + wall_name])
subprocess.run(['wpg', '-o', wall_name, theme_path + 'raw_wall_theme.json'])
