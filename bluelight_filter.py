# run this file with python3 bluelight_filter.py 
import subprocess

# Function to increase screen temperature (decrease blue light filter)
def increase_temp():
    subprocess.call(['xrandr', '--output', 'eDP-1', '--gamma', '1:1:1'])

# Function to decrease screen temperature (increase blue light filter)
def decrease_temp():
    subprocess.call(['xrandr', '--output', 'eDP-1', '--gamma', '1.2:1:1'])

# Call decrease_temp() or increase_temp() based on your preference
decrease_temp()
