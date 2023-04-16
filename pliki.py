import xml.etree.ElementTree as ET


def wczytaj(self:list, nazwa:str) -> bool:
    '''
    funkcja wczytujaca dane z pliku xml o podanej nazwie i zwracajaca, czy wczytanie sie powiodlo
    :param self:
    :param nazwa: nazwa pliku
    :return: bool
    '''
    try:
        drzewo = ET.parse(nazwa)
        root = drzewo.getroot()
        for e in root:
            self.dodaj(e.attrib['imie'], e.attrib['nazwisko'], int(e.attrib['pensja']))
        return True
    except:
        return False

def zapis(self, nazwa:str) -> bool:
    '''
    funkcja zapisujaca dane do pliku xml zwracajaca informacje czy operacja sie powiodla
    :param self:
    :param nazwa: nazwa pliku
    :return: bool
    '''
    try:
        root = ET.Element('root')
        for i in self.pracownicy:
            _pracownik = ET.SubElement(root, 'pracownik')
            _pracownik.set('id', str(i.id))
            _pracownik.set('imie', i.imie)
            _pracownik.set('nazwisko', i.nazwisko)
            _pracownik.set('pensja', str(i.pensja))

        data = ET.tostring(root).decode('utf-8')
        if not nazwa.endswith('.xml'):
            nazwa += '.xml'
        f = open(nazwa, 'w')
        f.write(data)
        f.close()
        return True
    except:
        return False