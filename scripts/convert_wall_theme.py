import json
import os
import sys

theme_path = os.path.expanduser('~/.config/themes/')

raw_theme_file = open(theme_path + 'raw_wall_theme.json', 'r')
raw_wall_theme = json.load(raw_theme_file)

wall_theme = {}
wall_theme['primary'] = {}
wall_theme['primary']['background'] = raw_wall_theme['special']['background']
wall_theme['primary']['foreground'] = raw_wall_theme['special']['foreground']
wall_theme['normal'] = {}
wall_theme['bright'] = {}

raw_colors = raw_wall_theme['colors']
raw_keys = list(raw_colors.keys())
standard_keys = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
for i in range(len(standard_keys)):
    wall_theme['normal'][standard_keys[i]] = raw_colors[raw_keys[i]]
    wall_theme['bright'][standard_keys[i]] = raw_colors[raw_keys[i + 8]]

with open(theme_path + 'current_theme.json', 'w') as f:
    f.write(json.dumps(wall_theme))
    f.close()
