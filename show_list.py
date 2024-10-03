import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, Label,messagebox
import detect_face
import config_last
from capture_face import text_img
from PIL import Image, ImageTk
import sql_comand

class Subject:
    def __init__(self, root,name):
        self.name = name
        self.root = root
        self.root.resizable(False,False)
    
    def list_mon_hoc(self):
        data = config_last.get_subject_owner()
        class_now = data[0]
        infor = data[1]
        pos_x = 70
        pos_y = 180
        dem=0
        for tmp in range(len(class_now)):
            self.create_box(pos_x,pos_y,class_now[tmp],infor[tmp])
            dem+=1
            if dem%3 ==0:
                pos_y+=240
                pos_x=70
            else :
                pos_x+=210
    
    def list_student_join(self,name,id):
        app=tk.Toplevel(self.root)
        self.root.withdraw()
        app.geometry('800x600')
        app.resizable(False,False)

        name_class = 'Đây là lớp : ' + name
        label_name = tk.Label(app, text=name_class, font=("Helvetica", 16), padx=10, pady=10)
        label_name.place(x=30,y=10)

        btn_face=tk.Button(app,text='Điểm danh',background="#1d62f5", fg="white",command=lambda: self.detect_face_import(app,id,name),font=("family",15))
        btn_face.place(x=300,y=5)

        btn_face=tk.Button(app,text='Thêm Học Sinh',background="#1d62f5", fg="white",command=lambda: self.text_img(app,name,id),font=("family",15))
        btn_face.place(x=450,y=5)

        btn_face=tk.Button(app,text='Thoát',background="#ff0015", fg="#000000",command=lambda: self.back_to_subject(app),font=("family",15))
        btn_face.place(x=650,y=5)

        canvas = tk.Canvas(app)
        canvas.place(x=1,y=50,width=800,height=600)
        scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=780, height=540)
        canvas.configure(yscrollcommand=scrollbar.set)

        columns = ('#1', '#2', '#3','#4','#5')
        tree = ttk.Treeview(scrollable_frame, columns=columns, show='headings')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 13, "bold"))

        tree.heading('#1', text='ID', anchor=tk.CENTER)
        tree.heading('#2', text='Date', anchor=tk.CENTER)
        tree.heading('#3', text='Check In', anchor=tk.CENTER)
        tree.heading('#4', text='Check Out', anchor=tk.CENTER)
        tree.heading('#5', text='Date Submit', anchor=tk.CENTER)

        tree.column('#1', width=50, anchor=tk.CENTER)
        tree.column('#2', width=100, anchor=tk.CENTER)
        tree.column('#3', width=50, anchor=tk.CENTER)
        tree.column('#4', width=50, anchor=tk.CENTER)
        tree.column('#5', width=50, anchor=tk.CENTER)

        tree.tag_configure('custom_font', font=("Helvetica", 13))
        #tree.place(x=250, y=150)
        tree.config(height=20)

        data = self.get_data_student(id)

        for row in data:
            tree.insert('', tk.END, values=row, tags=('custom_font'))

        tree.pack(fill=tk.BOTH, expand=True)

        #canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def get_data_student(self,id):
        tmp = config_last.get_result(id)
        return tmp
    
    def detect_face_import(self,app,id,name):
        temp =tk.Toplevel(app)
        btn_face=tk.Button(temp,text='Thoát',background="#ff0015", fg="#000000",command=lambda: self.back_to_student(app,temp,id,name),font=("family",15),width=30,height=4)
        btn_face.place(x=500,y=480)
        app.withdraw()
        detect_face.detect_know_face(temp,id)
        temp.resizable(False,False)
    
    def back_to_student(self,app,temp,id,name):
        app.destroy()
        self.list_student_join(name,id)
        #app.deiconify()
        temp.destroy()
        detect_face.stop()

    def back_to_add(self,app,temp,id,name):
        print('BACK')
        app.destroy()
        self.list_student_join(name,id)
        #app.deiconify()
        temp.destroy()

    def back_to_subject(self,app):
        app.destroy()
        self.root.deiconify()
        
    def create_box(self,x_pos,y_pos,class_now,infor):
        def handle_event(event):
            self.list_student_join(class_now,infor[2])
        canvas_tmp = tk.Canvas(self.root,background='#000000',highlightthickness=0)
        canvas_tmp.place(x=x_pos,y=y_pos-40,width=174,height=74)
        frame_tmp=tk.Frame(canvas_tmp,background='#6ecfff')
        canvas_tmp.create_window(87,37,window=frame_tmp,height=70,width=170)
        lb_class = tk.Label(frame_tmp,text=class_now,bg='#ffffff',font=('family',13),background='#6ecfff')
        lb_class.pack(padx=10,pady=10)
        canvas_tmp.bind('<Button-1>',handle_event)
        frame_tmp.bind('<Button-1>',handle_event)

        canvas = tk.Canvas(self.root,background='#000000',highlightthickness=0)
        canvas.place(x=x_pos,y=y_pos,width=174,height=144)

        frame=tk.Frame(canvas,background='#ffffff')
        canvas.create_window(87,72,window=frame,height=140,width=170)

        lb_name = tk.Label(frame,text="Môn học: "+infor[0],bg='#ffffff',font=('family',13))
        lb_name.pack(padx=10,pady=10)
        lb_name.bind('<Button-1>',handle_event)

        lb_time = tk.Label(frame,text="Giờ: "+infor[1],bg='#ffffff',font=('family',13))
        lb_time.pack(padx=10,pady=10)
        lb_time.bind('<Button-1>',handle_event)

        lb_id = tk.Label(frame,text="ID: "+infor[2],bg='#ffffff',font=('family',13))
        lb_id.pack(padx=10,pady=10)
        lb_id.bind('<Button-1>',handle_event)
        canvas.bind('<Button-1>',handle_event)
        frame.bind('<Button-1>',handle_event)
    
    def text_img(self,temp,class_name,subject_id):
        app = tk.Toplevel(temp)
        temp.deiconify()
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
                            command=lambda : self.add_to_dbs(class_name,txt_id.get(),subject_id,txt_name.get()))
        btn_submit.place(x=200, y=150)

        canvas_img = tk.Canvas(app, background='#000000', highlightthickness=0)
        canvas_img.place(x=50, y=250, width=204, height=204)

        frame_img = tk.Frame(canvas_img, background='#ffffff')
        canvas_img.create_window(102, 102, window=frame_img, width=200, height=200)

        lb_img = tk.Label(frame_img)
        lb_img.place(x=0, y=0)

        btn_submit_img = tk.Button(frame_img, font=('family', 14), text='Chọn ảnh', background='#008fe8', fg='#ffffff', command=lambda: self.pick_file(lb_img, btn_submit_img))
        btn_submit_img.place(x=50, y=50)

        btn_face=tk.Button(app,text='Thoát',background="#ff0015",\
                        command=lambda: self.back_to_add(temp,app,subject_id,class_name), fg="#000000",font=("family",18))
        btn_face.place(x=600,y=500)

    def pick_file(self,lb_img, btn_submit_img):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            lb_img.img_tk = img_tk 
            lb_img.config(image=img_tk)
            btn_submit_img.place_forget()  

    def add_to_dbs(self,class_name,student_id,subject_id,name_student):
        ls_student = sql_comand.get_infor_student(student_id)
        student_id = int(student_id)
        ls_student_class = sql_comand.get_student_id_subject(subject_id)
        if ls_student == None:
            sql_comand.insert_student(student_id,name_student)
            sql_comand.insert_class_room(class_name,student_id,subject_id)
            sql_comand.insert_result_id(class_name,subject_id)
            messagebox.showinfo('Thông Báo',"Thêm Sinh Viên Thành Công")
        elif  student_id not in ls_student_class:
            sql_comand.insert_class_room(class_name,student_id,subject_id)
            sql_comand.insert_result_id(class_name,subject_id)
            messagebox.showinfo('Thông Báo','Thêm sinh viên thành công')
        else :
            messagebox.showerror('Thông Báo','Sinh viên đã có trên hệ thống')

