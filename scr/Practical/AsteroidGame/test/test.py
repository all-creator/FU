data = {"stavka1": '!', "stavka2": [1, 40]}


class TextArea:
    def __init__(self, text__="", start=0, end=0, step=1, name=""):
        self.text = text__
        self.start = start
        self.end = end
        self.step = step
        self.name = name
        self.numbers = []

    def get_val(self):
        self.gen_row()
        return self.text, self.numbers, self.name

    def gen_row(self):
        for i in range(self.start, self.end, self.step):
            self.numbers.append(i)


textarea1 = TextArea("1", 0, 10, 1, name="баскетбол")
textarea2 = TextArea("", 0)
textarea3 = TextArea("30", 1, 7, 3, name="футбол")
textarea4 = TextArea("", 0)
textarea5 = TextArea("", 0)

texts = [textarea1.get_val(), textarea2.get_val(), textarea3.get_val(), textarea4.get_val(), textarea5.get_val()]


def some_action(text_):
    print(f"Вы поставили на {text_[0]} с коэффициентами {text_[1]} на игру {text_[2]}")


for text in texts:
    if text[0] is None or text[0] == "":
        continue
    some_action(text)
