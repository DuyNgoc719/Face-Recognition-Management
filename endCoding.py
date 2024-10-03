import cv2
import face_recognition
import pickle
from sql_comand import get_img
import numpy as np


id =[]
def find_end_coding():
    temp =get_img()
    img_list =[]
    global id
    for tmp in temp:
        id.append(tmp[1])
        nparr = np.frombuffer(tmp[0], np.uint8)
        img_cv2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img_list.append(img_cv2)
    encode_list=[]
    for img in img_list:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list

end_code_know = find_end_coding()

end_code_with_id = [end_code_know,id]

with open("EndCoding.p","wb") as f:
    pickle.dump(end_code_with_id, f)
