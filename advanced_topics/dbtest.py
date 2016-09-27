import sqlite3

def Main():
    try:

        con = sqlite3.connect('test.db')
        cur = con.cursor()
        cur.executescript("""DROP TABLE IF EXISTS Pets;
        CREATE TABLE Pets(Id INT,Name TEXT,Price INT);
        INSERT INTO Pets VALUES(1,"Cat",400);
        INSERT INTO Pets VALUES(2,"Dog",456);
        INSERT INTO Pets VALUES(3,"Kutta",10000);
        """)

        pets = ((4,"Rabbit",200),
        (5,"Bird",60))

        cur.executemany("INSERT INTO Pets VALUES(?,?,?)",pets)

        con.commit()

        cur.execute('SELECT * FROM Pets')

        data = cur.fetchall()
        for row in data:
            print(row)

    except sqlite3.Error:
        if con:
            print("Error!, rolling back")
            con.rollback()

    finally:
        if con:
            con.close()


    con.close()

if __name__ == '__main__':
    Main()
