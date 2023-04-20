from pyconnector import connect_to_database
from select_data import select
from insert_data import insert
from update_data import update
from delt_data import delete

mydb = connect_to_database()

insert_choose = input("--------What do you want to do?? Pls choose------- \n 1.Insert\n 2.Update\n 3.Select\n 4.Delete\n Input here : ")
if insert_choose.lower() == "insert":
    insert()
elif insert_choose.lower() == "update":
    update()
elif insert_choose.lower() == "select":
    select()
elif insert_choose.lower() == "delete":
    delete()   
else:
    print ("Iced Americano")

    
