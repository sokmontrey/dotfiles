import json 
import os
import sys

theme_path = os.path.expanduser('~/.config/themes/')
current_theme_file = open(theme_path + 'current_theme.json', 'r')
theme = json.load(current_theme_file)

# waybar 
waybar_path = os.path.expanduser('~/.config/waybar/theme.css')
'''
waybar format:
@define-color key1-key2 value
'''
waybar_css = ''
for i in theme['primary']:
    waybar_css += '@define-color ' + 'primary-' + i + ' ' + theme['primary'][i] + ';\n'
for i in theme['normal']:
    waybar_css += '@define-color ' + 'normal-' + i + ' ' + theme['normal'][i] + ';\n'
for i in theme['bright']:
    waybar_css += '@define-color ' + 'bright-' + i + ' ' + theme['bright'][i] + ';\n'

with open(waybar_path, 'w') as f:
    f.write(waybar_css)
    f.close()

# alacritty
alacritty_path = os.path.expanduser('~/.config/alacritty/theme.toml')
'''
alacritty format:
[colors.key1]
key2 = value
'''
alacritty_toml = ''
alacritty_toml += '[colors.primary]\n'
for i in theme['primary']:
    alacritty_toml += i + ' = "' + theme['primary'][i] + '"\n'
alacritty_toml += '\n[colors.normal]\n'
for i in theme['normal']:
    alacritty_toml += i + ' = "' + theme['normal'][i] + '"\n'
alacritty_toml += '\n[colors.bright]\n'
for i in theme['bright']:
    alacritty_toml += i + ' = "' + theme['bright'][i] + '"\n'

with open(alacritty_path, 'w') as f:
    f.write(alacritty_toml)
    f.close()

