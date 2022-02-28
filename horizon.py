from conn import Connector

def connect():
    connection = Connector("localhost", "3306", "root", "rafie1112", "student")
    connection = connection.connect_db()
    info = connection.get_server_info()
    print(info)
    return(connection)

def open_csv(path):
    connection = Connector("localhost", "3306", "root", "rafie1112", "student")
    file = connection.import_csv(path)
    return file

def getAllStudents():
    connection = connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students;")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def getStudentRecord(rollNumber):
    connection = connect()
    cursor = connection.cursor(dictionary=True)
    command_to_execute = f"SELECT * FROM students WHERE ROLL={rollNumber};"
    cursor.execute(command_to_execute)
    rows = cursor.fetchone()
    cursor.close()
    connection.close()
    return rows

def insertRecord(roll, name, gender, contact, dob, address):
    connection = connect()
    cursor = connection.cursor(dictionary=True)
    command_to_execute = f"INSERT INTO student.students (ROLL,NAME,GENDER,CONTACT,DOB,ADDRESS) VALUES ({int(roll)},'{name}','{gender}','{contact}','{dob}','{address}');"
    cursor.execute(command_to_execute)
    connection.commit()
    connection.close()

def removeRecord(rollNumber):
    connection = connect()
    cursor = connection.cursor(dictionary=True)
    command_to_execute = f"DELETE FROM student.students WHERE ROLL={rollNumber.get()};"
    cursor.execute(command_to_execute)
    connection.commit()
    connection.close()

def updateRecord(roll, name, gender, contact, dob, address):
    connection = connect()
    cursor = connection.cursor(dictionary=True)
    command_to_execute = f"UPDATE student.students SET NAME='{name}',GENDER='{gender}',CONTACT='{contact}',DOB='{dob}',ADDRESS='{address}' WHERE ROLL={roll};"
    cursor.execute(command_to_execute)
    connection.commit()
    connection.close()