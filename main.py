import mp3play

import os
from PyQt5.QtWidgets import*

from PyQt5.QtCore import Qt # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap # оптимізована для показу на екрані картинка


 
app = QApplication([])
win = QWidget()      
win.resize(700, 500)
win.setWindowTitle('Easy Editor')
lb_music = QLabel("MUSIC")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()
 
btn_left = QPushButton("START")
btn_right = QPushButton("STOP")
btn_flip = QPushButton("NEXT")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")
 
row = QHBoxLayout()          # Головна лінія
col1 = QVBoxLayout()         # ділиться на два стовпці
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      # в першому - кнопка вибору каталогу
col1.addWidget(lw_files)     # і список файлов
col2.addWidget(lb_music, 95) # в другому - картинка
row_tools = QHBoxLayout()    # і ряд кнопок
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)
 
row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

app.setStyleSheet('''
QWidget{
color: black;
font-size: 15px;
font-weight: bold;
border-radius: 2px;
padding: 5px;
} 

''')

win.show()
 
workdir = ''
 
def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result
 
def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()
 
def showFilenamesList():
   extensions = ['.mp3']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
 
   lw_files.clear()
   for filename in filenames:
       lw_files.addItem(filename)
 
btn_dir.clicked.connect(showFilenamesList)

# другий урок
class MusicProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
    
    def loadMusic(self, dir, filename):
        ''' під час завантаження запам'ятовуємо шлях та ім'я файлу '''
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        return image_path
    
    def playMusic(self, name):
        res = name
        filename = self.loadMusic(self.dir, self.filename)
        clip = mp3play.load(filename)
        clip.play()


musico = MusicProcessor() 

def playChosenMus():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        musico.loadMusic(workdir, filename)
        musico.playMusic(filename)
        # image_path = os.path.join(workimage.dir, workimage.filename)
        # workimage.showImage(image_path)

lw_files.currentRowChanged.connect(playChosenMus)

app.exec()