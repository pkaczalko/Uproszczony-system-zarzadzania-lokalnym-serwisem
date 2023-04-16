class pracownik:
    aktualneId = 0

    def __init__(self,_imie,_nazwisko,_pensja,_id = - 1):
        '''
        konstruktor dla obiektów klasy pracownik
        :param _imie:
        :param _nazwisko:
        :param _pensja:
        :param _id:
        '''
        pracownik.aktualneId += 1
        if _id!= -1:
            self.__id=_id
        else:
            self.__id = pracownik.aktualneId

        self.__imie = _imie
        self.__nazwisko = _nazwisko
        self.__pensja = _pensja

    @property
    def imie(self):
        return self.__imie

    @property
    def id(self):
        return self.__id

    @imie.setter
    def imie(self, _imie):
        self.__imie = _imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @nazwisko.setter
    def nazwisko(self, _nazwisko):
        self.__nazwisko = _nazwisko

    @property
    def pensja(self):
        return self.__pensja

    @pensja.setter
    def pensja(self, _pensja):
        self.__pensja = _pensja


class Pracownicy:
    '''klasa przechowujaca tablice pracownikow i metody do jej obslugi'''
    def __init__(self):
        '''
        konstruktor dla listy pracownikow
        '''
        self.pracownicy = []

    def dodaj(self, _imie = 'Jan', _nazwisko = 'Kowalski', _pensja = 1250,_id=-1):
        '''
        metoda dodajaca obiekt pracownika
        :param self:
        :param _imie: imie pracownika
        :param _nazwisko: nazwisko pracownika
        :param _pensja: pensja pracownika
        :param _id: unikalne id pracownika
        :return:
        '''
        try:
            if _imie =='' or _nazwisko=='' or _pensja=='':  raise Exception
            nowy = pracownik(_imie, _nazwisko, _pensja,_id)
            self.pracownicy.append(nowy)
        except:
            return False
        return True

    def usun(self, _id):
        '''
        metoda do usuwania obiektu
        :param self:
        :param _id: id do usuniecia, gdy rowny 'all' zamiast jednego obiektu, usuwa cala liste
        :return:
        '''
        try:
            del self.pracownicy[_id-1]
            return True
        except:
            if(_id == 'all'):
                del self.pracownicy[:]
                return True
            return False

    def wyswietl(self):
        '''metoda wyswietlajaca dane wszystkich pracownikow'''
        for t in self.pracownicy:
            print(t.id, t.imie, t.nazwisko, t.pensja)


    def wyswietl_i(self,index:int)->str:
        '''
        funkcja zwracajaca dane pojedynczego pracownika
        :param self: obiekt klasy Pracownicy
        :param index: indeks na liscie
        :return: string
        '''
        t = self.pracownicy[index]
        return 'id: '+ str(t.id)+' imie: '+t.imie+' nazwisko: '+t.nazwisko+' pensja: '+str(t.pensja)



pr_imiona_k = ("ANNA","MARIA","KATARZYNA","MAŁGORZATA","AGNIESZKA","BARBARA","EWA","KRYSTYNA","MAGDALENA","ELŻBIETA","JOANNA","ALEKSANDRA","ZOFIA","MONIKA","TERESA","DANUTA","NATALIA","JULIA","KAROLINA","MARTA","BEATA","DOROTA","HALINA","JADWIGA","JANINA","ALICJA","JOLANTA","GRAŻYNA","IWONA","IRENA","PAULINA","JUSTYNA","ZUZANNA","BOŻENA","WIKTORIA","URSZULA","RENATA","HANNA","SYLWIA","AGATA","HELENA","PATRYCJA","MAJA","IZABELA","EMILIA","ANETA","WERONIKA","EWELINA","OLIWIA","MARTYNA","KLAUDIA","MARIANNA","MARZENA","GABRIELA","STANISŁAWA","DOMINIKA","KINGA","LENA","EDYTA","AMELIA","WIESŁAWA","KAMILA","WANDA","ALINA","LIDIA","LUCYNA","MARIOLA","NIKOLA","MIROSŁAWA","WIOLETTA","MILENA","DARIA","ANGELIKA","KAZIMIERA","GENOWEFA","BOGUMIŁA","ANTONINA","LAURA","OLGA","SANDRA","HENRYKA","ILONA","JÓZEFA","STEFANIA","MICHALINA","SABINA","BOGUSŁAWA","MARLENA","REGINA","NADIA","ŁUCJA","ANITA","KORNELIA","WŁADYSŁAWA","CZESŁAWA","ANIELA","IGA","LILIANA","JAGODA","MARCELINA","NINA","POLA","WIOLETA","ADRIANNA","ROKSANA","KARINA","DAGMARA","CECYLIA","MALWINA","SARA","LEOKADIA","ZDZISŁAWA","ŻANETA","ELIZA")

pr_imiona_m = ("JERZY","GRZEGORZ","WOJCIECH","MARCIN","KAZIMIERZ","TADEUSZ","ŁUKASZ","MARIAN","ANTONI","FRANCISZEK","ZBIGNIEW","JAKUB","ROBERT","RYSZARD","JACEK","HENRYK","MATEUSZ","JANUSZ","MACIEJ","WŁADYSŁAW","KAROL","MARIUSZ","RAFAŁ","ROMAN","DARIUSZ","ALEKSANDER","SEBASTIAN","STEFAN","EDWARD","MIROSŁAW","ARTUR","KAMIL","MIECZYSŁAW","DAWID","SŁAWOMIR","WIESŁAW","DANIEL","SZYMON","MIKOŁAJ","JAROSŁAW","DOMINIK","CZESŁAW","LESZEK","ZDZISŁAW","BOGDAN","PATRYK","DAMIAN","WALDEMAR","ZYGMUNT","WIKTOR","PRZEMYSŁAW","SYLWESTER","KONRAD","EUGENIUSZ","ARKADIUSZ","KACPER","BOGUSŁAW","BARTŁOMIEJ","KRYSTIAN","ADRIAN","FILIP","WŁODZIMIERZ","WITOLD","BRONISŁAW","MAKSYMILIAN","SZCZEPAN","IRENEUSZ","BARTOSZ","WACŁAW","BOLESŁAW","LEON","ZENON","HUBERT","IGNACY","JULIAN","RADOSŁAW","LUDWIK","GABRIEL","BERNARD","CEZARY","FELIKS","NORBERT","EDMUND","LECH","LUCJAN","ALOJZY","WINCENTY","OSKAR","EMIL","BŁAŻEJ","BOGUMIŁ","WALENTY","SEWERYN","IGOR","MARIA","MIŁOSZ","TEODOR","ROMUALD","BENEDYKT","GERARD","JOACHIM","ERYK","ALFRED","ALBERT","AUGUSTYN","FLORIAN","MARCEL","JULIUSZ","OLIWIER","NIKODEM","KONSTANTY","LEONARD","REMIGIUSZ")

pr_nazwiska = ("NOWAK","WÓJCIK","KOWALCZYK","WOŹNIAK","MAZUR","KRAWCZYK","KACZMAREK","ZAJĄC","PAWŁOWSKI","KRÓL","WRÓBEL","WIECZOREK","DUDEK","STĘPIEŃ","PAWLAK","NOWICKI","SIKORA","WALCZAK","BARAN","MICHALAK","SZEWCZYK","PIETRZAK","JASIN","MARCINIAK","SADOWSKI","BĄK","DUDA","WILK","WŁODARCZYK","LIS","MAZUREK","KUBIAK","KOŁODZIEJ","KAŹMIERCZAK","KRUPA","MRÓZ")
