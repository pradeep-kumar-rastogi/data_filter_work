# if s == product_title_new.lower().strip():
#                 res1 = "Same"
#                 print(res1)
#                 sql = "UPDATE mip_data_check SET product_title_test = '" + str(
#                     res1) + "' WHERE product_url='" + str(product_url) + "'"
#                 mycursor.execute(sql)
#                 mydb.commit()
#                 print(mycursor.rowcount, "record updated.")
#             else:
#                 res2 = "Different"
#                 print(res2)
#                 sql = "UPDATE mip_data_check SET product_title_test = '" + str(
#                     res2) + "' WHERE product_url='" + str(product_url) + "'"
#                 mycursor.execute(sql)
#                 mydb.commit()
#                 print(mycursor.rowcount, "record updated.")


# if add_name == title_page:
#     var1 = "Same values Found in databases"
#     # print(var1)
#     ps = "UPDATE real_tits_dba63 SET product_title_test = 'var1'"
#     result.execute(ps)
#     obj1.commit()
#     print(mycursor.rowcount, "record(s) affected")
# else:
#     var2 = "Different values Found in Databases"
#     print(var2)
#     sqlyog = "UPDATE real_tits_dba63 SET product_title_test = 'var2'"
#     result.execute(sqlyog)
#     print(mycursor.rowcount, "record(s) affected")
#     # print(result)
#     obj1.commit()
