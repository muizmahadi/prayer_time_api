import mysql.connector


def create_database():

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mumtazspm",
    database="waktu_solat"

  )

  mycursor = mydb.cursor()
  mycursor.execute("""CREATE TABLE Pray_time 
                    (day VARCHAR(50),
                    date VARCHAR(50),
                    fajr VARCHAR(50), 
                    dhuhr VARCHAR(50), 
                    asr VARCHAR(50),
                    maghrib VARCHAR(50), 
                    isha VARCHAR(50))""")
  return mycursor

           
create_database()