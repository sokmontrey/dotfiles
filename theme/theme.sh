#!/bin/bash

# load theme.json
theme=$(cat theme.json)

# get theme.special field
special=$(echo $theme | jq -r '.special')
colors=$(echo $theme | jq -r '.colors')

colors_field=("black" "red" "green" "yellow" "blue" "magenta" "cyan" "white")
primary_field=("background" "foreground")
normal_field=("color0" "color1" "color2" "color3" "color4" "color5" "color6" "color7")
bright_field=("color8" "color9" "color10" "color11" "color12" "color13" "color14" "color15")

toml_result=""
toml_result+="[colors.primary]\n"
for i in "${!primary_field[@]}"; do
  field=${primary_field[$i]}
  value=$(echo $special | jq -r '.'$field)
  toml_result+="$field = \"$value\"\n"
done

toml_result+="\n[colors.normal]\n"
for i in "${!normal_field[@]}"; do
  field=${normal_field[$i]}
  value=$(echo $colors | jq -r '.'$field)
  toml_result+="${colors_field[$i]} = \"$value\"\n"
done

toml_result+="\n[colors.bright]\n"
for i in "${!bright_field[@]}"; do
  field=${bright_field[$i]}
  value=$(echo $colors | jq -r '.'$field)
  toml_result+="${colors_field[$i]} = \"$value\"\n"
done

echo -e $toml_result > theme.toml

css_result=""
css_prefix="pm"
for i in "${!primary_field[@]}"; do
  field=${primary_field[$i]}
  value=$(echo $special | jq -r '.'$field)
  css_result+="@define-color $css_prefix-$field $value;\n"
done

css_prefix="nm"
for i in "${!normal_field[@]}"; do
  field=${normal_field[$i]}
  value=$(echo $colors | jq -r '.'$field)
  css_result+="@define-color $css_prefix-${colors_field[$i]} $value;\n"
done

css_prefix="br"
for i in "${!bright_field[@]}"; do
  field=${bright_field[$i]}
  value=$(echo $colors | jq -r '.'$field)
  css_result+="@define-color $css_prefix-${colors_field[$i]} $value;\n"
done

echo -e $css_result > theme.css
