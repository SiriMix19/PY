from pyconnector import connect_to_database
mydb = connect_to_database()
mycursor = mydb.cursor()

def insert():
    foodId = input("Input your food id : ")
    foodName = input("Input your food name : ")
    foodCT = input("Input your food country : ")
    foodPrice = input("Input your food price : ")

    insert_query = "INSERT INTO dafood (food_ID, food_Name, country_F, food_Price) VALUES (%s, %s, %s, %s)"
    insert_values = (foodId, foodName, foodCT, foodPrice)
    insert_confirmation = input("Do you want to insert a new record? (y/n)")
    if insert_confirmation.lower() == "y":
        mycursor.execute(insert_query, insert_values)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    else:
        print("Insert operation cancelled.")
