import pymysql
from datetime import datetime
import os
from PIL import Image
from io import BytesIO

conn=pymysql.connect(
    host='localhost',
    user='root',
    password='Ngoc71986@',
    database='quanly'
)
cursor = conn.cursor()



def get_date_now():
    day_now = datetime.now()
    return day_now.day

def login_account():
    cursor.execute("SELECT * FROM account")
    row = cursor.fetchall()
    return row

def get_lecturer(role):
    cursor.execute(f"SELECT * FROM account WHERE account.role ='{role}' ")
    row = cursor.fetchone()
    return row


def get_subject(name_owner,day_now):
    cursor.execute(f"SELECT * FROM subject WHERE subject.owner='{name_owner}' AND subject.day={day_now}")
    row = cursor.fetchall()
    return row

def get_class(subject_name):
    cursor.execute(f"SELECT class_name FROM class_room_student WHERE class_room_student.subject_id = '{subject_name}'")
    row = cursor.fetchone()
    return row

def insert_student(id,name):
    sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
    cursor.execute(sql, (id,name,))
    conn.commit()

def insert_class_room(class_name,student_id,subject_id):
    sql = "INSERT INTO class_room_student (class_name,student_id,subject_id) VALUES (%s, %s,%s)"
    cursor.execute(sql, (class_name,student_id,subject_id))
    conn.commit()

def insert_result(class_name,subject_name):
    insert_query = f"""
            INSERT INTO result (id, date, check_in, check_out)
            SELECT student_id, %s, NULL, NULL
            FROM class_room_student as crt
            WHERE crt.class_name = '{class_name}' and crt.subject_id ='{subject_name}'
            ;
            """
            
    current_date = datetime.now()
    current_date= current_date.strftime("%Y-%m-%d")
    cursor.execute(insert_query, (current_date,))
        
    conn.commit()

def insert_result_id(student_id):
    insert_query = "INSERT INTO result (id, date, check_in, check_out) VALUE (%s,%s);"
            
    current_date = datetime.now()
    current_date= current_date.strftime("%Y-%m-%d")
    cursor.execute(insert_query, (student_id,current_date,))
        
    conn.commit()

def get_student_id_subject(subject_name):
    cursor.execute(f"SELECT student_id FROM class_room_student as crt WHERE crt.subject_id ='{subject_name}'")
    row = cursor.fetchall()
    student_ids=[]
    for tmp in row : 
        student_ids.append(tmp[0] )
    return student_ids

def insert_all_result():
    id = get_all_class_student()
    for tmp in id :
        insert_query = f"""
                INSERT INTO result (id, date) VALUES (%s, %s)
                ;
                """
        current_date = datetime.now()
        current_date= current_date.strftime("%Y-%m-%d")
        cursor.execute(insert_query, (tmp,current_date,))
        conn.commit()

def get_all_class_student():
    cursor.execute(f"SELECT id FROM student ")
    row = cursor.fetchall()
    cleaned_rows = [item[0] for item in row]
    return cleaned_rows

def get_result(subject_name):
    name = get_student_id_subject(subject_name)
    student_ids_str = ', '.join([f"'{student_id}'" for student_id in name])
    cursor.execute(f"SELECT * FROM result WHERE result.id IN ({student_ids_str})")
    rows = cursor.fetchall()
    return rows

def get_infor_student(id):
    cursor.execute(f"SELECT * FROM student WHERE student.id = '{id}'")
    row = cursor.fetchone()
    return row    

def change_result(id_student,check_in,check_out):
    update_query = f"""
        UPDATE result
        SET check_in = %s, check_out = %s
        WHERE id = '{id_student}';
        """
    cursor.execute(update_query, (check_in, check_out))
    conn.commit()

def get_id(temp):
    tmp =temp.split('-')
    return tmp[0]

def insert_img():
    folder_path = 'image/sinhvien'
    with conn.cursor() as cursor:
        for filename in os.listdir(folder_path):
            if filename.endswith('.jpg'):  
                with open(os.path.join(folder_path, filename), 'rb') as file:
                    image_data = file.read()
                sql = "INSERT INTO image (image, id) VALUES (%s, %s)"
                id = get_id(filename)
                cursor.execute(sql, (image_data,id,))
    conn.commit()

def get_img():
    cursor.execute("SELECT * FROM image")
    row = cursor.fetchall()
    return row

def get_student_img(id):
    cursor.execute(f"SELECT image FROM image WHERE image.id ='{id}'")
    row = cursor.fetchone()
    return row

def update():
    update_query = f"""
        UPDATE result
        SET diem_danh = %s
        WHERE result.id = 22110381
        """
    cursor.execute(update_query,(4))
    conn.commit()

update()