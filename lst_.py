l2 = ['rp_B80-90', 'rp_B85', 'rp_18-8 Stainless Steel', 'rp_18-8 Stainless Steel', 'rp_Zinc', 'rp_B80/90']
for x in l2:
    if x == "rp_18-8 Stainless Steel":
        a = x.split(' ')[0]
        b = x.split(' ')[1:]
        print(a)
        # print(b)
        c = ' '.join(b)
        print(c)
print()
for y in l2:
    if y == "rp_B80-90":
        x = y.split('-')[0]
        print(x)
        z = y.split('-')[1]
        print(z)
print()
# split the value of "rp_B80/90"
for j in l2:
    if j == "rp_B80/90":
        p = j.split('-')[0]
        print(p)
print()
for i in l2:
    if i == "rp_B80/90":
        a = i.split('/')[0]
        print(a)
        b = i.split('/')[1]
        print(b)





















































# s = l.count("c")
# print(s)
#
# print(len(l))

# print(l[2][0:7])
# a = l[2][0:-20]
# b = l[2][8:-1]
# print(a + b)
#
# print(l[0])
# print(l[0][0:6])
#
# x = l[0][0:-6]
# y = l[0][7:]
# print(x + y)




