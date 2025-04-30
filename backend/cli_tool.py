from database import get_connection

db = get_connection()

print(db.dialect)
print(db.get_table_info())
print(db.run("SELECT * FROM Artist LIMIT 10;"))