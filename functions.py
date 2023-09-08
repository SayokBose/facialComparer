import os
import face_recognition as fr  
import cv2 
import numpy as np


def getEncoder(img):
    #return a encoder val of the person
    faceOne = fr.load_image_file(img)
    RgbFaceOne  = cv2.cvtColor(faceOne,cv2.COLOR_BGR2RGB)
    faceLocOne = fr.face_locations(RgbFaceOne)[0]
    faceOneEnco = fr.face_encodings(RgbFaceOne)[0]
    
    return faceOneEnco

#create person object
class Person:
    def __init__(self,encoder,folder):
        self.encoder = encoder
        self.folder = folder
    
    #has a folderpath stored as a string
    #has a encoder which is a list

def identifyFace(img, faces, current_File):

    # Calculate the encoding of the input image
    encoder = getEncoder(img)

    match = False
    for person in faces:
        for enc in person.encoder :
            match_result = fr.compare_faces([encoder], enc)
            if match_result[0]:
                break
        if match_result[0]:
            person.encoder.append(encoder)
            match = True
            # Add img to the person's folder
            person_folder_path = os.path.join(current_File, person.folder)
            img_filename = os.path.basename(img)
            cv2.imwrite(os.path.join(person_folder_path, img_filename), cv2.imread(img))
            break

    if not match:
        # Create a new folder directory
        new_folder = "person_" + str(len(faces) + 1)
        new_person_folder_path = os.path.join(current_File, new_folder)
        os.makedirs(new_person_folder_path)
        img_filename = os.path.basename(img)
        cv2.imwrite(os.path.join(new_person_folder_path, img_filename), cv2.imread(img))
        print(img)
        new_person = Person([encoder], new_folder)
        faces.append(new_person)

    return faces

