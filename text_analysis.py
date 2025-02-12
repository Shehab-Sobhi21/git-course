# Text Analysis

def text_repeting(text):
    """
    method تقوم باخذ مدخل المستخدم بعدها تقوم بعد عدد الكلمات
    """
    return(len(text.split(" ")))


def lins_repeting(text):
    """
    method تقوم بعد عدد الجمل في الفقرة
    """
    return(text.count(".") + text.count(",") + text.count("?")+ text.count("!"))


def rpeted_txets(text):
    """
    method تقوم بعد الكلمات المتكررة
    """
    new_text = text.split(" ")
    counter = {}
    for i in new_text:
        if new_text.count(i) > 1:
            counter[i] = new_text.count(i)
        else:
            continue
    for item in counter.items():
        print(f"{item[0]} => {item[1]}")


def char_repeting(text):
    """
    method تقوم بعد عدد الحروف في الفقرة
    """
    return(len(text))
