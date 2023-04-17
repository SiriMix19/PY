import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="food",
)
mycursor = mydb.cursor()

# INSERT DATA TO DATABASE
insert_query = "INSERT INTO dafood (food_ID, food_Name, country_F, food_Price) VALUES (%s, %s, %s, %s)"
insert_values = ("DF04", "Pad Turkey", "Turkey", "45.00")
insert_confirmation = input("Do you want to insert a new record? (y/n)")
if insert_confirmation.lower() == "y":
    mycursor.execute(insert_query, insert_values)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
else:
    print("Insert operation cancelled.")

# SELECT DATA FROM DATABASE
select_query = "SELECT * FROM dafood"
select_confirmation = input("Do you want to select all records? (y/n)")
if select_confirmation.lower() == "y":
    mycursor.execute(select_query)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
else:
    print("Select operation cancelled.")

# UPDATE DATA TO DATABASE
update_query = "UPDATE dafood SET food_Name = 'Pad China' WHERE food_Name = 'Pad Englan'"
update_confirmation = input("Do you want to update a record? (y/n)")
if update_confirmation.lower() == "y":
    mycursor.execute(update_query)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
else:
    print("Update operation cancelled.")

# DELETE DATA FROM DATABASE
delete_query = "DELETE FROM dafood WHERE food_Name = 'Pad Turkey'"
delete_confirmation = input("Do you want to delete a record? (y/n)")
if delete_confirmation.lower() == "y":
    mycursor.execute(delete_query)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
else:
    print("Delete operation cancelled.")
