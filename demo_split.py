a = ["rp_1/4-20", "rp_1/4-20", "rp_5/8-11", "rp_5/8-11", "rp_5/8-11", "rp_5/8-11", "rp_1/2-13", "rp_1/2-13", "rp_M16x2",
     "rp_M18x2.5", "rp_M20x2.5", "rp_M24x3", 'rp_M27x3', "rp_M33x3.5", "rp_M36x4"]
# print(a)
for i in a:
    if i == 'rp_1/4-20':
        a = i.split('-')[0]
        print(a)
        b = i.split('-')[1]
        print(b)
    elif i == "rp_5/8-11":      # output is rp_5/5 and 11
        x = i.split('-')[0]
        print(x)
        y = i.split('-')[1]
        print(y)
    elif i == "rp_1/2-13":
        p = i.split('-')[0]
        print(p)
        q = i.split('-')[1]
        print(q)
    elif i == "rp_M16x2":   # output is rp_M16 and 2
        j = i.split('x')[0]
        print(j)
        k = i.split('x')[1]
        print(k)
    elif i == "rp_M18x2.5":
        j = i.split('x')[0]
        print(j)
        k = i.split('x')[1]
        print(k)
    elif i == "rp_M20x2.5":
        j = i.split('x')[0]
        print(j)
        k = i.split('x')[1]
        print(k)
    elif i == "rp_M24x3":
        j = i.split('x')[0]
        print(j)
        k = i.split('x')[1]
        print(k)
    elif i == "rp_M27x3":
        j = i.split('x')[0]
        print(j)
        k = i.split('x')[1]
        print(k)
    elif i == "rp_M33x3.5":
        j = i.split('x')[0]
        print(j)
        k = i.split('x')[1]
        print(k)
    elif i == "rp_M36x4":
        j = i.split('x')[0]
        print(j)
        k = i.split('x')[1]
        print(k)




