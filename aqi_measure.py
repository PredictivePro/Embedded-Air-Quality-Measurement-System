#importing the required libraries
import thingspeak

def aqi_measure(initial_data): # Defining function to measure AQI values and write to thingspeak.

    #Extracting data from 'initial_data' and saving it into respective variables.
    pmi2 = initial_data[1]
    pmi10 = initial_data[2]
    aqi_array2 = []
    aqi_array10 = []
    aqi_max = []

    #Loop to iterate through every PMI values and do associated calculation according to the parameters.
    for i in range(0, 100, 1):
        if pmi2[i] >= 0 and pmi2[i] <= 12:
            h_minus_l = 50
            lpm2 = 12
            aqi2 = (h_minus_l / lpm2) * (pmi2[i] )
            aqi_array2.append(round(aqi2,2))

        elif pmi2[i] > 12 and pmi2[i] <= 35.4:
            h_minus_l = 49
            lpm2 = 23.3
            aqi2 = (h_minus_l / lpm2) * (pmi2[i] - (12.1)) + 51
            aqi_array2.append(round(aqi2,2))

        elif pmi2[i] > 35.4 and pmi2[i] <= 55.4:
            h_minus_l = 49
            lpm2 = 19.9
            aqi2 = (h_minus_l / lpm2) * (pmi2[i] - (35.5)) + 101
            aqi_array2.append(round(aqi2,2))

        elif pmi2[i] > 55.4 and pmi2[i] <= 150.4:
            h_minus_l = 49
            lpm2 = 94.9
            aqi2 = (h_minus_l / lpm2) * (pmi2[i] - (55.5)) + 151
            aqi_array2.append(round(aqi2,2))

        elif pmi2[i] > 150.4 and pmi2[i] <= 250.4:
            h_minus_l = 99
            lpm2 = 99.9
            aqi2 = (h_minus_l / lpm2) * (pmi2[i] - (150.5)) + 201
            aqi_array2.append(round(aqi2,2))

        elif pmi2[i] > 250.4 and pmi2[i] <= 350.4:
            h_minus_l = 99
            lpm2 = 99.9
            aqi2 = (h_minus_l / lpm2) * (pmi2[i] - (250.5)) + 301
            aqi_array2.append(round(aqi2,2))

        elif pmi2[i] > 350.4 and pmi2[i] <= 500.4:
            h_minus_l = 49
            lpm2 = 149.9
            aqi2 = (h_minus_l / lpm2) * (pmi2[i] - (350.5)) + 401
            aqi_array2.append(round(aqi2,2))

        else:
            print('Incorrect data')

    for i in range(0, 100, 1):
        if pmi10[i] >= 0 and pmi10[i] <= 54:
            h_minus_l = 50
            lpm2 = 54
            aqi10 = (h_minus_l / lpm2) * (pmi10[i] )
            aqi_array10.append(round(aqi10,2))

        elif pmi10[i] >= 55 and pmi10[i] <= 154:
            h_minus_l = 49
            lpm2 = 99
            aqi10 = (h_minus_l / lpm2) * (pmi10[i] - (12.1)) + 51
            aqi_array10.append(round(aqi10,2))

        elif pmi10[i] >= 155 and pmi10[i] <= 254:
            h_minus_l = 49
            lpm2 = 99
            aqi10 = (h_minus_l / lpm2) * (pmi10[i] - (35.5)) + 101
            aqi_array10.append(round(aqi10,2))

        elif pmi10[i] >= 255 and pmi10[i] <= 354:
            h_minus_l = 49
            lpm2 = 99
            aqi10 = (h_minus_l / lpm2) * (pmi10[i] - (55.5)) + 151
            aqi_array10.append(round(aqi10,2))

        elif pmi10[i] >= 355 and pmi10[i] <= 424:
            h_minus_l = 99
            lpm2 = 69
            aqi10 = (h_minus_l / lpm2) * (pmi10[i] - (150.5)) + 201
            aqi_array10.append(round(aqi10,2))

        elif pmi10[i] >= 425 and pmi10[i] <= 504:
            h_minus_l = 99
            lpm2 = 79
            aqi10 = (h_minus_l / lpm2) * (pmi10[i] - (250.5)) + 301
            aqi_array10.append(round(aqi10,2))

        elif pmi10[i] >= 505 and pmi10[i] <= 604:
            h_minus_l = 49
            lpm2 = 99
            aqi10 = (h_minus_l / lpm2) * (pmi10[i] - (350.5)) + 401
            aqi_array10.append(round(aqi10,2))

        else:
            print('Incorrect data')


    #To find the largest value among PMI 2.5 and PMI 10 at a given time.
    for (two, ten) in zip(aqi_array2, aqi_array10):
        aqi_max.append((max(two, ten)))


    channel_id = 1835082
    write_key = 'CJWYU448LWVZS0G0'
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    channel.update({'field1': aqi_array2[-1], 'field2': aqi_array10[-1], 'field3': aqi_max[-1]}) #Writing the values to
    #thingspeak cloud server.


