from flask.ext.mysql import MySQL

conn = MySQL.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE students (name TEXT, lastname TEXT, password TEXT, confirm password TEXT, DD TEXT, MM TEXT, YY TEXT, mobile_number TEXT, location TEXT)')
print "Table created successfully";


conn.close()
