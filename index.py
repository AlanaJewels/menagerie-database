import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Jewels2004!!!'
)

print("Connected to MYSQL Server!")

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)

mycursor.execute("DROP DATABASE IF EXISTS menagerie")
print("Database dropped!")

mycursor.execute("CREATE DATABASE menagerie")
print("Database created!")

mycursor.execute("USE menagerie")
mycursor.execute("""
CREATE TABLE Pet (
    name VARCHAR(20),
    owner VARCHAR(20),
    species VARCHAR(20),
    sex CHAR(1),
    birth DATE,
    death DATE
)
""")
print("Table created!")

mycursor.execute("DESCRIBE pet")
for row in mycursor:
    print(row)

mycursor.execute("""
INSERT INTO pet (name, owner, species, sex, birth, death) VALUES
('Fluffy', 'Harold', 'dog', 'f', '1993-02-04', NULL),
('Claws', 'Gwen', 'cat', 'm', '1994-03-17', NULL),
('Buffy', 'Harold', 'dog', 'f', '1989-05-13', NULL),
('Fang', 'Benny', 'dog', 'm', '1990-08-27', NULL),
('Bowser', 'Diane', 'dog', 'm', '1989-08-31', '1995-07-29'),
('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11', NULL),
('Whistler', 'Gwen', 'bird', NULL, '1997-12-09', NULL),
('Slim', 'Benny', 'snake', 'm', '1996-04-29', NULL),
('Puffball', 'Diane', 'hamster', 'f', '1999-03-30', NULL)
""")
mydb.commit()
print("Records inserted!")

mycursor.execute("SELECT * FROM pet")
for row in mycursor:
    print(row)

mycursor.execute("SELECT * FROM pet WHERE species='dog' AND sex='f'")
for row in mycursor:
    print(row)

mycursor.execute("SELECT name, birth FROM pet")
for row in mycursor:
    print(row)

mycursor.execute("SELECT owner, COUNT(*) AS pet_count FROM pet GROUP BY owner")
for row in mycursor:
    print(row)

query = """
SELECT name, birth, MONTH(birth) AS birth_month
FROM Pet
"""
mycursor.execute(query)

results = mycursor.fetchall()

headers = ["name", "birth", "MONTH(birth)"]

print(tabulate(results, headers=headers, tablefmt="grid"))


query = """
SELECT name, birth, MONTH(birth) AS birth_month
FROM Pet
"""
mycursor.execute(query)
results = mycursor.fetchall()

# Generate the HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Menagerie Database</title>
</head>
<body>
    <h1>Menagerie Database</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Name</th>
                <th>Birth</th>
                <th>Birth Month</th>
            </tr>
        </thead>
        <tbody>
"""
for row in results:
    html_content += f"""
            <tr>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
                <td>{row[2]}</td>
            </tr>
    """
html_content += """
        </tbody>
    </table>
</body>
</html>
"""

# Write the HTML to a file
with open("menagerie.html", "w") as html_file:
    html_file.write(html_content)

print("HTML file generated: menagerie.html")
