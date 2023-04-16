from pracownicy import *
from random import randint
from menu import *
pr = Pracownicy()


def start(n:int=200) -> None:
    '''
    :param n
       funkcja generujaca dane początkowe dla n pracownikow
    '''
    for i in range(n):
        if randint(0,n) %2==0:
            imie = pr_imiona_k[randint(1,len(pr_imiona_k))-1].lower().capitalize()
        else:
            imie = pr_imiona_m[randint(1, len(pr_imiona_m))-1].lower().capitalize()
        nazwisko = pr_nazwiska[randint(1, len(pr_nazwiska))-1].lower().capitalize()
        pensja = randint(1,10)*1000
        pr.dodaj(imie,nazwisko,pensja)


start()
app = QApplication([])
nowe = MainWindow(app,pr)
app.exec_()

