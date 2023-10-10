#importing the required libraries
from matplotlib import pyplot as plt

def plot_graph(aquired_data): #Defining the function which plots the initial graph with the initial values of PMI.

    #The required data is extracted and stored to respective variables.
    y_data_2 = aquired_data[0]
    Y_data_3 = aquired_data[1]
    y_data_4 = aquired_data[2]
    mean_pmi1 = aquired_data[3]
    mean_pmi2 = aquired_data[4]
    mean_pmi10 = aquired_data[5]

    x_data = range(0, 100) # The range is given as the graph is to be plotted for every 100 values in the list.


    plt.subplot(3, 1, 1) # Defining the position of the graph.
    plt.plot(x_data, y_data_2, 'ro-', marker=".", markersize=5) #To plot the values on the graph with the size and color
    # parameters.
    plt.title('PM 1.0 Graph', {'fontsize': 10})
    plt.ylabel('ATM')
    plt.xlabel('Sample')
    plt.hlines([mean_pmi1], 0, 100, color='blue') #To plot the mean line on the same graph.

    plt.subplot(3, 1, 2) # Defining the position of the graph.
    plt.plot(x_data, Y_data_3, 'ko-.', marker=".", markersize=5) #To plot the values on the graph with the size and color
    # parameters.
    plt.title('PM 2.5 Graph', {'fontsize': 10})
    plt.ylabel('ATM')
    plt.xlabel('Sample')
    plt.hlines([mean_pmi2], 0, 100, color='blue') #To plot the mean line on the same graph.

    plt.subplot(3, 1, 3) # Defining the position of the graph.
    plt.plot(x_data, y_data_4, 'yo-.', marker=".", markersize=5) #To plot the values on the graph with the size and color
    # parameters.
    plt.title('PM 10.0 Graph', {'fontsize': 10})
    plt.ylabel('ATM')
    plt.xlabel('Sample')
    plt.hlines([mean_pmi10], 0, 100, color='blue') #To plot the mean line on the same graph.

    plt.subplots_adjust(left=0.125,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.2,
                        hspace=.8)

    plt.show() #Displays the graph iteratively with the available data at that point of time.