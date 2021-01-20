import sqlite3

conn = sqlite3.connect("data.db")

c=conn.cursor()
#c.execute("DROP TABLE Extracted")
c.execute("Select * from Extracted")

#data = c.fetchall()
#print(data)

for row in c:
    print('{0}, {1}'.format(row[0].encode("UTF-8"), row[1].encode("UTF-8")))
    print("****************************************************")