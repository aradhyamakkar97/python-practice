import sqlite3

def Main():
    try:

        con = sqlite3.connect('test.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE Pets(Id INT,Name TEXT,Price INT)')
        cur.execute('INSERT INTO Pets VALUES(1,"Cat",400)')
        cur.execute('INSERT INTO Pets VALUES(2,"Dog",456)')
        cur.execute('INSERT INTO Pets VALUES(3,"Kutta",10000)')

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
