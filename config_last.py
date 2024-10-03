from tkinter import messagebox
import sql_comand
import giangvien
import time
from datetime import datetime
import tkinter as tk

check_time=[]

def submit_login(root,txt_username,txt_pass):
        tmp=False
        user = txt_username.get()
        pass_work = txt_pass.get()
        data = sql_comand.login_account()
        for row in data :
            if row[0]==user and row[1]==pass_work:
                messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
                root.after(10,root.withdraw)
                new_window = tk.Toplevel(root)
                name = get_lecturer('lecturer')
                time.sleep(0.5)
                giangvien.active(new_window,name[3])
                tmp=True
        if tmp ==False:
             messagebox.showerror("Thông báo", "Đăng nhập không thành công!")

def get_lecturer(role):
    lecturer = sql_comand.get_lecturer(role)
    return lecturer
def get_subject_owner():
    lecturer = get_lecturer('lecturer')
    day_now = get_now_day()
    subject = sql_comand.get_subject(lecturer[3],day_now)
    class_now=[]
    for sb in subject :
        tmp = sql_comand.get_class(sb[2])
        if tmp:
            class_now .append(tmp[0])
    return class_now ,subject

def get_now_day():
     day_time = datetime.now()
     day_time = day_time.day
     return day_time

def get_infor_student(id):
     pass

def get_result(subject_name):
     result = sql_comand.get_result(subject_name)
     return result     

def add_to_time(id_student):
    global check_time
    time_now = datetime.now()
    am_pm = time_now.strftime('%p')
    asd = (f"{am_pm}")
    temp = str(time_now.hour)+'h '+str(time_now.minute)+'p' +asd
    check_time.append(temp)
    if len(check_time)>1:
        sql_comand.change_result(id_student,check_time[0],check_time[len(check_time)-1])
    elif len(check_time)==1:
        sql_comand.change_result(id_student,check_time[0],None)