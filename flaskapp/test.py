file = int(input('#CSV: '))
data = list()
items = list()

with open(f'gtrends/geoMap{file}.csv', 'r') as f:
    csv = f.read().split('\n')
    for line in csv[3:]:
        data.append(line)

for item in data:
    parts = item.split(',')

    if len(parts) > 1 and parts[1] != '':
        items.append({parts[0]: parts[1]})
    else:
        items.append({parts[0]: '1'})
