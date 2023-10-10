#importing the required libraries
from matplotlib import pyplot as plt

def plot_five_graph(aquired_data, updated_values): #Defining the function which plots the graph with all the data
     # fields and also their mean values which gets updated every 10 seconds.

    # The required data is extracted and stored to respective variables.
    y_data_2 = aquired_data[0]
    Y_data_3 = aquired_data[1]
    y_data_4 = aquired_data[2]
    mean_pmi1 = aquired_data[3]
    mean_pmi2 = aquired_data[4]
    mean_pmi10 = aquired_data[5]
    data_temperature = aquired_data[6]
    data_humidity = aquired_data[7]

    #To calculate the mean of temperature and humidity to be plotted on the graph.
    mean_temp = sum(updated_values[0]) / len(updated_values[0])
    mean_humi = sum(updated_values[1]) / len(updated_values[1])

    x_data = range(0, 100) # The range is given as the graph is to be plotted for every 100 values in the list.

    plt.subplot(5, 1, 1) # Defining the position of the graph.
    plt.plot(x_data, y_data_2, 'ro-', marker=".", markersize=5) #To plot the values on the graph with the size and color
    # parameters.
    plt.title('PM 1.0 Graph', {'fontsize' :10})
    plt.ylabel('ATM')
    plt.hlines([mean_pmi1], 0, 100, color='blue') #To plot the mean line on the same graph.


    plt.subplot(5, 1, 2) # Defining the position of the graph.
    plt.plot(x_data, Y_data_3, 'ko-.', marker=".", markersize=5) #To plot the values on the graph with the size and color
    # parameters.
    plt.title('PM 2.5 Graph', {'fontsize' :10})
    plt.ylabel('ATM')
    plt.hlines([mean_pmi2], 0, 100, color='blue') #To plot the mean line on the same graph.

    plt.subplot(5, 1, 3) # Defining the position of the graph.
    plt.plot(x_data, y_data_4, 'yo-.', marker=".", markersize=5) #To plot the values on the graph with the size and color
    # parameters.
    plt.title('PM 10.0 Graph', {'fontsize' :10})
    plt.ylabel('ATM')
    plt.hlines([mean_pmi10], 0, 100, color='blue') #To plot the mean line on the same graph.

    plt.subplot(5, 1, 4) # Defining the position of the graph.
    plt.plot(x_data, data_temperature, 'co-.', marker=".", markersize=5) #To plot the values on the graph with the size
    # and color parameters.
    plt.ylabel('Temperature')
    plt.title('Temperature Graph', {'fontsize' :10})
    plt.hlines([mean_temp], 0, 100, color='blue') #To plot the mean line on the same graph.

    plt.subplot(5, 1, 5) # Defining the position of the graph.
    plt.plot(x_data, data_humidity, 'bo-.', marker=".", markersize=5) #To plot the values on the graph with the size and
    # color parameters.
    plt.title('Humidity Graph', fontdict = {'fontsize' :10})
    plt.ylabel('Humidity')
    plt.hlines([mean_humi], 0, 100, color='blue') #To plot the mean line on the same graph.

    plt.subplots_adjust(left=0.125,
                         bottom=0.05,
                         right=0.9,
                         top=0.95,
                         wspace=1,
                         hspace=1.2)

    plt.show() #Displays the graph iteratively with the available data at that point of time on screen.