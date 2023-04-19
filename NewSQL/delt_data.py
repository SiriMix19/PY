from pyconnector import connect_to_database
mydb = connect_to_database()
mycursor = mydb.cursor()

def delete():
    delete_query = "DELETE FROM dafood WHERE food_Name = 'Pad Turkey'"
    delete_confirmation = input("Do you want to delete a record? (y/n)")
    if delete_confirmation.lower() == "y":
        mycursor.execute(delete_query)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
    else:
        print("Delete operation cancelled.")
