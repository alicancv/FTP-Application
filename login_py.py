from PyQt5 import QtCore, QtGui, QtWidgets
import FTP_Controller

class Ui_Window(object):
    def setupUi(self, Window):
        self.window = Window
        Window.setObjectName("Window")
        Window.resize(200, 200)
        self.user_line = QtWidgets.QLineEdit(Window)
        self.user_line.setGeometry(QtCore.QRect(40, 30, 113, 22))
        self.user_line.setText("")
        self.user_line.setObjectName("user_line")
        self.password_line = QtWidgets.QLineEdit(Window)
        self.password_line.setGeometry(QtCore.QRect(40, 70, 113, 22))
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.host_line = QtWidgets.QLineEdit(Window)
        self.host_line.setGeometry(QtCore.QRect(40, 110, 113, 22))
        self.host_line.setText("")
        self.host_line.setObjectName("host_line")
        self.pushButton = QtWidgets.QPushButton(Window)
        self.pushButton.setGeometry(QtCore.QRect(50, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.greeting = QtWidgets.QLabel(Window)
        self.greeting.setGeometry(QtCore.QRect(480, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.greeting.setFont(font)
        self.greeting.setObjectName("greeting")
        self.current_path = QtWidgets.QLabel(Window)
        self.current_path.setEnabled(True)
        self.current_path.setGeometry(QtCore.QRect(10, 0, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.current_path.setFont(font)
        self.current_path.setObjectName("current_path")
        self.upload_button = QtWidgets.QPushButton(Window)
        self.upload_button.setGeometry(QtCore.QRect(640, 60, 151, 41))
        self.upload_button.setObjectName("upload_button")
        self.download_button = QtWidgets.QPushButton(Window)
        self.download_button.setGeometry(QtCore.QRect(640, 110, 151, 41))
        self.download_button.setObjectName("download_button")
        self.createdir_button = QtWidgets.QPushButton(Window)
        self.createdir_button.setGeometry(QtCore.QRect(640, 160, 151, 41))
        self.createdir_button.setObjectName("createdir_button")
        self.delete_button = QtWidgets.QPushButton(Window)
        self.delete_button.setGeometry(QtCore.QRect(640, 210, 151, 41))
        self.delete_button.setObjectName("delete_button")
        self.rename_button = QtWidgets.QPushButton(Window)
        self.rename_button.setGeometry(QtCore.QRect(640, 260, 151, 41))
        self.rename_button.setObjectName("rename_button")
        self.name_of = QtWidgets.QLineEdit(Window)
        self.name_of.setGeometry(QtCore.QRect(390, 400, 221, 31))
        self.name_of.setObjectName("name_of")
        self.label = QtWidgets.QLabel(Window)
        self.label.setGeometry(QtCore.QRect(20, 400, 391, 31))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Window)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 611, 351))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(Window)
        self.label_2.setGeometry(QtCore.QRect(640, 305, 141, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Window)
        self.label_3.setGeometry(QtCore.QRect(640, 330, 141, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Window)
        self.label_4.setGeometry(QtCore.QRect(640, 360, 141, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Window)
        self.label_5.setGeometry(QtCore.QRect(640, 390, 141, 31))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
        
        self.greeting.setVisible(False)
        self.current_path.setVisible(False)
        self.listWidget.setVisible(False)
        self.upload_button.setVisible(False)
        self.download_button.setVisible(False)
        self.createdir_button.setVisible(False)
        self.delete_button.setVisible(False)
        self.rename_button.setVisible(False)
        self.name_of.setVisible(False)
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        
        self.ftp = FTP_Controller.FTP_Controller()
        self.pushButton.clicked.connect(self.login)
        self.upload_button.clicked.connect(self.upload_file)
        self.download_button.clicked.connect(self.download_file)
        self.createdir_button.clicked.connect(self.create_directory)
        self.delete_button.clicked.connect(self.delete_file_or_directory)
        self.rename_button.clicked.connect(self.rename_file_or_directory)
        self.listWidget.itemDoubleClicked.connect(self.travel)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "171180062 - FTP Client"))
        self.user_line.setPlaceholderText(_translate("Window", "user name"))
        self.password_line.setPlaceholderText(_translate("Window", "password"))
        self.host_line.setPlaceholderText(_translate("Window", "host ip"))
        self.pushButton.setText(_translate("Window", "Login"))
        self.greeting.setText(_translate("Window", "Welcome User!!!"))
        self.current_path.setText(_translate("Window", "PATH"))
        self.upload_button.setText(_translate("Window", "Upload File"))
        self.download_button.setText(_translate("Window", "Download File"))
        self.createdir_button.setText(_translate("Window", "Create Directory"))
        self.delete_button.setText(_translate("Window", "Delete File/Directory"))
        self.rename_button.setText(_translate("Window", "Rename File/Directory"))
        self.label.setText(_translate("Window", "Write name of the directory/file before creating or renaming it:"))
        self.label_2.setText(_translate("Window", "Alican Sucu"))
        self.label_3.setText(_translate("Window", "171180062"))
        self.label_4.setText(_translate("Window", "Computer Networks"))
        self.label_5.setText(_translate("Window", "Homework 5"))
    
    def login(self):     
        self.user_name = self.user_line.text();
        self.password = self.password_line.text();
        self.host = self.host_line.text();
        self.ftp.login(self.host, 21, self.user_name, self.password)
        
        self.user_line.setVisible(False)
        self.password_line.setVisible(False) 
        self.host_line.setVisible(False)
        self.pushButton.setVisible(False)
        
        self.show_files(self.ftp.current_wdir())
        self.window.resize(800, 440)
        
        self.current_path.setVisible(True)
        self.greeting.setVisible(True)
        self.listWidget.setVisible(True) 
        self.upload_button.setVisible(True)
        self.download_button.setVisible(True)
        self.createdir_button.setVisible(True)
        self.delete_button.setVisible(True)
        self.rename_button.setVisible(True)
        self.name_of.setVisible(True)
        self.label.setVisible(True)
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.label_4.setVisible(True)
        self.label_5.setVisible(True)

        self.greeting.setText(f"Welcome {self.user_name} !!!")
        
    def show_files(self, remote_path = ""):
        self.listWidget.clear()
        files = self.ftp.show_dir(remote_path)
        self.listWidget.addItems(files)
        self.current_path.setText(f"path: {remote_path}") 
        
    def upload_file(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(None, 'Upload a file','',"All files (*)")
        self.ftp.upload_file(file_name[0], self.ftp.current_wdir())
        self.show_files(self.ftp.current_wdir())
        
    def download_file(self):
        current_dir = self.ftp.current_wdir()
        self.ftp.download_file("", current_dir + self.listWidget.currentItem().text() if current_dir == "/" else current_dir + "/" + self.listWidget.currentItem().text() )
        
    def create_directory(self):      
        self.ftp.make_dir(self.name_of.text() if self.name_of.text() != "" else "New Directory",
                          self.ftp.current_wdir())
        self.show_files(self.ftp.current_wdir())
    
    def delete_file_or_directory(self):
        current_dir = self.ftp.current_wdir()
        self.ftp.remove_file_or_dir(current_dir + self.listWidget.currentItem().text() if current_dir == "/" else current_dir + "/" + self.listWidget.currentItem().text() )
        self.show_files(self.ftp.current_wdir())
        
    def rename_file_or_directory(self):
        current_dir = self.ftp.current_wdir()
        self.ftp.rename_file_or_dir(self.name_of.text(), current_dir + self.listWidget.currentItem().text() if current_dir == "/" else current_dir + "/" + self.listWidget.currentItem().text() )
        self.show_files(self.ftp.current_wdir())
        
    def travel(self):
        try:
            current_dir = self.ftp.current_wdir()
            self.ftp.change_dir(current_dir + self.listWidget.currentItem().text() if current_dir == "/" else current_dir + "/" + self.listWidget.currentItem().text())    
            self.show_files(self.ftp.current_wdir())
        except:
            print("Element is not a directory")    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

