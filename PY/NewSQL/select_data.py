from pyconnector import connect_to_database
mydb = connect_to_database()
mycursor = mydb.cursor()
def select():
    select_query = "SELECT * FROM dafood"
    mycursor.execute(select_query)

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)