# turns off bluelight filter

import subprocess

# Function to increase screen temperature (decrease blue light filter)
def increase_temp():
    subprocess.call(['xrandr', '--output', 'eDP-1', '--gamma', '1:1:1'])

# Function to decrease screen temperature (increase blue light filter)
def decrease_temp():
    subprocess.call(['xrandr', '--output', 'eDP-1', '--gamma', '1.2:1:1'])

# Function to reset screen temperature to default
def reset_temp():
    subprocess.call(['xrandr', '--output', 'eDP-1', '--gamma', '1:1:1'])

# Call decrease_temp(), increase_temp(), or reset_temp() based on your preference
# Example: reset_temp()
reset_temp()
