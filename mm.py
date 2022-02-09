from sqlalchemy import insert, update, select, and_, or_, not_, delete, desc
from db import Base, engine, execute
from models import User, Address

Base.metadata.create_all (engine)

def insert_one_user ():
    query = insert (User).values(name = 'John', fullname = 'John Carter', sex='male', age=50)
    execute (query)

data = [
    {'name':'Alex', 'fullname': 'Alex Vronsky', 'sex':'male', 'age':23},
    {'name':'Anna', 'fullname': 'Anna Karenina', 'sex':'female', 'age':26},
    {'name':'Jane', 'fullname': 'Jane Austen', 'sex': 'female', 'age': 35},
    {'name':'Mary', 'fullname': 'Mary Skladovska', 'sex': 'female', 'age':20},
    {'name':'Emily', 'fullname': 'Emily Dickinson', 'sex': 'female', 'age':18},
    {'name':'Arthur', 'fullname': 'Arthur Burton', 'sex': 'male', 'age':18},
    {'name':'Paul', 'fullname': 'Paul Sartr', 'sex': 'male', 'age':40},
    {'name':'Auron', 'fullname': 'Auron S', 'sex': 'male', 'age':5},
    {'name':'Ares', 'fullname': 'Ares Greek', 'sex': 'male', 'age':50},
    {'name':'Apollo', 'fullname': 'Apollo Greek', 'sex': 'male', 'age':60}
] 
 
def insert_many_users ():
    query = insert (User)
    execute (query, data)

#insert_many_users()

#def insert_addresses ():
#    with engine.connect() as conn:
#        conn.execute(insert(Address)
#            .values (email_address = 'john@barsun', user_id = 1))
#            .values (email_address = 'alex@barsun', user_id = 2))
#            .values (email_address = 'anna@barsun', user_id = 3))
#            .values (email_address = 'jane@barsun', user_id = 4))
#            .values (email_address = 'mary@barsun', user_id = 5))
#            .values (email_address = 'emily@barsun', user_id = 6))
#            .values (email_address = 'arthur@barsun', user_id = 7))
#            .values (email_address = 'paul@barsun', user_id = 8))
#insert_addresses()




def select_users():
    query = (
        select (User.name, User.age, User.sex)
            .where(
                User.name.like('A%') |
                User.name.like ('L%') 
            )
            .where(
                User.sex == 'male'
            )
            .limit (3)
            .order_by(User.age.desc())
    )
    with engine.connect() as conn:
        cursor = conn.execute(query)
        users = list (cursor)
    for user in users:
        print (dict(user))
select_users()


