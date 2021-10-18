
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "Infortech"
)

mycursor = mydb.cursor()
mycursor.execute("""USE Infortech""")