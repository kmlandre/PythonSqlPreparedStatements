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

# This is the naughty way of doing things
def evilSqlQuery(evilUserInput):
    # Allow the bubbling goo of existential dread to wash over your soul...
    evilSql = "SELECT * FROM userInfo WHERE username = '" + evilUserInput + "';"
    print("")
    print("QUERY: \n  -- " + evilSql)

    # Prepare to send yourself on a journey from whence none shall return...
    # Grab a connection and cursor
    conn = getConnection()
    cursor = conn.cursor()

    # Shove in whatever horrors we may have been handed...
    cursor.execute(evilSql)

    # Remember the good times, oh youth!
    # For ye shall nae see such again,
    # Not in the twist of this helixed fate!
    results = cursor.fetchall()

    #          ____
    #        _/    \_
    #      _/        \_
    #    _/    RIP     \_
    #   /________________\
    #   |                |
    #   | Oh, such a day |
    #   | was grief      |
    #   | unfurled, with |
    #   | careless data  |
    #   | put cruelly in |
    #   | this world...  |
    #   |________________|

    # Close down the connection...
    conn.close()

    # Send back the package of doom and gloom you have just created...
    return results

# Just a quick utility method to display the contents of our results...
def printResults(results):
    print("")
    for row in results:
        print(row)

###############################################################
# Main driving bits...
###############################################################

# This is an injectable 'parameter', which you should notice is
# intentionally malformed (note the imbalanced single quote chars)...
evilUserInput = "' OR '1'='1"

# "Mom!  Dad!  Don't touch it!  It's *EVIL*!"
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("LOOK WHAT EVIL HATH BEEN WRAUGHT!")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
evilResults = evilSqlQuery(evilUserInput)
print("                                             ^^^^  Note the 'new' structure of the injection parameter!")
# Display our output...
printResults(evilResults)

