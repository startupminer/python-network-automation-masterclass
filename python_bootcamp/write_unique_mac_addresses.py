with open('macs.txt', 'r') as file:
    content = file.read().split()
# Eliminate duplicates
content = list(set(content))
print(content)
# write to new file
with open('macs_unique.txt', 'w', newline='') as file:
    for x in content:
        file.write(f'{x}\n')
