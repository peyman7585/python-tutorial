
import csv
import json
# file = open('example.txt', 'w')
# file.write("this test.\nfor us")

# file = open('example.txt', 'r')
#  print(file.read())
# file.close()


with open("example_write.txt", mode='w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['Alice', '23', 'NewYork'])

with open("example_write.txt", mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)


data = {
    'Name': 'Rogue',
    'Age': 24,
    'City': 'orgimar'
}

with open("example_json.txt", mode='w') as jsonFile:
    json.dump(data, jsonFile)

with open("example_json.txt", mode='r') as jsonFiles:
    data = json.load(jsonFiles)
    print(data)
