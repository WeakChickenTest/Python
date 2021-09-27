import pyttsx3


class yuyin:
    def __init__(self, neirong):
        self.neirong = neirong

    def bofang(self):
        engine = pyttsx3.init()
        engine.say(self.neirong)
        engine.runAndWait()


txt = open(r"语音朗读.txt", encoding="UTF-8")
for i in txt:
    print(i)
    a = yuyin(i)
    a.bofang()
