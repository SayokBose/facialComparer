import face_recognition as fr  
import cv2 
import sys
import os

#create person object
class Person:
    def __init__(self,encoder,folder):
        self.encoder = encoder
        self.folder = folder
    
    #has a folderpath stored as a string
    #has a encoder which is a list

def getFaces(img):
    faceOne = fr.load_image_file(img)
    RgbFaceOne  = cv2.cvtColor(faceOne,cv2.COLOR_BGR2RGB)
    faces = fr.face_encodings(RgbFaceOne)
    return faces


def identifyFace(img, faces,current_File):
    #this function takes an image and sorts it into the file(s) it needs to go into
    #faces is a list of all the unqiue people
    imgfaces = getFaces(img)
    #this itereates through every face in an image
    for encoder in imgfaces:
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

    #if not, its a unique face and create new person object and append to faces

    #update faces incase a new person was added
    return faces