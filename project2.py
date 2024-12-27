from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import*
from PyQt5 import QtGui

notes = {
    "Ukraine": {
        "текст": "Украинская девушка",
        "image": "UkraineGirl.jpg"
    },
    "Japan": {
        "текст": "Японская девушка",
        "image": "JapanGirl.jpg"
    },
    "Italy": {
        "текст": "Итальянская девушка",
        "image": "ItalyGirl.jpg"
    }
}

app = QApplication([])

win = QWidget()
win.setWindowTitle("Женщины разных стран")
win.resize(900, 600)

text_label = QLabel("")
text_label.setWordWrap(True)

image_label = QLabel("")
image_label.setFixedSize(300, 300)

list_country = QListWidget()
list_country.addItems(notes.keys())

def show_note():
    key = list_country.selectedItems()[0].text()
    note = notes[key]
    
    text_label.setText(note["текст"])
    
    pixmap = QPixmap(note["image"])
    pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio)
    image_label.setPixmap(pixmap)

list_country.itemClicked.connect(show_note)

layout = QHBoxLayout()

left_col = QVBoxLayout()
left_col.addWidget(QLabel("Список стран:"))
left_col.addWidget(list_country)

right_col = QVBoxLayout()
right_col.addWidget(image_label)
right_col.addWidget(text_label)

layout.addLayout(left_col, stretch=1)
layout.addLayout(right_col, stretch=2)

win.setLayout(layout)

win.show()
app.exec()