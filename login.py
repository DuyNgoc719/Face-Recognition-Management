import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
from config_last import submit_login

def login_place(root,):
    root.title("Login")
    root.geometry("800x600")

    img = Image.open('image/background/login.jpg')
    img_background = ImageTk.PhotoImage(img)

    background_lb = Label(root, image=img_background)
    background_lb.place(x=0, y=0, relheight=1, relwidth=1)
    background_lb.image = img_background

    canvas_tmp = tk.Canvas(root,background='#000000',highlightthickness=0)
    canvas_tmp.place(x=140,y=260,width=504,height=44)
    frame_tmp =tk.Frame(canvas_tmp,background='#6ecfff')
    canvas_tmp.create_window(252,22,window=frame_tmp,width=500,height=40)
    lb_temp=tk.Label(frame_tmp,text='Đăng Nhập',font=('family', 15), background='#6ecfff')
    lb_temp.place(x=1,y=1)


    canvas = tk.Canvas(root,background='#000000',highlightthickness=0)
    canvas.place(x=140,y=300,width=504,height=204)

    frame = tk.Frame(canvas, background='#ffffff')
    canvas.create_window(252,102,window=frame,width=500,height=200)


    lb_username = tk.Label(frame, text="Tài Khoản : ", font=('family', 15), background='#ffffff')
    lb_username.place(x=100, y=50) 

    txt_username = tk.Entry(frame, font=('family', 15), width=20, background='#ffffff')
    txt_username.place(x=230, y=50)  

    lb_pass = tk.Label(frame, text="Mật khẩu : ", font=('family', 15), background='#ffffff')
    lb_pass.place(x=100, y=100)  

    txt_pass = tk.Entry(frame, font=('family', 15), width=20, background='#ffffff', show='*')
    txt_pass.place(x=230, y=100)  

    btn_submit = tk.Button(frame, font=('family', 15), text='Đăng Nhập', command=\
                           lambda : submit_login(root,txt_username,txt_pass), background='#ffffff')
    btn_submit.place(x=350, y=150)  

    
    root.mainloop()

