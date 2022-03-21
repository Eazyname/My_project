import datetime


def good():
    a = input()
    print(a + " good day" + str(datetime.datetime.now().day))

good()


