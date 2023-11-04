import csv
print('Write row of csv data')
with open('people.csv', 'a') as csvfile:
    # write function from csv module that converts data into delimited string and stores in an object
    writer = csv.writer(csvfile)
    # tuple
    csvData = (5, 'Anne', 'Amsterdam')
    # new row will be added to csv file
    writer.writerow(csvData)
print('\n##########################\n')
print('Output rows of manipulated numbers data')
# Open file in write mode and create this number.csv file
# newline is optional arg that by default is \n so explicitly set to empty string
with open('numbers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Add first row header
    # x , x^2 , x^3, x^4, x^5
    writer.writerow(['x', 'x**2', 'x**3', 'x**4', 'x**5'])
    # Loop to add row of numbers from 1 - 100
    # (1 is included and 101 is not included)
    for x in range(1, 101):
        writer.writerow([x, x**2, x**3, x**4])