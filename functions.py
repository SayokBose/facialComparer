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

def identifyFace(img, faces_folder):
    # Load existing person objects and their encodings from the faces_folder
    faces = []
    for person_folder in os.listdir(faces_folder):
        person_folder_path = os.path.join(faces_folder, person_folder)
        if os.path.isdir(person_folder_path):
            # Load the encoding from the known_encoding.npy file
            encoder = np.load(os.path.join(person_folder_path, 'known_encoding.npy'))
            person = Person(encoder, person_folder)
            faces.append(person)

    # Calculate the encoding of the input image
    encoder = getEncoder(img)

    match = False
    for person in faces:
        match_result = fr.compare_faces([encoder], person.encoder)
        if match_result[0]:
            match = True
            # Add img to the person's folder
            person_folder_path = os.path.join(faces_folder, person.folder)
            img_filename = os.path.basename(img)
            cv2.imwrite(os.path.join(person_folder_path, img_filename), cv2.imread(img))
            break

    if not match:
        # Create a new folder directory
        new_folder = "person_" + str(len(faces) + 1)
        new_person_folder_path = os.path.join(faces_folder, new_folder)
        os.makedirs(new_person_folder_path)
        np.save(os.path.join(new_person_folder_path, 'known_encoding.npy'), encoder)
        img_filename = os.path.basename(img)
        cv2.imwrite(os.path.join(new_person_folder_path, img_filename), cv2.imread(img))
        
        new_person = Person(encoder, new_folder)
        faces.append(new_person)

    return faces