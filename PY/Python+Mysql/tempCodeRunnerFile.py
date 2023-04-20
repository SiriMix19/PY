# INSERT DATA TO DATABASE
# insert_query = "INSERT INTO dafood (food_ID, food_Name, country_F, food_Price) VALUES (%s, %s, %s, %s)"
# insert_values = ("DF05", "Pad HongKong", "HongKong", "47.00")
# insert_confirmation = input("Do you want to insert a new record? (y/n)")
# if insert_confirmation.lower() == "y":
#     mycursor.execute(insert_query, insert_values)
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted.")
# else:
#     print("Insert operation cancelled.")