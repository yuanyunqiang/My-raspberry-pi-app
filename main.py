import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_main import Ui_MainWindow
import requests
import json
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
import time
import os

KEY = 'SUW1Fx3ly1EPVrwzd'  # API key
UID = "PmC3hdJllnrgDELPF"  # 用户ID
LOCATION = 'zhongshan'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.tianqi2()
        self.time2()
        self.timer = QTimer()
        self.timer.timeout.connect(self.tianqi2)
        self.timer.start(600*1000)
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.time2)
        self.timer2.start(100)
    def tianqi2(self):
        txt=self.tianqi()
        text = json.loads(txt)
        t=text["results"][0]['now']['text']
        tem=text["results"][0]['now']['temperature']
        self.label_2.setText(tem+"℃ "+t)
        cmd = "sudo ntpdate cn.pool.ntp.org";
        os.system(cmd)

    def tianqi(self):
        result = requests.get(API, params={
            'key': KEY,
            'location': LOCATION,
            'language': LANGUAGE,
            'unit': UNIT
        })
        return result.text

    def time2(self):
        self.label.setText(time.strftime("%H:%M:%S", time.localtime()))
        self.label_4.setText(time.strftime("%Y-%m-%d", time.localtime()))


if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = MainWindow()
    ex.showFullScreen()
    ex.show()
    sys.exit(App.exec_())