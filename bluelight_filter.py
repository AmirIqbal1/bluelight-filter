import subprocess

# Function to increase screen temperature (decrease blue light filter)
def increase_temp():
    # Adjust gamma values for a warmer tone
    subprocess.call(['xrandr', '--output', 'eDP-1', '--gamma', '1.3:1:0.8'])

# Function to decrease screen temperature (increase blue light filter)
def decrease_temp():
    # Adjust gamma values for a slightly warmer tone
    subprocess.call(['xrandr', '--output', 'eDP-1', '--gamma', '1.2:1:0.9'])

# Call decrease_temp() or increase_temp() based on your preference
increase_temp()  # Change to increase_temp() for a warmer screen
