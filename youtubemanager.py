import sqlite3
con = sqlite3.connect("youtubemanager.db")
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS youtubemanager(
            ID INTEGER PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            TIME TEXT NOT NULL     
     )
''')

def addvideo():
    Id = int(input("Enter ID: "))
    name = input("Enter name: ")
    time = input("Enter time: ")
    cur.execute("INSERT INTO youtubemanager VALUES(?,?,?)",(Id,name,time))
    con.commit()

def viewall():
    cur.execute("SELECT * FROM youtubemanager")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    if not rows:
        print("No videos found")    

def viewparticular():
    Id = int(input("Enter ID: "))
    cur.execute("SELECT * FROM youtubemanager WHERE ID = ?",(Id,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def deletevideo():
    id = int(input("Enter ID: "))
    cur.execute("DELETE FROM youtubemanager WHERE ID = ?",(id,))
    con.commit()

def updatevideo():
    id = int(input("Enter Video ID: "))
    name = input("Enter new name: ")
    time = input("Enter new time: ")
    cur.execute("UPDATE youtubemanager SET NAME = ?, TIME = ? WHERE ID = ?",(name,time,id))
    con.commit()

def main():
    while True:
        print("\n 1. Add youtube video")
        print("2. View all videos")
        print("3. View a particular video")
        print("4. Delete a video")
        print("5. Update a video")
        print("6. Exit")
        ch = int(input("Enter your choice: "))

        match ch:
            case 1:
                addvideo()
            case 2:
                viewall()
                break
            case 3:
                viewparticular()
                break
            case 4:
                deletevideo()
            case 5:
                updatevideo()
            case 6:
                break
            case _:
                print("Invalid choice")    

    cur.close()



if __name__ == "__main__":
    main()