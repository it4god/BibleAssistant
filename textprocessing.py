import mysql.connector
import time
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bible"
)


bookid = 0
chapter = 0
verse = 0
bookname = "Bible"

with open("TEXT-PCE.txt") as f:
    for line in f:
        #time.sleep(1)
        bibleline = line.split(" ", 2)
        book = bibleline[0]
        text = bibleline[2] 
        chapterverse = bibleline[1].split(":")
        chapter = chapterverse[0]
        verse = chapterverse[1]
        if(bookname != book):
            bookname = book
            bookid = bookid + 1

        
        mycursor = mydb.cursor()

        sql = "INSERT INTO kjv (book, chapter, verse, text) VALUES (%s, %s, %s, %s)"
        val = (str(bookid), str(chapter), str(verse), str(text))
        mycursor.execute(sql, val)

        mydb.commit()
        print(str(bookid) + " " + str(chapter) + " " + str(verse) + " " + str(text))
