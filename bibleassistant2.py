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

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("recognizing")
        query = r.recognize_google(audio, language="en-US")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again")
        return "None"
    return query

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
    t = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10 }
    speak("What book do you want to read ?")
    bookname = takeCommandMic().lower()
    bookid = 0
    for b in book :
        bookid = bookid + 1
        if b.lower()==bookname.lower():
            break
    speak("What chapter ?")
    chapter = takeCommandMic().lower()
    if chapter in t:
        chapter = str(t[chapter])
    speak("What verse ?")
    verse = takeCommandMic().lower()
    if verse in t:
        verse = str(t[verse])
    mycursor.execute("SELECT * FROM kjv WHERE book=" + str(bookid) + " and chapter=" + chapter + " and verse=" + verse)
    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        speak("Bible verse not found")
    else:
        for row in myresult:
            speak(row[4])

speak("I am Bible Assistant. I am at your service.")
bible()