from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///example.db")  # this is creating engine that connect with database ,however it only connect with database when query is executed 

conn = engine.connect() # conn is used to execute queries 

# creating a table 
conn.execute(text( """ 
Create Table IF NOT EXISTS users(
             id Integer Primary key,
             Name String var(20),
             Email String
             )
"""))
 
# inserting value in database 
conn.execute(text("""
    Insert into users(id, Name, Email)
    Values (4, 'Prince', 'PRINCE@gmail.com'),(2, 'Prince', 'PRINCE@gmail.com'),(3, 'Prince', 'PRINCE@gmail.com')
"""))

# reading value in database
results = conn.execute(text("""
Select * from users
"""))
for row in results:
    print(row)
''' 

# querry for deleting table completly 
conn.execute(text("""
    Drop Table users
"""))
 '''