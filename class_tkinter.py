import tkinter as tk
from PIL import Image, ImageTk
import config_last
import cv2
import numpy as np
from sql_comand import get_student_img,get_infor_student



class Window():
    def __init__(self,root,name):
        self.root=root
        self.name=name
        self.root.resizable(False,False)
        root.geometry('1000x600')

    def active_home(self,img):
        lb = tk.Label(self.root, height=300, width=400, relief="solid", border=2)
        lb.place(x=50, y=50)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        lb.imgtk = imgtk  
        lb.config(image=imgtk)

    def infor_face(self,name,id):

        lb_infor = tk.Label(self.root,height=20,width=60,relief="solid",border=2)
        lb_infor.place(x=500,y=50)

        lb_name = tk.Label(self.root,text = "Họ tên ",font=("Helvetica", 15))
        lb_name.place(x=550,y=100)


        lb_id = tk.Label(self.root,text = "Mã Sinh Viên ",font=("Helvetica", 15))
        lb_id.place(x=550,y=200)


        lb_doc_name = tk.Label(self.root,text=" : ",font=("Helvetica", 15))
        lb_doc_name.place(x=680,y=100)

        lb_doc_ms = tk.Label(self.root,text=" : ",font=("Helvetica", 15))
        lb_doc_ms.place(x=680,y=200)

        lb_out_name = tk.Label(self.root,text = name,font=("Helvetica", 15))
        lb_out_name.place(x=720,y=100)

        lb_out_id = tk.Label(self.root,text = id,font=("Helvetica", 15))
        lb_out_id.place(x=720,y=200)

        def remove_labels():
            lb_infor.destroy()
            lb_name.destroy()
            lb_id.destroy()
            lb_doc_name.destroy()
            lb_doc_ms.destroy()
            lb_out_name.destroy()
            lb_out_id.destroy()
        self.root.after(2000, remove_labels)

    def infor_face_errou(self,name,id):

        lb_infor = tk.Label(self.root,height=20,width=60,relief="solid",border=2)
        lb_infor.place(x=500,y=50)

        lb_name = tk.Label(self.root,text = "Họ tên ",font=("Helvetica", 15))
        lb_name.place(x=550,y=100)


        lb_id = tk.Label(self.root,text = "Mã Sinh Viên ",font=("Helvetica", 15))
        lb_id.place(x=550,y=200)


        lb_doc_name = tk.Label(self.root,text=" : ",font=("Helvetica", 15))
        lb_doc_name.place(x=680,y=100)

        lb_doc_ms = tk.Label(self.root,text=" : ",font=("Helvetica", 15))
        lb_doc_ms.place(x=680,y=200)

        lb_out_name = tk.Label(self.root,text = name,font=("Helvetica", 15))
        lb_out_name.place(x=720,y=100)

        lb_out_id = tk.Label(self.root,text = id,font=("Helvetica", 15))
        lb_out_id.place(x=720,y=200)

        def remove_labels():
            lb_infor.destroy()
            lb_name.destroy()
            lb_id.destroy()
            lb_doc_name.destroy()
            lb_doc_ms.destroy()
            lb_out_name.destroy()
            lb_out_id.destroy()
        self.root.after(2000, remove_labels)

    def is_accept(self):
        lb_accept = tk.Label(self.root,text = "Điểm danh thành công ",font=("Helvetica", 15),background="#1d62f5", fg="white")
        lb_accept.place(x=620,y=300)
        self.root.after(2000,lb_accept.destroy)

    def is_errou(self):
        lb_accept = tk.Label(self.root,text = "Không có trong lớp học ",font=("Helvetica", 18),background="#e30000", fg="#121111")
        lb_accept.place(x=620,y=300)
        self.root.after(2000,lb_accept.destroy)
    
    def is_have_student(self,id_student):
        ls_student = config_last.get_result(self.name)
        id_student = int(id_student)
        dem=0
        for student in ls_student :
            if id_student == student[0]:
                dem+1
                config_last.add_to_time(id_student)
                self.is_accept()
                name = get_infor_student(id_student)
                self.infor_face(name[1],id_student)
                break
            else :
                self.is_errou()
    def load_image_student(self,id):
        image_data = get_student_img(id)
        image_data=image_data[0]
        nparr = np.frombuffer(image_data, np.uint8)
        img_cv2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img_cv2
    def run(self):
        self.root.mainloop()

