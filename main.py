import csv
with open(r'C:\Users\Harish\Downloads\check_data.csv', 'r') as f:
    data = csv.reader(f)
    for row in data:
        entity_id = row[0]
        l3_name = row[1]
        model_no = row[2]
        attr_name = row[3]
        attr_value = row[4]
        b = []
        if attr_name == 'Drop-In Anchor Type':
            a = 'Type'
            new_attr_name = a
            new_attr_value = attr_value
            print(new_attr_name, "=", new_attr_value)
        elif attr_name == 'Anchor Length':
            a = 'Length'
            new_attr_name = a
            new_attr_value = attr_value
            print(new_attr_name, "=", new_attr_value)
        elif attr_name == 'Ultimate Shear in 4000 PSI Concrete (Lb.)' and attr_value == 'rp_3714':
            a = 'Ultimate Shear'
            new_attr_name = a
            new_attr_value = attr_value + " "+"lbs."
            print(new_attr_name, "=", new_attr_value)
