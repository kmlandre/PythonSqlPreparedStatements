import pymssql # or import pyodbc


# Connect to the target server and database
def getConnection():
    conn = pymssql.connect(
        server='localhost',
        user='testUser',
        ###  DO NOT DO THIS!  ####
        password='1BadPassword!',
        database='TestDb'
    )

    return conn

# This is a better way to do SQL interactions...
def uprightAndDecentCitizenSqlQuery(userInput):
    # Prepare a statement
    goodQueryNiceQuerySitQuery = "SELECT * FROM userInfo WHERE username = %s"
    print("")
    print("QUERY: \n  -- " + goodQueryNiceQuerySitQuery.replace("%s", userInput))

    # Grab a connection and cursor
    conn = getConnection()
    cursor = conn.cursor()

    # Bind parameters and execute
    cursor.execute(goodQueryNiceQuerySitQuery, userInput)

    # Commit the transaction
    results = cursor.fetchall()

    # Congratulations!  You get to keep your job!
    conn.close()

    return results

def printResults(results):
    print("")
    for row in results:
        print(row)

###############################################################
evilUserInput = "' OR '1'='1"

print("")
print("--------------------------------------------------------------------------")
print("Ahh, the land of sweet milk and flower'd honey...")
results = uprightAndDecentCitizenSqlQuery(evilUserInput)
print("                                             ^^^^  Note that the injected structure now parses 'safely'...")
printResults(results)

evilUserInputV2 = "OR '1'='1';"

print("--------------------------------------------------------------------------")
print("Yep.  Still safe.  FOR NOW.....")
results = uprightAndDecentCitizenSqlQuery(evilUserInputV2)
print("                                             ^^^^  Note that the injected structure now parses 'safely'...")

printResults(results)

decentUserInput = "lilbobby"

print("--------------------------------------------------------------------------")
print("But does is *work*?")
results = uprightAndDecentCitizenSqlQuery(decentUserInput)
print("                                             ^^^^  Notice the 'clean' parameter...")

printResults(results)