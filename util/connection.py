import psycopg2

# Global constant
PSQL_HOST = "localhost"
PSQL_PORT = "3306"
PSQL_USER = "root"
PSQL_PASS = ""
PSQL_DB_NAME = ""

# Connection
connection_address = """
host=%s port=%s user=%s password=%s dbname=%s
""" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB_NAME)
connection = psycopg2.connect(connection_address)

cursor = connection.cursor()

# Query

SQL = "SELECT * FROM ;"
cursor.execute(SQL)

# Get Values
all_values = cursor.fetchall()

cursor.close()
connection.close()

print("Get values: ", all_values)