from pyconnector import connect_to_database
def update():
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    update_query = "UPDATE dafood SET food_Name = %s WHERE food_Name = %s"
    update_confirmation = input("Do you want to update a record? (y/n)")

    if update_confirmation.lower() == "y":
        food_name = input("Enter the new food name: ")
        old_food_name = input("Enter the old food name: ")
        values = (food_name, old_food_name)
        mycursor.execute(update_query, values)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
    else:
        print("Update operation cancelled.")