import pyttsx3
import mysql.connector
import speech_recognition as sr

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bible"
)

engine = pyttsx3.init()
engine.setProperty('rate', 120) 
mycursor = mydb.cursor()

def speak(text):    
    engine.say(text)
    engine.runAndWait()

def bible():
    book = [ "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings",
    "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah",
    "Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes",
    "Songs", "Isaiah", "Jeremiah", "Lamentations", "Ezekiel",
    "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah",
    "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah",
    "Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans",
    "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
    "Phillipians", "Colossians", "1 Thessalonians", "2 Thessalonians",
    "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James",
    "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation" ]

    bookname = input("What Book you want to read : ")
    bookid = 0
    for b in book :
        bookid = bookid + 1
        if b.lower()==bookname.lower():
            break
    
    chapter = input("What chapter you want to read : ")
    verse = input("What verse you want to read : ") 
    mycursor.execute("SELECT * FROM t_kjv WHERE b=" + str(bookid) + " and c=" + chapter + " and v=" + verse)
    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        speak("Bible verse not found")
    else:
        for row in myresult:
            speak(row[4])

speak("I am Bible Assistant. I am at your service.")
bible()