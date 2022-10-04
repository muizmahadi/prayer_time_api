#get response from function get_api(), then insert into database

from function_insert_into_database import get_api,create_database


reponse=get_api()
mycursor=create_database()

def insert_into_database(response,mycursor):
  prayers_key=["day","date","fajr","dhuhr","asr","maghrib","isha"]
  for i in response:
    new_time=[i[key].replace(":00","") for key in prayers_key]
    mycursor.execute("""INSERT INTO Pray_time (day,date,fajr,dhuhr,asr,maghrib,isha)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                        (new_time[0],new_time[1],new_time[2],new_time[3],new_time[4],new_time[5],new_time[6]))
    