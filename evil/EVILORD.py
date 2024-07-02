import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QDateTimeEdit, QComboBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QDateTime, QTimer
import ephem

class StarAltAzApp(QWidget):
    def __init__(self):
        super().__init__()

        # Define star names
        self.star_names = ['Vega', 'Sirius', 'Polaris', 'Aldebaran', 'Arcturus', 'Canopus', 'Rigel', 'Deneb', 'Spica',
                          'Capella', 'Procyon', 'Ahernar', 'Betelgeuse', 'Hadar', 'Altair', 'Acrux', 'Antares', 'Pollux',
                          'Fomalhaut', 'Mimosa', 'Regulus', 'Adhara', 'Castor', 'Shaula', 'Gacrux', 'Bellatrix',
                          'Elnath', 'Miaplacidus', 'Alnair', 'Alnilam', 'Alnitak', 'Alioth', 'Dubhe', 'Mirfak', 'Wezen',
                          'Sargas', 'Kaus Australis', 'Avior', 'Alkaid']

        # Define star coordinates
        self.star_coordinates = {
            'Vega': ('18:36:56.33635', '+38:47:01.2802'),
            'Sirius': ('06:45:08.9173', '-16:42:58.017'),
            'Polaris': ('02:31:47.0752', '+89:15:50.792'),
            'Aldebaran': ('04:35:55.23907', '+16:30:33.4885'),
            'Arcturus': ('14:15:39.6721', '+19:10:56.673'),
            'Canopus': ('06:23:57.1099', '-52:41:44.381'),
            'Rigel': ('05:14:32.2721', '-08:12:05.8981'),
            'Deneb': ('20:41:25.9168', '+45:16:49.2203'),
            'Spica': ('13:25:11.5783', '-11:09:40.7506'),
            'Capella': ('05:16:41.3585', '+45:59:52.7692'),
            'Procyon': ('07:39:18.1195', '+05:13:29.9552'),
            'Ahernar': ('01:37:42.8455', '-57:14:12.3108'),
            'Betelgeuse': ('05:55:10.3054', '+07:24:25.4304'),
            'Hadar': ('14:39:35.9452', '-60:49:33.946'),
            'Altair': ('19:50:46.9988', '+08:52:05.9563'),
            'Acrux': ('12:26:35.8952', '-63:05:56.734'),
            'Antares': ('16:29:24.4597', '-26:25:55.2092'),
            'Pollux': ('07:45:18.9496', '+28:01:34.316'),
            'Fomalhaut': ('22:57:39.0462', '-29:37:20.0504'),
            'Mimosa': ('12:47:43.5642', '-59:41:19.7579'),
            'Regulus': ('10:08:22.3107', '+11:58:01.9503'),
            'Adhara': ('06:58:37.5488', '-28:58:19.5096'),
            'Castor': ('07:34:36.8693', '+31:53:18.1797'),
            'Shaula': ('17:33:36.5115', '-37:06:13.761'),
            'Gacrux': ('12:31:09.9447', '-57:06:47.7506'),
            'Bellatrix': ('05:25:07.8772', '+06:20:59.955'),
            'Elnath': ('05:26:17.5133', '+28:36:26.748'),
            'Miaplacidus': ('09:13:12.0589', '-69:43:01.8755'),
            'Alnair': ('22:08:13.9849', '-46:57:39.0147'),
            'Alnilam': ('05:36:12.8131', '-01:12:06.9087'),
            'Alnitak': ('05:40:45.528', '-01:56:33.2606'),
            'Alioth': ('12:54:01.661', '+55:57:35.4814'),
            'Dubhe': ('11:03:43.6712', '+61:45:03.208'),
            'Mirfak': ('03:24:19.3702', '+49:51:40.157'),
            'Wezen': ('07:08:23.4594', '-26:23:35.9695'),
            'Sargas': ('17:37:19.1291', '-42:59:52.3693'),
            'Kaus Australis': ('18:24:10.3226', '-34:23:04.0482'),
            'Avior': ('08:22:30.8317', '-59:30:34.1062'),
            'Alkaid': ('13:47:32.6258', '+49:18:47.2372')
        }

        self.initUI()
        self.startupAnimation()

    def initUI(self):
        self.setWindowTitle('EVILORD SATRS')
        self.setGeometry(100, 100, 1240, 720)  # Increased size

        # Set background image
        pixmap = QPixmap('BACK.png')
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        # Logo
        logo_label = QLabel(self)
        logo_pixmap = QPixmap('')  # Replace 'logo.png' with the path to your logo file
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        # Location input
        location_label = QLabel('Enter your location (longitude, latitude) in degrees separated by comma:')
        self.location_edit = QLineEdit()
        location_layout = QHBoxLayout()
        location_layout.addWidget(location_label)
        location_layout.addWidget(self.location_edit)

        # Date input
        date_label = QLabel('Select date:')
        self.date_edit = QDateTimeEdit()
        self.date_edit.setDateTime(QDateTime.currentDateTime())
        self.date_edit.setCalendarPopup(True)
        date_layout = QHBoxLayout()
        date_layout.addWidget(date_label)
        date_layout.addWidget(self.date_edit)

        # Time input
        time_label = QLabel('Select time:')
        self.time_edit = QDateTimeEdit()
        self.time_edit.setDateTime(QDateTime.currentDateTime())
        self.time_edit.setTimeSpec(Qt.UTC)
        self.time_edit.setDisplayFormat("HH:mm:ss")
        time_layout = QHBoxLayout()
        time_layout.addWidget(time_label)
        time_layout.addWidget(self.time_edit)

        # Star name input
        star_label = QLabel('Select the name of the star:')
        self.star_combo = QComboBox()  # Changed to QComboBox
        self.star_combo.addItems(self.star_names)
        star_layout = QHBoxLayout()
        star_layout.addWidget(star_label)
        star_layout.addWidget(self.star_combo)

        # Compute button
        self.compute_button = QPushButton('LET GO EVILORD')
        self.compute_button.clicked.connect(self.computeAltAz)
        compute_layout = QHBoxLayout()
        compute_layout.addWidget(self.compute_button)

        # Results display
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        self.results_text.setStyleSheet("background-image: url('OUTPUT.jpg'); color: white; font-size: 20px; font-weight: bold;") # Set background image, text color, font size, and weight

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(logo_label)
        main_layout.addLayout(location_layout)
        main_layout.addLayout(date_layout)
        main_layout.addLayout(time_layout)
        main_layout.addLayout(star_layout)
        main_layout.addLayout(compute_layout)
        main_layout.addWidget(self.results_text)

        self.setLayout(main_layout)

    def startupAnimation(self):
        self.setWindowOpacity(0.0)
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.increaseOpacity)
        self.animation_timer.start(50)

    def increaseOpacity(self):
        current_opacity = self.windowOpacity()
        new_opacity = min(current_opacity + 0.05, 1.0)
        self.setWindowOpacity(new_opacity)
        if new_opacity == 1.0:
            self.animation_timer.stop()

    def computeAltAz(self):
        location_str = self.location_edit.text()
        date = self.date_edit.date().toString(Qt.ISODate)
        time = self.time_edit.time().toString(Qt.DefaultLocaleLongDate)
        star_name = self.star_combo.currentText()

        try:
            location = tuple(map(float, location_str.split(',')))
            date_time_str = f"{date} {time}"
            date_time = ephem.Date(date_time_str)

            observer = ephem.Observer()
            observer.lon, observer.lat = location
            observer.date = date_time

            # Get star coordinates
            ra_str, dec_str = self.star_coordinates.get(star_name, (None, None))
            if ra_str is None:
                raise ValueError(f"Star '{star_name}' not found in the database")

            star = ephem.FixedBody()
            star._ra = ra_str
            star._dec = dec_str

            star.compute(observer)

            altitude = star.alt * 180 / ephem.pi
            azimuth = star.az * 180 / ephem.pi

            result_str = f"Altitude: {altitude:.2f} degrees\nAzimuth: {azimuth:.2f} degrees\n HERE IS THE LOCATION...<3\n YOU NEED TO GO {altitude:.2f} LEFT \n AND {azimuth:.2f} UP FRO THE NORTH SIDE"
            self.results_text.setPlainText(result_str)
        except Exception as e:
            self.results_text.setPlainText(f"Error: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StarAltAzApp()
    ex.show()
    sys.exit(app.exec_())
