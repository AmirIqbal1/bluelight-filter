Bluelight Filter
=================

This is a simple blue light filter app for Linux Mint with Cinnamon desktop. The app uses the `xrandr` command to adjust the color temperature of the screen to a warmer temperature that reduces blue light.

Installation
------------

1. Clone the repository to your local machine:

```bash
git clone https://github.com/AmirIqbal1/bluelight-filter.git
```

2. Navigate to the cloned repository:

```bash
cd bluelight-filter-app
```

3. Install the required dependencies:

```bash
sudo apt-get install xrandr
```

4. Run the app:

```bash
python3 bluelight_filter.py
```

Usage
-----

The app provides two functions:

* `increase_temp()`: Increases the screen temperature (decreases the blue light filter)
* `decrease_temp()`: Decreases the screen temperature (increases the blue light filter)

To use the app, simply call one of the functions. For example, to decrease the screen temperature, you can call the `decrease_temp()` function:

```python
decrease_temp()
```

# Startup Script Automatically

To start the blue light filter app automatically when your system starts up, you can create a startup command.

1. Open "Startup Applications"

2. `python3 /path/to/bluelight_filter.py`

3. Replace `/path/to/bluelight_filter.py` with the actual path to the `bluelight_filter.py` script.

4. Log out your system to test the startup script.

   
