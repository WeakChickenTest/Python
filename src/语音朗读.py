import pyttsx3


class yuyin:
    def __init__(self, neirong):
        self.neirong = neirong

    def bofang(self):
        engine = pyttsx3.init()
        engine.say(self.neirong)
        engine.runAndWait()


a = yuyin("天……天上有个太阳~，水中有个月亮")
a.bofang()
