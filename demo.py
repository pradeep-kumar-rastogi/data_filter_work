import csv
with open(r'C:/Users/harish/downloads/check_data.csv', 'r') as f:
    data = csv.reader(f)
    for row in data:
        entity_id = row[0]
        l3_name = row[1]
        model_no = row[2]
        attr_name = row[3]
        attr_value = row[4]
    if attr_value == "rp_18-8 Stainless Steel":  # There are two rows with attr_value = rp_18-8 Stainless Steel
        x = attr_value.replace('18-8', '')
        print(x)
        a = attr_value.replace('rp_', '')
        b = a.split(' ')[0]
        c = "rp_Grade "
        print(c + b)
        print(b)

