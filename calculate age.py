from PyQt6.QtWidgets import QApplication, QVBoxLayout, \
    QLabel, QWidget, QGridLayout, QLineEdit, QPushButton  # Import Qt widgets for GUI
from datetime import datetime  # Import datetime for date operations
import sys  # Import sys for system operations

class AgeCalculator(QWidget):
    """Main widget class for age calculation application with grid layout"""

    def __init__(self,):
        """Initialize UI: create widgets, set up grid layout, and connect signals"""
        super().__init__()
        self.setWindowTitle(("age calculator"))
        grid = QGridLayout()  # Create grid layout for structured widget placement

        #Create widgets
        name_label = QLabel("name:")
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel("Date of birth mm/dd/yyyy:")
        self.date_birth_line_edit =  QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)  # Connect button click to calculation method
        self.output_label = QLabel("")

        #Add widgets to grid (row, column, rowSpan, colSpan)
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)  # Span 2 columns
        grid.addWidget(self.output_label, 3, 0, 1, 2)  # Span 2 columns

        self.setLayout(grid)

    def calculate_age(self):
        """Calculate age based on current year and user input, display result"""
        current_year = datetime.now().year  # Get current year
        date_of_birth = self.date_birth_line_edit.text()  # Get DOB from input
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").year  # Parse and extract year
        age = current_year - year_of_birth  # Calculate age
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")  # Display result

app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())