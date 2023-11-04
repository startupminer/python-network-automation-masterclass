print ('Virquan')
with open('devices.txt') as file:
    # read each line and split into a list item
    content = file.readline().splitlines()
    print(content)
    # create empty object
    devices = list()
    # loop over content
    for line in content:  # all content
        # separate each line of string data by ':' and append item to new list of devices
        devices.append(line.splitlines(':'))

    for line in content[1:]:  # start at index of 1
        # separate each line of string data by ':' and append item to new list of devices
        devices.append(line.splitlines(':'))

    print(devices)
