import matplotlib.pyplot as plt
import numpy as np


def wykres(pracownicy:list) -> None:
    '''
    funkcja wyswietlajaca histogram dla pensji pracownikow
    :param pracownicy: lista z danymi pracownikow
    :return: None
    '''
    x = []

    for i in pracownicy:
        x.append(i.pensja)

    print(x)
    x.append(1000)
    plt.figure()
    plt.hist(x,bins=25,color='green')
    plt.show()
