import face_recognition as fr  
import cv2 

def compareFaces(img1, img2):
    # let's match two faces 
    

    faceOne = fr.load_image_file(img1)
    faceTwo = fr.load_image_file(img2)

    # face convert to rgb 

    RgbFaceOne  = cv2.cvtColor(faceOne,cv2.COLOR_BGR2RGB)
    RgbFaceTwo  = cv2.cvtColor(faceTwo,cv2.COLOR_BGR2RGB)

    # lets Face locations

    faceLocOne = fr.face_locations(RgbFaceOne)[0]
    faceLocTwo = fr.face_locations(RgbFaceTwo)[0]

    '''
    cv2.rectangle(faceOne ,(faceLocOne[3],faceLocOne[0]),(faceLocOne[1],faceLocOne[2]), (0,255,0) ,2)
    cv2.rectangle(faceTwo ,(faceLocTwo[3],faceLocTwo[0]),(faceLocTwo[1],faceLocTwo[2]), (0,255,0) ,2)
    '''
    # Encodings to Match 
    faceOneEnco = fr.face_encodings(RgbFaceOne)[0]
    faceTwoEnco = fr.face_encodings(RgbFaceTwo)[0]


    # matching Face  
    MatchResult = fr.compare_faces([faceOneEnco],faceTwoEnco)

    return MatchResult[0]

    '''
    if MatchResult[0] == True :
        cv2.putText(faceOne,"Face Matched" , (5,60),cv2.FONT_HERSHEY_COMPLEX ,2,(255,0,0),2)
    else:
        cv2.putText(faceOne,"Face Not Matched" , (5,60),cv2.FONT_HERSHEY_COMPLEX ,2,(255,0,0),2)
    cv2.imshow("Image", faceOne)
    cv2.imshow("Image Two", faceTwo)
    cv2.waitKey()
    print('done')'''

p1 = "/Users/sayok/Desktop/Projects/facial_app/people/isla.jpg"
p2 = "/Users/sayok/Desktop/Projects/facial_app/people/isla2.jpg"
result = compareFaces(p1,p2)
print(result)