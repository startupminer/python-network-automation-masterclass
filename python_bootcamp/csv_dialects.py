import csv
# For cases when data has a different character as the delimiter (separation of data)
print('Read data with different delimiters')
with open('passwd.csv') as file:
    # separate line of data by ':' and end on new line
    reader = csv.reader(file, delimiter=':', lineterminator='\n')
    for row in reader:
        print(row)

# dialects describes the properties of a csv file
print(csv.list_dialects())
print('\n##########################\n')
print('Register custom dialects')
# registering custom dialects
csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

# Output data correctly parsed
with open('items.csv', 'r') as file:
    # ref custom dialect
    reader = csv.reader(file, dialect='hashes')
    for row in reader:
        print(row)


print('\n##########################\n')
print('Write to csv file using the delimiter format')
with open('items.csv', 'a') as file:
    writer = csv.writer(file, dialect='hashes')
    writer.writerow(('spoon', 3, 1.5))