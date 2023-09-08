import face_recognition as fr  
import cv2 
import sys
import os
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileSystemModel,
    QTreeView,
    QListView,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QFileDialog,
    QLineEdit,
    QDesktopWidget
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QFont
from functions import *


class FaceComparer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.faces = []
        self.folder_path = ""

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Face Comparer')

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        self.main_layout = QVBoxLayout(central_widget)

        # Create a sidebar for directory tree
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setSpacing(0)

        organize_button = QPushButton('Organize', self)
        organize_button.clicked.connect(self.organize)
        sidebar_layout.addWidget(organize_button)
        
        file_layout = QVBoxLayout()
        file_layout.setSpacing(0)
        # Create a file input
        self.file_input = QLineEdit(self)
        file_layout.addWidget(QLabel('File:'))
        file_layout.addWidget(self.file_input)
 
        # Create a button to select the file
        folder_button = QPushButton('Select File', self)
        folder_button.clicked.connect(self.upload_folder)
        file_layout.addWidget(folder_button)

        file_widget = QWidget()
        file_widget.setLayout(file_layout)
        sidebar_layout.addWidget(file_widget)

        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar_layout)
        self.main_layout.addWidget(sidebar_widget)

        screen_geo = QDesktopWidget().screenGeometry()
        minimum_width = int(screen_geo.width() * 0.6)
        minimum_height = int(screen_geo.height() * 0.6)
        self.setMinimumSize(minimum_width, minimum_height)

    def upload_folder(self):
        folder_dialog = QFileDialog()
        folder_path = folder_dialog.getExistingDirectory(self, 'Select Folder')
        if folder_path:
            self.file_input.setText(folder_path)
            self.folder_path = folder_path

    def organize(self):
        #iterate through all the images in the folder. the path is self.folder_path
        files = os.listdir(self.folder_path)
        #image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".webp")
        for i in files:
            print(i)
            if i[0] == '.':
                continue
            else:
                self.faces = identifyFace(self.folder_path + "/" +i ,self.faces, self.folder_path)

        '''
        for img in folder: #sudo code not actually the way to iterate
            self.faces = identifyFace(img,self.faces)'''



def main():
    app = QApplication(sys.argv)
    ex = FaceComparer()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()





'''
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

    
    cv2.rectangle(faceOne ,(faceLocOne[3],faceLocOne[0]),(faceLocOne[1],faceLocOne[2]), (0,255,0) ,2)
    cv2.rectangle(faceTwo ,(faceLocTwo[3],faceLocTwo[0]),(faceLocTwo[1],faceLocTwo[2]), (0,255,0) ,2)
    
    # Encodings to Match 
    faceOneEnco = fr.face_encodings(RgbFaceOne)[0]
    faceTwoEnco = fr.face_encodings(RgbFaceTwo)[0]

    # matching Face  
    MatchResult = fr.compare_faces(faceOneEnco,[faceTwoEnco])

    

    
    if MatchResult[0] == True :
        cv2.putText(faceOne,"Face Matched" , (5,60),cv2.FONT_HERSHEY_COMPLEX ,2,(255,0,0),2)
    else:
        cv2.putText(faceOne,"Face Not Matched" , (5,60),cv2.FONT_HERSHEY_COMPLEX ,2,(255,0,0),2)
    cv2.imshow("Image", faceOne)
    cv2.imshow("Image Two", faceTwo)
    cv2.waitKey()
    print('done')
    return MatchResult[0]



p2 = "/Users/sayok/Desktop/Projects/facial_app/people/kimb4.jpg"
p1 = "/Users/sayok/Desktop/Projects/facial_app/people/kimA.jpg"
result = compareFaces(p1,p2)
print(result)
'''