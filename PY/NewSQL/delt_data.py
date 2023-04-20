from pyconnector import connect_to_database
mydb = connect_to_database()
mycursor = mydb.cursor()

def delete():
    delete_query = "DELETE FROM dafood WHERE food_ID = %s"
    delete_confirmation = input("Do you want to delete a record? (y/n)")

    if delete_confirmation.lower() == "y":
        food_ID = input("Enter the food ID to be deleted: ")
        values = (food_ID,)
        delete_confirmation = input("Do you sure to want to delete a record? (y/n)")
        if delete_confirmation.lower() == "y":
            mycursor.execute(delete_query, values)
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted")
        else:
            print("Delete operation cancelled.")
    else:
        print("Delete operation cancelled.")
