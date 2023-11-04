import csv


print('Parse devices data')
with open('devices.txt', 'r') as file:
    content = file.read().splitlines()
    devices = list()
    for item in content:
        # split by delimiter into a list
        tmp = item.split(':')
        devices.append(tmp)
    print(devices)

# utilize csv module
print('\n##########################\n')
print('Parse devices data')
with open('devices.txt', 'r') as file:
    reader = csv.reader(file, delimiter=':')
    devices = list()
    for row in reader:
        devices.append(row)
    print(devices)