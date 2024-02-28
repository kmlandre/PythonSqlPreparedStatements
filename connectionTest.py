import pymssql # or import pyodbc

# Connect to the target server and database
conn = pymssql.connect(
    server='localhost',
    user='testUser',
    ###  DO NOT DO THIS!  ####
    password='1BadPassword!',
    database='TestDb'
)

# We're going to create a cursor, which is
# enough to prove that we've successfully
# connected to the machine
cursor = conn.cursor()

# Close down and clean up our connections...
conn.close()