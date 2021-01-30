import datetime


def sm(text):
    f = open('classic.txt', 'a')
    f.write(str(text) + '\n\n')
    f.close()


def rm():
    check_date()
    f = open('classic.txt', 'r')
    f2 = open('repeating.txt', 'r')
    f3 = open('repeatDate.txt', 'r')
    text = f.read()
    text2 = f2.read()
    text3 = f3.read()
    final_text = 'повторяющееся сообщение:\nповтор до ' + text3 + '\n\n' + text2 +'\n\nобычное сообщение:\n\n' + text
    f.close()
    f2.close()
    f3.close()
    return final_text


def load_date(text):
    f = open('repeatDate.txt', 'a')
    f.write(str(text))
    f.close()


def srm(text):
    f = open('repeating.txt', 'a')
    f.write(str(text))
    f.close()


def check_date():
    f = open('repeating.txt', 'r')
    text = f.read()
    f2 = open('repeatDate.txt', 'r')
    text2 = f2.readline(10)
    f3 = open('classic.txt', 'r')
    text3 = f3.read()
    f4 = open('classicDate.txt', 'r')
    text4 = f4.readline(10)
    f.close()
    f2.close()
    f3.close()
    f4.close()
    today = str(datetime.date.today())
    if today > text2:
        text = ''
        text2 = ''
    if today > text4:
        text3 = ''
        text4 = today
    f = open('repeating.txt', 'w')
    f2 = open('repeatDate.txt', 'w')
    f.write(text)
    f2.write(text2)
    f3 = open('classic.txt', 'w')
    f4 = open('classicDate.txt', 'w')
    f3.write(text3)
    f4.write(text4)

