#!/usr/bin/python
import mysql.connector
from mysql.connector import errorcode
# Import modules for CGI handling 
import cgi, cgitb 
# Create instance of FieldStorage 

form = cgi.FieldStorage() 
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "shouut")
cursor=cnn.cursor()
name = form.getvalue('name')
ashoka_id = form.getvalue('ashoka_id')
e_number  = form.getvalue('e_number')
mobile = form.getvalue('mobile')
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Shuttle Bookings</title>"
print "</head>"
sql = 'SELECT e_number FROM seats'
cursor.execute(sql)
# Fetch all the rows in a list of lists.
results = cursor.fetchall()

for i in results:


	if i[0]==int(e_number):
		print "User Exists"
		print "\n"
		print "<a href=/programs/SignUp.html>Re-Register</a>"    
		break	
	else:
		if int(id)==20:
			print "Content-type:text/html\r\n\r\n"

			print "Full"
			break	

else:
	print "Content-type:text/html\r\n\r\n"

	print "Welcome"
	addName="INSERT INTO seats (name,ashoka_id,e_number,mobile) VALUES ('%s',%s','%s','%s')" % (name, ashoka_id , e_number , mobile)
	cursor.execute(addName)
	print "Content-type:text/html\r\n\r\n"

#print "<a href='/cgi-bin/getdata.py'> Check Availability </a>"

print "<body>"
#print "<h2> Hello %s %s %s %s %s %s %s %s </h2>" % (first_name,last_name,middle_name,mobile,day,month,year,qualification)
print "</body>"
print "</html>"
cnn.commit()
cnn.close()