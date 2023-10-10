# This program represents the embedded Air Quality Index (AQI) measurement system. It reads and visualize the
# atmospheric data saved in cloud storage while local temperature and humidity is being measured by the PiTrokli system.
# The code further calculates the AQI using the available data and writes it to the cloud server where it is graphically
# visualized. The local Pitrokli system also displays the mean values of the measurements using the 7 segment display
# and graphical representation using the Matrix LED display.


#importing the required libraries
import time

while True:  # While loop is used as the following code needs to be continuously executed every 60 seconds.

    import data_initialise  #importing the function file
    initial_data = data_initialise.acquire_data() # The 'acquire_data' function reads the data from things speak cloud
    # server. This data is stored in the variable 'initial_data'.

    initial_temp = initial_data[6] # The variable 'initial_temp' saves initial temperature from 'initial_data'.
    initial_humidity = initial_data[7] # The variable 'initial_humidity' saves initial humidity from 'initial_data'.

    import Plot_Graph #importing the function file
    Plot_Graph.plot_graph(initial_data) # The 'plot_graph' function plots the initial atmospheric values in graph when
    # 'initial_data' is passed as parameter.

    i = 1 # 'i' is initialized as 1 after every 60 seconds.
    while i%7 != 0: # This while loop will be executed 6 times until coming out of the loop.

        start = time.time() # Measures the start time of the nested while loop.

        import temp_hum_measure #importing the function file
        current_atmospheric_values = temp_hum_measure.measure_temp_hum() # The function 'measure_temp_hum' measures the
        # local temperature and humidity. This data is stored in 'current_atmospheric_values'

        import fifo #importing the function file
        updated_values = fifo.fifo(current_atmospheric_values, initial_temp, initial_humidity) # The function 'fifo'
        # implements the First In First Out concept by appending the latest temperature and humidity to the initial
        # list. For this the current atmospheric data and initial temperature and humidity is passed as parameters.
        # The updated list returned by the function is stored in the variable 'updated_values'

        import plot_five_graph #importing the function file
        plot_five_graph.plot_five_graph(initial_data, updated_values) # The function 'plot_five_graph' plots the graph
        # of the all data from the cloud server. The current temperature and humidity is also passed as parameter
        # which gets updated on the graph every 10 seconds.

        initial_temp = updated_values[0] #The updated temperature list with the local temperature is saved in the
        # variable 'initial_temp'.
        initial_humidity = updated_values[1] #The updated humidity list with the local humidity is saved in the variable
        # 'initial_humidity'.

        import user_interface1 #importing the function file
        user_interface1.user_interface1(initial_data, updated_values,start) # The function 'user_interface1' implements
        # the code to display the graph on LED matrix and the 7 Segment Display. For this the variables initial_data,
        # updated_values, and start are passed as parameters.

        i = i + 1 # 'i' is incremented after every iteration in the nested while loop so that the loop gets executed on
        # 6 times before coming out of the loop and going to the main while loop

    import aqi_measure #importing the function file
    aqi_measure.aqi_measure(initial_data) # The function 'aqi_measure' calculates the Air Quality Index from the
    # available data and also compares AQI level PM2.5 and for PM10.0 to obtain the maximum value at a given time. This
    # function also writes the AQI values and the maximum AQI value to the thingspeak server.


