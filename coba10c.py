# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\James\Kuliah\Semester 8\code\pyqt-opencv\tes_sendiri\coba10c.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import cv2
import numpy as np
from keras.models import model_from_json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QThread

from coba10c_page23 import Ui_SecondWindow

import sys
import pygame
import time
import random
import os

bg = None
sekali = False
kelas = ['Atas','Bawah','Kanan','Kiri','Latar']
arah = ''

with open('keras/model.json', 'r') as file:
    model = model_from_json(file.read())

model.load_weights('keras/model.h5')
print('Model Loaded!')

files = os.listdir()
if 'highscore.txt' in files:
    file = open('highscore.txt', 'r')
    isinya = file.read()
    # print(isinya)
    highscore = int(isinya)
else:
    file = open('highscore.txt', 'w')
    file.write('0')
    highscore = 0
    file.close()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1347, 625)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(920, 90, 400, 300))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(1050, 440, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 50, 125, 125))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 500, 500))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(688, 233, 171, 176))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(689, 427, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(598, 233, 81, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(600, 430, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 530, 251, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(650, 500, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.button_2.setFont(font)
        self.button_2.setStyleSheet("border-top-color: rgb(0, 255, 127);")
        self.button_2.setObjectName("button_2")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(700, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(690, 200, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        # Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1347, 21))
        self.menubar.setObjectName("menubar")
        # Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        # Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MainWindow"))
        self.button.setText(_translate("Form", "Mulai"))
        self.label_10.setText(_translate("Form", "Atas"))
        self.label_11.setText(_translate("Form", "Bawah"))
        self.label_12.setText(_translate("Form", "Kanan"))
        self.label_13.setText(_translate("Form", "Kiri"))
        self.label_14.setText(_translate("Form", "Latar"))
        self.label_15.setText(_translate("Form", "Gerakan"))
        self.label_16.setText(_translate("Form", "Skor Tertinggi:"))
        self.button_2.setText(_translate("Form", "Cara Bermain"))
        self.label_18.setText(_translate("Form", "Inputan"))
        self.label_19.setText(_translate("Form", "Tingkat Keyakinan"))

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
silver = (141, 143, 145)

dis_width = 500
dis_height = 500

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

snake_block = 25
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    global dis
    value = score_font.render("Skor: " + str(score), True, green)
    dis.blit(value, [0, 0])
 
 
def our_snake(snake_block, snake_list):
    global dis
    for x in snake_list:
        if x == snake_list[-1]:
            pygame.draw.rect(dis, (141, 143, 145), [x[0], x[1], snake_block, snake_block])
        else:
            pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])
        
class gaming(QThread):
    def __init__(self, gambar, hs):
        # call QWidget constructor
        QThread.__init__(self)
        self.gambar = gambar
        self.hs = hs
        
    def run(self):
        global arah
        global dis
        global highscore
        try:
            posisi = None
        
            x1 = dis_width / 2
            y1 = dis_height / 2
        
            x1_change = 0
            y1_change = 0
        
            snake_List = []
            Length_of_snake = 1
        
            foodx = round(random.randrange(0, dis_width - snake_block) / 25.0) * 25.0
            foody = round(random.randrange(0, dis_height - snake_block) / 25.0) * 25.0
        
            game_over = False
            while True:
                if game_over == True:
                    # print(best_score)
                    time.sleep(0.5)
                    pygame.display.update()
             
                    x1 = dis_width / 2
                    y1 = dis_height / 2
                    
                    x1_change = 0
                    y1_change = 0
                 
                    snake_List = []
                    Length_of_snake = 1
                 
                    foodx = round(random.randrange(0, dis_width - snake_block) / 25.0) * 25.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 25.0) * 25.0
                    
                    game_over = False
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_over = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT and posisi is not 'Kanan':
                                x1_change = -snake_block
                                y1_change = 0
                                posisi = 'Kiri'
                            elif event.key == pygame.K_RIGHT and posisi is not 'Kiri':
                                x1_change = snake_block
                                y1_change = 0
                                posisi = 'Kanan'
                            elif event.key == pygame.K_UP and posisi is not 'Bawah':
                                y1_change = -snake_block
                                x1_change = 0
                                posisi = 'Atas'
                            elif event.key == pygame.K_DOWN and posisi is not 'Atas':
                                y1_change = snake_block
                                x1_change = 0
                                posisi = 'Bawah'
                                
                    if arah == 'Kiri' and posisi is not 'Kanan':
                        x1_change = -(snake_block)
                        y1_change = 0
                        posisi = 'Kiri'
                    elif arah == 'Kanan' and posisi is not 'Kiri':
                        x1_change = snake_block
                        y1_change = 0
                        posisi = 'Kanan'
                    elif arah == 'Atas' and posisi is not 'Bawah':
                        y1_change = -(snake_block)
                        x1_change = 0
                        posisi = 'Atas'
                    elif arah == 'Bawah' and posisi is not 'Atas':
                        y1_change = snake_block
                        x1_change = 0
                        posisi = 'Bawah'
            
                    if x1 >= dis_width:
                            x1 = 0
                    elif x1 < 0:
                        x1 = dis_width
                    elif y1 >= dis_height:
                        y1 = 0
                    elif y1 < 0:
                        y1 = dis_height
                            
                    x1 += x1_change
                    y1 += y1_change
                    dis.fill(black)
                    pygame.draw.ellipse(dis, red, [foodx, foody, snake_block, snake_block])
                    snake_Head = []
                    snake_Head.append(x1)
                    snake_Head.append(y1)
                    snake_List.append(snake_Head)
                    if len(snake_List) > Length_of_snake:
                        del snake_List[0]
            
                    for x in snake_List[:-1]:
                        if x == snake_Head:
                            if ((Length_of_snake - 1) > highscore):
                                highscore = (Length_of_snake - 1)
                                file = open('highscore.txt', 'w')
                                file.write(str(highscore))
                                file.close()
                            game_over = True
            
                    our_snake(snake_block, snake_List)
                    Your_score(Length_of_snake - 1)
            
                    pygame.display.update()
            
                    if x1 == foodx and y1 == foody:
                        foodx = round(random.randrange(0, dis_width - snake_block) / 25.0) * 25.0
                        foody = round(random.randrange(0, dis_height - snake_block) / 25.0) * 25.0
                        Length_of_snake += 1
            
                    clock.tick(snake_speed)
                    
                    data =  dis.get_buffer().raw
                    qImg3 = QImage(data,dis_width,dis_height,QImage.Format_RGB32)
                    # self.ui.label_3.setPixmap(QPixmap.fromImage(qImg3))
                    self.gambar.setPixmap(QPixmap.fromImage(qImg3))
                    self.hs.setText(str(highscore))
                        
        except Exception as e:
                print(e)
                pass



class MainWindow(QWidget, QThread):
    # class constructor
    # gerakan = 'Belum diisi'
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.mainWindow2 = QtWidgets.QMainWindow()

        self.game = gaming(self.ui.label_3, self.ui.label_17)
        
        # create a timer
        self.timer = QTimer()
        
        self.timer.timeout.connect(self.viewCam)
        
        self.ui.button.clicked.connect(self.controlTimer)
        self.ui.button_2.clicked.connect(self.openSecondWindow)
        self.game.start()
        
    def openSecondWindow(self):
        self.SecondWindow = QtWidgets.QMainWindow()
        self.ui2 = Ui_SecondWindow()
        self.ui2.setupUi(self.SecondWindow)
        self.SecondWindow.show()
        
    
    def segment(self, image, threshold=30):
        global bg
        diff = cv2.absdiff(bg.astype("uint8"), image)
        thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]
        return thresholded
            
    def pause(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(snake_speed)
        
    def nebak(self):
        # global gerakan
        global arah
        try:
            reshape = np.array(self.resized).reshape(-1,50,50,1)
            reshape = reshape/255
            tebak = model.predict(reshape)
            self.gerakan = kelas[np.argmax(tebak)]
            self.ui.label_4.setText(self.gerakan)
            self.ui.label_5.setText(str(tebak[0][0]))
            self.ui.label_6.setText(str(tebak[0][1]))
            self.ui.label_7.setText(str(tebak[0][2]))
            self.ui.label_8.setText(str(tebak[0][3]))
            self.ui.label_9.setText(str(tebak[0][4]))
            arah = self.gerakan
        except Exception as e:
            print(e)
            pass
    
    # view camera
    def viewCam(self):
        # read image in BGR format
        global bg
        top, right, bottom, left = 80, 410, 330, 660
        ret, frame = self.cap.read()
        frame = cv2.resize(frame, (700,525))
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        clone = frame.copy()
        roi = frame[top:bottom, right:left]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        if bg is None:
            bg = blur
        else:
            hand = self.segment(blur)
            height2, width2 = hand.shape
            qImg2 = QImage(hand.data, width2, height2, hand.strides[0], QImage.Format_Indexed8)
            qImg2 = qImg2.rgbSwapped()
            pixmap2 = QPixmap.fromImage(qImg2)
            pixmap2 = pixmap2.scaled(125, 125, QtCore.Qt.KeepAspectRatio)
            self.ui.label_2.setPixmap(pixmap2)
            self.resized = cv2.resize(hand,(int(hand.shape[0]/5),int(hand.shape[1]/5)))
            self.nebak()
        cv2.rectangle(clone, (left, top), (right, bottom), (0,255,0), 2)
        height, width, channel = frame.shape
        step = channel * width
        qImg = QImage(clone.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        pixmap = pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pixmap)
        
        # print("Pressed")

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.button.setText("Berhenti")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.button.setText("Mulai")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

