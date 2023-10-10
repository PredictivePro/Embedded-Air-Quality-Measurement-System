def fifo(current_atmospheric_values, initial_temp, initial_humidity): #Defining the function to implement First In First
    # Out concept to update the initial temperature and Humidity list from the thingspeak server with the locally
    #measured temperature and humidity.

    temp_current = current_atmospheric_values[0] # Temperature from Pitrokli sensor is saved to the variable
    # 'temp_current' from the passed parameter.
    hum_current = current_atmospheric_values[1]  # Humidity from Pitrokli sensor is saved to the variable
    # 'hum_current' from the passed parameter.

    initial_temp.pop(0) #The first element at location 0 of the initial temperature list is deleted.
    initial_temp.insert(99, temp_current) # The current temperature is inserted at the end of the list at 99th location.

    initial_humidity.pop(0) #The first element of the initial humidity list at location 0 is deleted.
    initial_humidity.insert(99, hum_current) # The current humidity is inserted at the end of the list at 99th location.

    updated_values = [initial_temp, initial_humidity] # The new values are stored in the form of a list to be returned.

    return updated_values