from PyQt5 . QtWidgets import QApplication, QMessageBox ,QListWidget,QCheckBox , QWidget , QPushButton , QVBoxLayout,QLabel, QDialog , QLineEdit
from PyQt5 import QtCore
from wykresy import wykres
import sys
import pliki

class Lista(QListWidget):

   def Clicked(self,item):
      QMessageBox.information(self, "ListWidget",item.text())


class Dodaj(QDialog):
    '''
    okno dialogowe z polami do dodania informacji o nowym pracowniku
    '''
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.imie = QLineEdit("")
        self.l1 = QLabel("IMIE")
        self.nazwisko = QLineEdit("")
        self.l2 = QLabel("NAZWISKO")
        self.pensja = QLineEdit("")
        self.l3 = QLabel("PENSJA")
        self.button = QPushButton('Dodaj')
        self.button.clicked.connect(self.accept)
        self.layout.addWidget(self.l1)
        self.layout.addWidget(self.imie)
        self.layout.addWidget(self.l2)
        self.layout.addWidget(self.nazwisko)
        self.layout.addWidget(self.l3)
        self.layout.addWidget(self.pensja)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


class Pliki(QDialog):
    '''
    klasa do obslugi okna zwiazanego z plikami
    '''
    def __init__(self,b):
        '''
        :param b: tryb dzialania 'r' - odczyt, 'w' - zapis
        '''
        super().__init__()
        self.layout = QVBoxLayout()
        self.nazwa = QLineEdit("")
        self.l1 = QLabel("Podaj nazwe pliku")
        if b =='r': self.button = QPushButton('wczytaj')
        elif b=='w':    self.button = QPushButton('Zapisz')
        self.button.clicked.connect(self.accept)
        self.layout.addWidget(self.l1)
        self.layout.addWidget(self.nazwa)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


class Usun(QDialog):
    '''
    klasa do obslugi okna zwiazanego z usuwaniem pracownikow
    '''
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.id = QLineEdit("")
        self.l1 = QLabel("Wpisz id")
        self.all = QCheckBox("Usun wszystkich")
        self.button = QPushButton('usun')
        self.button.clicked.connect(self.accept)
        self.layout.addWidget(self.l1)
        self.layout.addWidget(self.id)
        self.layout.addWidget(self.all)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

class Wyswietl(QDialog):
    '''
    klasa do wyswietlania listy pracownikow
    '''
    def __init__(self,_pr):
        super().__init__()
        self.pr = _pr
        self.layout = QVBoxLayout()
        self.lista = Lista()
        self.button = QPushButton('OK')
        self.button.clicked.connect(self.accept)
        self.layout.addWidget(self.lista)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        for i in range(len(self.pr.pracownicy)):
            self.lista.addItem(self.pr.wyswietl_i(i))
        self.lista.itemClicked.connect(self.lista.Clicked)


class OK(QDialog):
    '''
    klasa do okna z rezultatem operacji
    '''
    def __init__(self,b:bool):
        '''

        :param b: True or False, powodzenie lub niepowodzenie operacji
        '''
        super().__init__()
        self.layout = QVBoxLayout()
        if b:   self.l1 = QLabel("Pomyslnie wykonano operacje")
        else:   self.l1 = QLabel("Nie udało się")
        self.button = QPushButton('OK')
        self.button.clicked.connect(self.accept)
        self.layout.addWidget(self.l1)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


class MainWindow(QWidget):
    '''
    klasa glownego menu aplikacji
    '''
    def __init__(self,app,pr):
        '''

        :param app: aplikacja
        :param pr: obiekt dla listy z obiektami pracownikow
        '''
        super().__init__()
        self.prac = pr
        self.setGeometry(200, 200, 300, 300)
        self.layout = QVBoxLayout()
        self.button = QPushButton('Dodaj pracownika')
        self.button2 = QPushButton('Usun pracownika')
        self.button3 = QPushButton('Wyswietl pracownikow')
        self.button4 = QPushButton('Wyswietl histogram pensji')
        self.button6 = QPushButton('Zapisz do pliku XML')
        self.button7 = QPushButton('Wczytaj z pliku XML')
        self.button5 = QPushButton('Wyjdz')
        self.button.clicked.connect(self.dodaj)
        self.button2.clicked.connect(self.usun)
        self.button3.clicked.connect(self.wyswietl)
        self.button4.clicked.connect(self.Wykres)
        self.button5.clicked.connect(self.Koncz)
        self.button7.clicked.connect(self.Wczytaj)
        self.button6.clicked.connect(self.Zapisz)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button6)
        self.layout.addWidget(self.button7)
        self.layout.addWidget(self.button5)
        self.setLayout(self.layout)
        self.show()


    def dodaj(self):
        '''
        metoda wykonujaca polecenie dodawania
        :return:
        '''
        dial = Dodaj()
        if dial.exec_() == QDialog.Accepted:

            dial1 = OK(self.prac.dodaj(dial.imie.text(),dial.nazwisko.text(), dial.pensja.text()))
            dial1.exec_()
    def usun(self):
        '''
               metoda wykonujaca polecenie usuwania
               :return:
               '''
        dial = Usun()
        if dial.exec_() == QDialog.Accepted:
            if dial.all.isChecked():
                dial1 = OK(self.prac.usun('all'))
            else:
                dial1 = OK(self.prac.usun(int(dial.id.text())))
            dial1.exec_()

    def wyswietl(self):
        '''
               metoda wykonujaca polecenie wyswietlania
               :return:
               '''
        dial = Wyswietl(self.prac)
        dial.exec_()

    def Wykres(self):
        '''
               metoda rysujaca wykres
               :return:
               '''
        wykres(self.prac.pracownicy)

    def Wczytaj(self):
        '''
               metoda wczytujaca dane z pliku xml
               :return:
               '''
        dial = Pliki('r')
        dial.exec_()
        dial1 = OK(pliki.wczytaj(self.prac,dial.nazwa.text()))
        dial1.exec_()


    def Zapisz(self):
        '''
               metoda zapisujaca do pliku xml
               :return:
               '''
        dial = Pliki('w')
        dial.exec_()
        dial1 = OK(pliki.zapis(self.prac, dial.nazwa.text()))
        dial1.exec_()

    def Koncz(self):
        '''
               metoda wykonujaca polecenie zakonczenia programu
               :return:
               '''
        sys.exit()


