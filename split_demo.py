l2 = ['rp_B80-90', 'rp_B85', 'rp_18-8 Stainless Steel', 'rp_18-8 Stainless Steel', 'rp_Zinc', 'rp_B80/90']
for x in l2:
    if x == "rp_18-8 Stainless Steel":
        a = x.split(' ')[0]
        b = x.split(' ')[1:]
        print(a)
        c = ' '.join(b)
        print(c)
    elif x == "rp_B80-90":
        y = x.split('-')[0]
        print(y)
        z = x.split('-')[1]
        print(z)
    elif x == "rp_B80/90":
        a = x.split('/')[0]
        print(a)
        b = x.split('/')[1]
        print(b)
