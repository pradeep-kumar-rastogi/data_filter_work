# working on csv file to find rp_Stainless Steel and replace Grade

import csv
with open(r'C:\Users\Harish\Downloads\l3_data_work.csv', 'r')as file_data:
    data = csv.reader(file_data)
    for row in data:
        entity_id = row[0]
        mpn = row[0]
        L3_entity_name = row[2]
        attribute_name = row[3]
        attribute_value = row[4]
        if attribute_value == "rp_18-8 Stainless Steel":
            x = attribute_value.replace('18-8', '')
            print(x)
            a = attribute_value.replace('rp_', '')
            b = a.split(' ')[0]
            c = "rp_Grade "
            print(c+b)
            # print(b)

