# Embedded-Air-Quality-Measurement-System
This repository contains the code for an embedded Air Quality Index (AQI) measurement system. The system reads and visualizes atmospheric data saved in cloud storage while also measuring local temperature and humidity using a Raspberry Pi-based Pitrokli system. The code calculates the AQI using the available data and writes it to a cloud server, where it is graphically visualized. The Pitrokli system displays mean values of the measurements using a 7-segment display and provides graphical representations using a matrix LED display.

# Components
## Hardware Components
1. Raspberry Pi (with internet connectivity)
2. Pitrokli Sensor
3. 7-segment display (Adafruit 7-segment display)
4. LED matrix display (MAX7219)
5. Buttons for user interface
## Software Components
1. Python (3.x)
2. Libraries for Pitrokli sensor, 7-segment display, and LED matrix display
3. Thingspeak for cloud data storage and visualization

# Installation and Usage
Clone this repository to your Raspberry Pi:

bash
git clone https://github.com/your-username/air-quality-measurement.git
- Install the required Python libraries:
> pip install thingspeak
> pip install matplotlib
> pip install adafruit-led-backpack
> pip install luma.core

Configure your Thingspeak account and obtain the necessary API key.

Modify the config.py file with your Thingspeak channel ID and API key.

Run the main program:
python main.py
The program will continuously collect data from the cloud, measure local temperature and humidity, calculate the AQI, and display the data on the 7-segment display and LED matrix.

### Files
> main.py: The main program that orchestrates data collection, local measurements, and display.
> data_initialise.py: Reads data from the Thingspeak cloud.
> temp_hum_measure.py: Measures local temperature and humidity using the Pitrokli sensor.
> fifo.py: Implements a First-In-First-Out (FIFO) mechanism to update local temperature and humidity data.
> plot_five_graph.py: Plots a graph of atmospheric data and updates it every 10 seconds.
> user_interface1.py: Controls the user interface with buttons and displays data on the 7-segment display and LED matrix.
> aqi_measure.py: Calculates the Air Quality Index (AQI) and writes it to Thingspeak.

# Acknowledgments
This project was developed as a collaborative effort and benefited from discussions and contributions from Syamraj Satheesh Kumar.
