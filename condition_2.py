import csv
with open(r'C:\Users\Harish\Downloads\check_data.csv', 'r') as f:
    data = csv.reader(f)
    for row in data:
        entity_id = row[0]
        l3_name = row[1]
        model_no = row[2]
        attr_name = row[3]
        attr_value = row[4]
    if attr_name == 'Anchor Length':
        y = 'Length'
        new_attr_name = y
        new_attr_value = attr_value
        print(new_attr_name, "=", new_attr_value)