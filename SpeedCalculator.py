import sys
from PyQt6.QtWidgets import QApplication, QComboBox, \
    QLabel, QWidget, QGridLayout, QLineEdit, QPushButton 


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        #Create Windgets
        distance_label = QLabel("distance:")
        self.distance_input = QLineEdit()

        time_label = QLabel("Time:")
        self.time_input = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Metic (km)", "Imperial (miles)"])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)

        self.result_label = QLabel("")

        #Add wifgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        #Get distance and time from the input boxes
        distance = float(self.distance_input.text())
        time = float(self.time_input.text())

        #Calculate average speed
        speed = distance / time

        #Check what user chose in the combo 
        if self.unit_combo.currentText() == "Metric (km)":
            speed = round(speed, 2)
            unit = "km/h"
        else:
            speed = round(speed * 0.6213, 2)
            unit = "mph"

        #Display the result
        self.result_label.setText(f"Average Speed:{speed} {unit}")

app = QApplication(sys.argv)
calculator = SpeedCalculator()
calculator.show()
sys.exit(app.exec())