import os
import sys
import json
import subprocess
import random

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

mode = sys.argv[1] if len(sys.argv) > 1 else 'random'

if mode == 'random':
    index = random.randint(0, len(all_walls) - 1)
elif mode == 'next':
    index = (index + 1) % len(all_walls)
elif mode == 'prev':
    index = (index - 1) % len(all_walls)
else:
    index = (index + 1) % 2

wall_name = all_walls[index]
subprocess.run(['swww', 'img', walls_path + wall_name, '--transition-type=wipe', '--transition-duration=2'])

with open(wall_config_path, 'w') as f:
    f.write('{"index": %d}' % index)
    f.close()
