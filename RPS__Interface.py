from RPS__main import *
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Rock Paper Scissor")

        stone = "rock-576669_1280.png"
        score_layout = qtw.QHBoxLayout()
        input_layout = qtw.QHBoxLayout()
        graphics_layout = qtw.QHBoxLayout()

        # Pc Score
        pc_score = qtw.QLabel("PC: 0")
        score_layout.addWidget(pc_score)

        # User Score
        user_score =  qtw.QLabel("User: 0")
        score_layout.addWidget(user_score, alignment=Qt.AlignRight)

        self.layout().addLayout(score_layout)

        visuals = qtw.QLabel("Start Game!")
        visuals.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(visuals)

        #Image Layout
        self.im = qtg.QPixmap("./logo.png")
        self.label = qtw.QLabel()
        new_size = self.im.scaled(200, 200, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.label.setPixmap(new_size)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.label)
        self.label.setContentsMargins(20, 30, 20, 30)
        

        # rock button
        rock_button = qtw.QPushButton("Rock", clicked=lambda: press("r"))
        rock_button.setToolTip("Rock: Shortcut - 1")
        rock_button.setShortcut(qtg.QKeySequence("1"))
        input_layout.addWidget(rock_button)

        # paper button
        paper_button = qtw.QPushButton("Paper", clicked=lambda: press("p"))
        paper_button.setShortcut(qtg.QKeySequence("2"))
        paper_button.setToolTip("Paper: Shortcut - 2")
        input_layout.addWidget(paper_button)

        # Scissor button
        scissor_button = qtw.QPushButton("Scissor", clicked=lambda: press("s"))
        scissor_button.setShortcut(qtg.QKeySequence("3"))
        scissor_button.setToolTip("Scissor: Shortcut - 3")
        input_layout.addWidget(scissor_button)

        self.layout().addLayout(input_layout)


        self.user_scor=0
        self.pc_scor = 0 
        self.dict= {"r":"Rock", "p":"Paper", "s":"Scissor"}
        self.load_sounds()

        
        def press(x):
            res = rps(x)
            if res[1]=="r":
                new_image_path = "./rock.png"  # Replace with your new image path
                new_im = qtg.QPixmap(new_image_path)
                new_size = new_im.scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
                self.label.setPixmap(new_size)
                shadow = qtw.QGraphicsDropShadowEffect() 
                shadow.setBlurRadius(15)
                self.label.setGraphicsEffect(shadow)

            if res[1]=="p":
                new_image_path = "./paper.png"  # Replace with your new image path
                new_im = qtg.QPixmap(new_image_path)
                new_size = new_im.scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
                self.label.setPixmap(new_size)
                shadow = qtw.QGraphicsDropShadowEffect() 
                shadow.setBlurRadius(15)
                self.label.setGraphicsEffect(shadow)

            if res[1] == "s":
                new_image_path = "./scissor.png"  # Replace with your new image path
                new_im = qtg.QPixmap(new_image_path)
                new_size = new_im.scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
                self.label.setPixmap(new_size)
                shadow = qtw.QGraphicsDropShadowEffect() 
                shadow.setBlurRadius(15)
                self.label.setGraphicsEffect(shadow)

            if res[0] == 1:
                self.user_scor +=1
                self.play_sound("sound1")
                user_score.setText(f"User: {self.user_scor}")
                visuals.setText(f"The Computer Said: {self.dict[res[1]]}")
            elif res[0] == 0:
                self.pc_scor +=1
                self.play_sound("sound2")
                pc_score.setText(f"PC: {self.pc_scor}")
                visuals.setText(f"The Computer Said: {self.dict[res[1]]}")
            else:
                self.play_sound("sound3")
                visuals.setText(f"The Computer Said: {self.dict[res[1]]}")

        self.setMaximumSize(300, 200)
        self.show()

        
    def load_sounds(self):
        self.media_player = QMediaPlayer()

        self.sound_effects = {
            "sound1": QMediaContent(QUrl.fromLocalFile("./win_sound.wav")),
            "sound3": QMediaContent(QUrl.fromLocalFile("./Eh Sound.wav")),
            "sound2": QMediaContent(QUrl.fromLocalFile("./Lost Sound.wav"))
        }

    def play_sound(self, sound_name):
        media_content = self.sound_effects.get(sound_name)
        if media_content:
            self.media_player.setMedia(media_content)
            self.media_player.play()

        
        
app = qtw.QApplication([])
style = """
    QPushButton{
       border-radius: 4px;
       background-color:#704F4F;
       padding: 6px 6px 6px 6px;
       font-size: 11px;
       font-family: roboto;
       color: white;
       letter-spacing: 1px;
     } 

     QLabel{
     font-size: 16px;
     font-family: Roboto;
     font-weight: semi-bold;
     letter-spacing: 1px;
     }

     QLabel #img{
     box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.5);
     }
"""

app.setStyleSheet(style)
app.setStyle("Fusion")
mw = MainWindow()
app.exec_()


#Implement Timing Function

