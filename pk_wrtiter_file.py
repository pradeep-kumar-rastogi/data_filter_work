import csv

with open('Student12.csv', 'w', newline='')as sd:
    student = csv.writer(sd)
    student.writerow(["S_Id", "Name", "Email", "Address", "Mobile_No",  " city","new_city"])
    student.writerow([1, "Shani", "shani@gmail.con", "varanasi", "969696548"])
    student.writerow([2, "rahul", "rk@gmail.con", "Jaunpur", "969632548"])
    student.writerow([3, "ashwin", "ak@gmail.con", "mughal sarai", "923656548"])
    student.writerow([4, "amit", "amot@gmail.con", "Jaunpur", "96969231548"])
    student.writerow([5, "saurabh", "sa21@gmail.con", "Babat pur", "9696965332"])
    student.writerow([6, "vikash", "vikas2@gmail.con", "ram nagar ", "9696965418"])
    student.writerow([7, "pradeep", "pk@gmail.con", "ghazipur", "9696962654"])
    student.writerow([8, "narendra", "nk5@gmail.con", "varanasi", "9696926540"])
    student.writerow([9, "abhishek", "abho@gmail.con", "jagat gang vns", "96969651201"])
    student.writerow([10, "mohit", "powni@gmail.con", "Mirzapur", "969696596"])
    print(student)

