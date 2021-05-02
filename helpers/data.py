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
