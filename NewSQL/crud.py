from pyconnector import connect_to_database
from select_data import select
from insert_data import insert
from update_data import update

mydb = connect_to_database()

insert_choose = input("--------What do you want to do?? Pls choose------- \n 1.Insert\n 2.Update\n 3.Select\n 4.Delete\n Input here : ")
if insert_choose.lower() == "insert":
    insert()
if insert_choose.lower() == "update":
    update()
if insert_choose.lower() == "select":
    select()
else:
    print 

    
