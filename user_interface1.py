#importing the required libraries
import time
import statistics
from Adafruit_LED_Backpack import SevenSegment
import wiringpi as WiPi
# Importing the SPI communication protocol
from luma.core.interface.serial import spi, noop
# import the class which specifies the MAX7219 driver element
from luma.led_matrix.device import max7219
# Import the convas object we use for drawing
from luma.core.render import canvas


# Define serial connection
serial = spi(port=0, device=1, gpio=noop())
# Define device Max7219
device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)

counter = 0 #Defining a global variable
def user_interface1(initial_data, current_atmospheric_values,start):
    # Create a new 7SD instance with the I2C address 0x70
    my_seven_segment = SevenSegment.SevenSegment(address=0x70)
    # Initialise 7SD
    my_seven_segment.begin()

    # Definition of Pins of PI-Trokli system: Here the directional buttons
    PinButtonLeft = 25
    PinButtonRight = 19

    # Define an array with all input pins
    GPIOInputPins = [PinButtonLeft, PinButtonRight]

    # Defining that we want to use the GPIO (BCM) numberings system
    WiPi.wiringPiSetupGpio()

    # Iterate through all elements of the GPIOInputPins array
    for CurrentPin in GPIOInputPins:
        # Defining that we want to utilise the defined input pins as input
        WiPi.pinMode(CurrentPin, 0)
        # Deactivating PullUp/PullDown resistance
        WiPi.pullUpDnControl(CurrentPin, 0)

    global counter #Calling global variable

    # The required data is extracted and stored to respective variables.
    data_pmi1 = initial_data[0]
    data_pmi2 = initial_data[1]
    data_pmi10 = initial_data[2]
    temp_for_graph = current_atmospheric_values[0]
    hum_for_graph = current_atmospheric_values[1]

    #Calculating mean of temperature and humidity.
    mean_temp = statistics.mean(temp_for_graph)
    mean_humidity = statistics.mean(hum_for_graph)

    # Saving all the data required for plotting in a new list for easier access.
    graph_values = [data_pmi1, data_pmi2, data_pmi10, temp_for_graph, hum_for_graph]

    #Converting the digits to string format, rounding the value to nearest 1 decimal point, removing '.',
    # filling the remaining digit space with 0 in the front.
    mean_pmi1 = str(round(initial_data[3],1)).replace(".", "").zfill(5)
    mean_pmi2 = str(round(initial_data[4],1)).replace(".", "").zfill(5)
    mean_pmi10 = str(round(initial_data[5],1)).replace(".", "").zfill(5)
    temperature = str(round(mean_temp,1)).replace(".", "").replace(" ", "").replace("C", "").zfill(4)
    humidity = str(round(mean_humidity, 1)).replace(".", "").zfill(4)

    # Saving all the data in a new list for easier access to display on 7SD.
    mean_values = [mean_pmi1, mean_pmi2, mean_pmi10, temperature, humidity]

    list01 = [0, 1, 2, 3, 4, 5, 6, 7] # New list to select the co-ordinate while plotting the graph in the LED Matrix.

    graph_values_scale = [] #List to store the scaled mean values for the graph
    for i in range(0,5):
        j = 0
        k = 15
        mean_array = []
        while k < 100: # while loop to store the mean values and save to 'mean_array'.
            mean = statistics.mean(graph_values[i][j:k]) #To find mean of list with given parameters.
            j += 12
            k += 12
            mean_array.append(mean)
        max_value = max(mean_array) # Finding maximum value in the mean array to use while scaling the values.

        j = 0
        k = 15
        scale_array = []
        while k < 100: # while loop to scale the mean value with respect to the maximum value and saving in 'scale_array'.
            mean = int(statistics.mean(data_pmi1[j:k]))
            j += 12
            k += 12
            scale = int(round(5 * (mean / max_value))) #Scaling in a way that the system uses only 5 rows of the LED
            # Matrix display from the bottom.
            scale_array.append(scale)

        graph_values_scale.append(scale_array)

    interval = 5 #Initializin g a random initial value to the variable.
    while interval < 10:

        if not WiPi.digitalRead(PinButtonLeft) and counter != 0:
            counter = counter - 1
            # Showing which pin was read before

        if not WiPi.digitalRead(PinButtonRight) and counter != 4:
            counter = counter + 1
            # Showing which pin was read before

        time.sleep(0.3) #Small time delay so that the system distinguishes between each button presses.

        digit = 0
        for my_character in mean_values[counter]:
            # Writing a digit of the 7SD
            my_seven_segment.set_digit(digit, my_character)
            my_seven_segment.set_decimal(2, True)
            digit = digit + 1

        # Write all elements to 7SD
        my_seven_segment.write_display()

        with canvas(device) as draw: #To plot the graph on the LED matrix display according to the coordinate.
            draw.point((counter, 0), fill="white")
            for (i, j) in zip(list01, graph_values_scale[counter]):
                draw.point((i, 7 - j), fill="white")

        end = time.time() #To record the end time of the function
        interval = int(end - start) #To measure the difference between start and end time so that the code runs
        # continuously for 10 seconds while being inside the main loop.

