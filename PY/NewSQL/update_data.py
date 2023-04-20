from pyconnector import connect_to_database

mydb = connect_to_database()
mycursor = mydb.cursor()

def update():
    update_query = "UPDATE dafood SET food_Name = %s, country_F = %s, food_Price = %s WHERE food_ID = %s"
    continue_update = True
    
    while continue_update:
        food_ID = input("Enter the food ID to update: ")
        food_name = input("Enter the new food name: ")
        country_F = input("Enter the new food country: ")
        food_Price = input("Enter the new food price: ")
        values = (food_name, country_F, food_Price, food_ID)
        
        mycursor.execute(update_query, values)
        mydb.commit()
        print(mycursor.rowcount, "record(s) updated")
        
        update_confirmation = input("Do you want to update another record? (y/n)")
        if update_confirmation.lower() != "y":
            continue_update = False
            print("Update operation cancelled.")
