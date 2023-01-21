import csv
with open(r'C:\Users\Harish\Downloads\l3_data_work.csv', 'r') as file_data:
    data = csv.reader(file_data)
    for row in data:
        entity_id = row[0]
        model_no = row[1]
        L3_entity_name = row[2]
        attribute_name = row[3]
        attribute_value = row[4]
        # print(entity_id)
        if attribute_value == "rp_18-8 Stainless Steel":
            # a = attribute_value.split('_')[0]
            b = attribute_value.split(' ')[1:]
            c = ''.join(b)
            print("rp_", c)
            x = attribute_value.replace('rp_', '')
            y = x.split(' ')[0]
            c = "Grade "
            d = 'rp_' + c+y
            print(d)
