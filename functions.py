import face_recognition as fr  
import cv2 

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

def identifyFace(img, faces):
    #faces is a list of all the unqiue people
    encoder = getEncoder(img)
    match = False
    for person in faces:
        MatchResult = fr.compare_faces([encoder],person.encoder)
        if MatchResult[0]:
            match = True
            #add img to person.folder
            break
    if not match:
        #create a new folder directory
        newFolder = ""
        newFace = Person(encoder,newFolder)
        faces.append(newFace)
    #if not, its a unique face and create new person object and append to faces

    #update faces incase a new person was added
    return faces