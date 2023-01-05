# from PyQt5.QtWidgets import *

# app = QApplication([])
# app.setStyle('Fusion')

# window = QWidget()
# layout = QVBoxLayout()

# label = QLabel("Hello World!")
# text_edit = QLineEdit()
# button = QPushButton('Click')

# layout.addWidget(label)
# layout.addWidget(text_edit)
# layout.addWidget(button)

# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText('You clicked the button!')
#     alert.exec()
# button.clicked.connect(on_button_clicked)

# window.setLayout(layout)
# window.show()

# app.exec_()


# Example to use groupbox.
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QRadioButton

app = QApplication([])

# Create a parent widget and a layout
parent = QWidget()
layout = QVBoxLayout(parent)

# Create a group box and a layout for it
group_box = QGroupBox("Select a fruit:")
group_layout = QVBoxLayout(group_box)

# Add radio buttons to the group box's layout
button1 = QRadioButton("Apple")
button2 = QRadioButton("Banana")
button3 = QRadioButton("Orange")
group_layout.addWidget(button1)
group_layout.addWidget(button2)
group_layout.addWidget(button3)

# Add the group box to the parent's layout
layout.addWidget(group_box)

parent.show()
app.exec_()
