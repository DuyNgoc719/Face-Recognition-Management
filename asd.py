import tkinter as tk

def canvas_clicked(event):
    print("Canvas clicked")

root = tk.Tk()
root.geometry('800x600')

def canvas_tmp_clicked(event):
    print("Canvas tmp clicked")

canvas_tmp = tk.Canvas(root,background='#000000',highlightthickness=0)
canvas_tmp.place(x=70,y=140,width=174,height=74)
frame_tmp=tk.Frame(canvas_tmp,background='#6ecfff')
canvas_tmp.create_window(87,37,window=frame_tmp,height=70,width=170)
lb_class = tk.Label(frame_tmp,text="C201",bg='#ffffff',font=('family',13),background='#6ecfff')
lb_class.pack(padx=10,pady=10)
frame_tmp.bind('<Button-1>', canvas_tmp_clicked)  # Gán sự kiện cho Frame

canvas_tmp.bind('<Button-1>', canvas_clicked)  # Gán sự kiện cho Canvas

canvas = tk.Canvas(root,background='#000000',highlightthickness=0)
canvas.place(x=70,y=180,width=174,height=144)
frame=tk.Frame(canvas,background='#ffffff')
canvas.create_window(87,72,window=frame,height=140,width=170)

lb_name = tk.Label(frame,text="Môn học: python",bg='#ffffff',font=('family',13))
lb_name.pack(padx=10,pady=10)

lb_time = tk.Label(frame,text="Giờ: 9h30-11h30",bg='#ffffff',font=('family',13))
lb_time.pack(padx=10,pady=10)

lb_id = tk.Label(frame,text="ID : python-2211",bg='#ffffff',font=('family',13))
lb_id.pack(padx=10,pady=10)

root.mainloop()
