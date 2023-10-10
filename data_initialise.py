#importing the required libraries
import thingspeak
import json

def acquire_data(): # Function to read data from the thingspeak channel
    channel_ID = 628559 # Setting thingspeak channel ID
    read_key = '' # Defining read key blank as there is no read key

    #Defining the field numbers
    field_pm1 = 1
    field_pm2 = 2
    field_pm10 = 3
    field_uptime = 4
    field_rssi = 5
    field_temperature = 6
    field_humidity = 7
    field_pmi2_5_cf = 8

    read_channel = thingspeak.Channel(channel_ID, read_key) #Calling the thingspeak function to read the data from the
    # given channel ID

    #Storing data from the thingspeak server to respective variables.
    pmi1 = read_channel.get_field(field_pm1)
    pmi2 = read_channel.get_field(field_pm2)
    pmi10 = read_channel.get_field(field_pm10)
    uptime = read_channel.get_field(field_uptime)
    rssi = read_channel.get_field(field_rssi)
    temperature = read_channel.get_field(field_temperature)
    humidity = read_channel.get_field(field_humidity)
    pmi2_5_cf = read_channel.get_field(field_pmi2_5_cf)

    #The complicated fields from the thingspeak server is simplified using json library into their respective variable.
    json_pmi1 = json.loads(pmi1)
    feeds_pmi1 = json_pmi1['feeds']

    json_pmi2 = json.loads(pmi2)
    feeds_pmi2 = json_pmi2['feeds']

    json_pmi10 = json.loads(pmi10)
    feeds_pmi10 = json_pmi10['feeds']

    json_uptime = json.loads(uptime)
    feeds_uptime = json_uptime['feeds']

    json_rssi = json.loads(rssi)
    feeds_rssi = json_rssi['feeds']

    json_temperature = json.loads(temperature)
    feeds_temperature = json_temperature['feeds']

    json_humidity = json.loads(humidity)
    feeds_humidity = json_humidity['feeds']

    json_pmi2_5_cf = json.loads(pmi2_5_cf)
    feeds_pmi2_5_cf = json_pmi2_5_cf['feeds']


    #The required data from the feeds is extracted and stored into lists.
    data_pmi1 = []
    for i in range(-100, 0 , 1):
        data_pmi1.append(float(feeds_pmi1[i]['field1']))

    data_pmi2 = []
    for i in range(-100, 0, 1):
        data_pmi2.append(float(feeds_pmi2[i]['field2']))

    data_pmi10 = []
    for i in range(-100, 0, 1):
        data_pmi10.append(float(feeds_pmi10[i]['field3']))

    data_uptime = []
    for i in range(-100, 0, 1):
        data_uptime.append(float(feeds_uptime[i]['field4']))

    data_rssi = []
    for i in range(-100, 0, 1):
        data_rssi.append(float(feeds_rssi[i]['field5']))

    data_temperature = []
    for i in range(-100, 0, 1):
        data_temperature.append(float(feeds_temperature[i]['field6']))

    data_humidity = []
    for i in range(-100, 0, 1):
        data_humidity.append(float(feeds_humidity[i]['field7']))

    data_pmi2_5_cf = []
    for i in range(-100, 0, 1):
        data_pmi2_5_cf.append(float(feeds_pmi2_5_cf[i]['field8']))

    # The required data is stored to respective variables to create a list with it. This is list is then easily
    # returned by this function.
    y_data_2 = data_pmi1
    Y_data_3 = data_pmi2
    y_data_4 = data_pmi10
    mean_pmi1 = sum(data_pmi1) / len(data_pmi1)
    mean_pmi2 = sum(data_pmi2) / len(data_pmi2)
    mean_pmi10 = sum(data_pmi10) / len(data_pmi10)
    mean_temp = sum(data_temperature) / len(data_temperature)
    mean_humi = sum(data_humidity) / len(data_humidity)

    # A new list is created with the datas required to be returned
    data_list = [y_data_2, Y_data_3, y_data_4, mean_pmi1, mean_pmi2, mean_pmi10, data_temperature, data_humidity, mean_temp, mean_humi]

    return data_list


