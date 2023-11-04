import csv
print('Use built-in reader')
with open('airtravel.csv') as f:
    # reader function from csv used to read the file
    # returns an iterable object
    reader = csv.reader(f)
    for row in reader:
        # print content of file line by line
        print(row)

print('\n##########################\n')
print('Print second row of object for each item')
with open('airtravel.csv') as f:
    reader = csv.reader(f)
    # skip the first line
    next(reader)
    for row in reader:
        # print only the second row
        print(row[1])
print('\n##########################\n')
print('Calculate the busiest month in 1958')
with open('airtravel.csv') as f:
    reader = csv.reader(f)
    # skip the first line
    next(reader)
    # create dictionary of year 1958
    year_1958 = dict()
    for row in reader:
        # key:value pair
        year_1958[row[0]] = row[1]
    # print(year_1958)

    # max function gets the maximum value from the dictionary
    # values method returns a list that contains the values of the dictionary

    max_1958 = max(year_1958.values())
    # print(f'Max number of flights for 1958: {max_1958}')

    for k, v in year_1958.items():
        if max_1958 == v:
            # use string method 'strip' to remove whitespaces
            print(f'Busiest month for air travel in 1958: {k}, Flights: {v.strip()}')
print('\n##########################\n')
