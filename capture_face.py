import tkinter as tk
from tkinter import filedialog, Label,messagebox
from PIL import Image, ImageTk
import sql_comand

def text_img(root,class_name,subject_id):
    app = tk.Toplevel(root)
    app.title("Login")
    app.geometry("800x600")
    app.resizable(False,False)

    img = Image.open('image/background/login.jpg')
    img_background = ImageTk.PhotoImage(img)

    background_lb = Label(app, image=img_background)
    background_lb.place(x=0, y=0, relheight=1, relwidth=1)
    background_lb.image = img_background

    canvas = tk.Canvas(app, background='#000000', highlightthickness=0)
    canvas.place(x=400, y=250, width=354, height=204)

    frame = tk.Frame(canvas, background='#ffffff')
    canvas.create_window(177, 102, window=frame, width=350, height=200)

    lb_id = tk.Label(frame, text="Id : ", font=('family', 12), background='#ffffff')
    lb_id.place(x=58, y=50)

    txt_id = tk.Entry(frame, font=('family', 12), width=18, background='#ffffff')
    txt_id.place(x=150, y=50)

    lb_name = tk.Label(frame, text="Họ Tên : ", font=('family', 12), background='#ffffff')
    lb_name.place(x=20, y=100)

    txt_name = tk.Entry(frame, font=('family', 12), width=18, background='#ffffff')
    txt_name.place(x=150, y=100)

    btn_submit = tk.Button(frame, font=('family', 15), text='Hoàn tất', background='#ffffff',\
                           command=lambda : add_to_dbs(class_name,txt_id.get(),subject_id,txt_name.get()))
    btn_submit.place(x=200, y=150)

    canvas_img = tk.Canvas(app, background='#000000', highlightthickness=0)
    canvas_img.place(x=50, y=250, width=204, height=204)

    frame_img = tk.Frame(canvas_img, background='#ffffff')
    canvas_img.create_window(102, 102, window=frame_img, width=200, height=200)

    lb_img = tk.Label(frame_img)
    lb_img.place(x=0, y=0)

    btn_submit_img = tk.Button(frame_img, font=('family', 14), text='Chọn ảnh', background='#008fe8', fg='#ffffff', command=lambda: pick_file(lb_img, btn_submit_img))
    btn_submit_img.place(x=50, y=50)
    btn_face=tk.Button(app,text='Thoát',background="#ff0015", fg="#000000",font=("family",18))

    btn_face.place(x=600,y=500)

def pick_file(lb_img, btn_submit_img):
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        lb_img.img_tk = img_tk 
        lb_img.config(image=img_tk)
        btn_submit_img.place_forget()  

def add_to_dbs(class_name,student_id,subject_id,name_student):
    ls_student = sql_comand.get_infor_student(student_id)
    print(ls_student)
    student_id = int(student_id)
    print(student_id)
    ls_student_class = sql_comand.get_student_id_subject(subject_id)
    print(ls_student_class)
    if ls_student == None:
        print('not have student')
        sql_comand.insert_student(student_id,name_student)
        sql_comand.insert_class_room(class_name,student_id,subject_id)
        sql_comand.insert_result(class_name,subject_id)
        messagebox.showinfo('Thêm sinh viên thành công')
    elif  student_id not in ls_student_class:
        print('not in class')
        sql_comand.insert_class_room(class_name,student_id,subject_id)
        sql_comand.insert_result(class_name,subject_id)
        messagebox.showinfo('Thêm sinh viên thành công')
    else :
        messagebox.showerror('Sinh viên đã có trên hệ thống')
