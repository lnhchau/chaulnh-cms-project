import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=sqlserverchau.database.windows.net;DATABASE=sqlchau;UID=chaulnh;PWD=pass@12345678')
cursor = conn.cursor()
cursor.execute('SELECT 1')
print(cursor.fetchone())
