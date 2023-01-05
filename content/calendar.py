from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QTextCharFormat, QBrush
from PyQt5.QtCore import Qt

app = QApplication([])

# Create a parent widget and a layout
parent = QWidget()
layout = QVBoxLayout(parent)

# Create a calendar widget and a label
calendar = QCalendarWidget()
label = QLabel()

# Set the calendar's selection mode to single date
calendar.setSelectionMode(QCalendarWidget.SingleSelection)

def on_date_selected():
    # Get the selected date
    date = calendar.selectedDate()

    # Calculate the time period
    period = 6 * 7  # 3 weeks
    start_date = date
    end_date = start_date.addDays(period)

    # Display the time period in the label
    label.setText(f"Time period: {start_date.toString()} - {end_date.toString()}")

    # Set the calendar's dates to busy or free
    format = QTextCharFormat()
    for i in range(period):
        d = start_date.addDays(i)
        if i < 21:  # Every 3 weeks
            format.setBackground(QBrush(Qt.blue))  # Free
        else:
            format.setBackground(QBrush(Qt.red))  # Busy
        calendar.setDateTextFormat(d, format)
    for i in range (period, period +60):
        day = start_date.addDays(i)
        format.setBackground(QBrush(Qt.white))
        calendar.setDateTextFormat(day, format)
    for i in range (-60,0):
        day = start_date.addDays(i)
        format.setBackground(QBrush(Qt.white))
        calendar.setDateTextFormat(day, format)

# Connect the calendar's selectionChanged signal to a slot
calendar.selectionChanged.connect(on_date_selected)

# Add the calendar and label to the layout
layout.addWidget(calendar)
layout.addWidget(label)

parent.show()
app.exec_()

