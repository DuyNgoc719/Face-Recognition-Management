import tkinter as tk
from show_list import Subject


class TeacherDashboard:
    def __init__(self, root,name):
        self.root = root
        self.name=name
        self.root.resizable(False,False)
        self.root.title("Giảng viên - Điều hành lớp học")
        self.root.geometry("800x600")

        header_frame = tk.Frame(root, bg="#1d62f5", padx=10, pady=10)
        header_frame.pack(fill=tk.X)

        header_label = tk.Label(header_frame, text="Xin Chào "+name, font=("Helvetica", 20), bg="#1d62f5", fg="white")
        header_label.pack()
    
    def show_list_subject(self):
        app = Subject(self.root,self.name)
        app.list_mon_hoc()
def active(root,name):
    app = TeacherDashboard(root,name)
    app.show_list_subject()
    root.mainloop()
