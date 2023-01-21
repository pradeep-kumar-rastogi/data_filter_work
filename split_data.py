file_data = ["rp_1/4-20", "rp_1/4-20", "rp_5/8-11", "rp_5/8-11", "rp_5/8-11", "rp_5/8-11", "rp_1/2-13", "rp_1/2-13",
             "rp_M16x2", "rp_M18x2.5", "rp_M20x2.5", "rp_M24x3", 'rp_M27x3', "rp_M33x3.5", "rp_M36x4"]
for data in file_data:
    if 'x' in data:
        a = data.split('x')[0]
        b = data.split('x')[1]
        print(a)
        print(b)
    elif '-' in data:
        x = data.split('-')[0]
        b = data.split('-')[1]
        print(b)
        print(x)
