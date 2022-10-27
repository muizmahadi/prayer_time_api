

import requests
from datetime import datetime
import smtplib
import mysql.connector
from fpdf import FPDF
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders



mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="mumtazspm",
  database="waktu_solat"


)

mycursor=mydb.cursor()

#Function that send text to email specified.
def send_to_email(topic):
  sender="udemy7778@gmail.com"
  password="lqokdlbnjgsizfob"
  receiver="rahim.aiman@gmail.com"

  message=MIMEMultipart()
  message["From"] =sender
  message["To"] = receiver
  message["Subject"] ="Below is the attached pdf file for prayer times,"
  
  pdfname=topic

  binary_pdf=open(pdfname,"rb")
  payload=MIMEBase("application","octate-stream",name=pdfname)
  payload.set_payload((binary_pdf).read())

  encoders.encode_base64(payload)

  payload.add_header("Content-Decomposition","attachment",filename=pdfname)
  message.attach(payload)

  session = smtplib.SMTP("smtp.gmail.com",587)
  session.starttls()
  session.login(sender,password)

  text=message.as_string()
  session.sendmail(sender,receiver,text)
  print("Mail sent")
  session.quit()

#Function that create messages in email
def return_email_message(date,mycursor):
  time=[]
  sql_query="""SELECT * FROM pray_time where date IN (%s);"""
  mycursor.execute(sql_query,(date,))
  times=mycursor.fetchall()
  
  
  text=f"Date: {times[0][1]}"+"\n"
  text+=f"Day:  {times[0][0]}"+"\n\n"
  text+=f"fajr      -       {times[0][2]}"+"\n"
  text+=f"dhuhr     -       {times[0][3]}"+"\n"
  text+=f"asr       -       {times[0][4]}"+"\n"
  text+=f"maghrib   -       {times[0][5]}"+"\n"
  text+=f"isha      -       {times[0][6]}"+"\n"

  return text
  
#change the formnat of text to .pdf
def change_format_pdf(date,text):
  pdf=FPDF()
  pdf.add_page()
  pdf.set_font("Arial",size = 13)
  pdf.multi_cell(0,5,text)
  topic=f"Waktu Solat untuk {date}.pdf"
  pdf.output(topic)
  

#main function to compare between current and database date
def main_compare_date(mycursor ):
  today=datetime.now().strftime("%d-%b-%Y")
  mycursor.execute("SELECT date FROM Pray_time")
  dates=[date[0] for date in mycursor.fetchall()]
  for date in dates:
    if today==date:
      text=return_email_message(date,mycursor)
      topic=change_format_pdf(date,text)
  send_to_email(topic)

  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

#calling function to start the program
main_compare_date(mycursor)
