import mysql.connector



def create_conn():
    conn = None
    try:
        conn = mysql.connector.connect(host="35.188.102.27",
                                        db="community",
                                        user="myinstance",
                                        password="123456")
    except Exception as e:
        print(e)
    return conn


print(create_conn()) 

def execute_query(query, params, fetchall=True):
    conn = create_conn()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query % params)
        try:
            if fetchall:
                results = cursor.fetchall()
            else:
                results = cursor.fetchone()
        except:
            results = None
        conn.commit()
        cursor.close()
        conn.close()
        return results
    else:
        return False


def insert_course(name ,description ,days  ,teacher):
        
      conn = mysql.connector.connect(host="35.188.102.27",
                                          db="community",
                                          user="myinstance",
                                          password="123456")
            
      if conn:
        cursor = conn.cursor()
        cursor.execute("insert into Courses (name, description, days, teacher_name) VALUES(%s,%s,%s,%s);",name ,description ,days,teacher)
        
        return True
        
      else:
        print("Error while connecting to MySQL")
        return False
       

def insert_tasks(name,subject,description,dueDate):
        
      conn = mysql.connector.connect(host="35.188.102.27",
                                          db="community",
                                          user="myinstance",
                                          password="123456")
            
      if conn:
        cursor = conn.cursor()
        cursor.execute("insert into Tasks (task_name, subject, task_description, dueDate) VALUES(%s,%s,%s,%s);",name, subject, description, dueDate)
       
        return True
        
      else:
        print("Error while connecting to MySQL")
        return False
       

def insert_exam(name,subject,description,Date):

      conn = mysql.connector.connect(host="35.188.102.27",
                                          db="community",
                                          user="myinstance",
                                          password="123456")
            
      if conn:
        cursor = conn.cursor()
        cursor.execute("insert into Exams (exam_name, subject, exam_description, exam_date) VALUES(%s,%s,%s,%s);",name,subject,description,Date)
        
        return True
        
      else:
        print("Error while connecting to MySQL")
        return False
       
def insert_user(lastName  , firstName  , schoolID  ):

      conn = mysql.connector.connect(host="35.188.102.27",
                                          db="community",
                                          user="myinstance",
                                          password="123456")
             
      if conn:
        cursor = conn.cursor()
        cursor.execute(" insert into Users (userid,lastname,firstname) VALUES(%s,%s,%s) ;",lastName,firstName  , schoolID  )
        return True
        
      else:
        print("Error while connecting to MySQL")
        return False
       
def read_query(connection, query):
    cursor = connection.cursor()
    result = None

    if connection:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    else:
        print("Error while connecting to MySQL")
        return False

def list_