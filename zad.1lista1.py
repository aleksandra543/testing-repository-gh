# Stworz klase Vector przechowującą kolekcję liczb. Zaimplementuj
# • konstruktor przyjmujący rozmiar wektora jako argument (domyślnie 3),
# • metodę do losowej generacji elementów wektora
# • metodę do wczytywania elementów wektora z listy podanej jako argument,
# • operator dodawania i odejmowania dwóch wektorów (powinien rzucać wyjątek ValueError w sytuacji, kiedy wektory mają różne rozmiary),
# • mnożenie wektora przez skalar,
# • metodę wyliczającą długość wektora, 
# • metodę wyliczającą sumę elementów wektora,
# • metodę wyliczającą iloczyn skalarny dwóch wektorów,
# • reprezentację tekstową wektora,
# • operator [] pozwalający na dostęp do konkretnych elementów wektora,
# • operator in sprawdzający przynależność elementu do wektora. Kod powinien być 
# napisany w formie modułu, z częścią wykonywalną testującą klasę. Proszę zwrócić 
# szczególną uwagę na udokumentowanie modułu i metod

#?? po co to na pomaranczowo """, co mi to daje?

import random                                           #biblioteka do generowania losowych liczb

class Vector:                                           #klasa przechowuje funkcje zwane metodami
    def __init__(self, rozmiar=3):                      #definiuje konstruktor; init - inicjacja nowego obiektu w klasie (dzieki temu bede mogla tworzyc kolejne obiekty np. metody???)
        """                                 
        Konstruktor klasy Vector, ktory inicjalizuje obiekt Vector z okreslonym rozmiarem.

        Parametry:
        rozmiar (int): Rozmiar wektora (domyslnie 3).
        """
        self.rozmiar = rozmiar                          #zmiennej rozmiar przypisujemy nowy rozmiar rowny 3 elementom (domyslnie sa tam zera)
        self.dane = [0] * rozmiar                       #te 3 miejsca w wektorze - zmienna rozmiar - staje sie tablica o 3 pustych miejscach

    def generowanie_losowych_elementow(self):            #self musi byc, mimo, ze go nie uzyje
        """
        Metoda, ktora generuje losowe elementy wektora.
        """
        for i in range(self.rozmiar):                    #za pomoca petli ide po kazdym argumencie tablicy (wektora), w kazde miejsce losuje mi sie jakas liczba
            self.dane[i] = random.randint(1,100)  #???????? tylko czemu zmiennej dane przypisuje wylosowana liczbe calk. od 1 do 100; tu chodzi o to, ze kazdemu elementowi tablicy to przypisuje?
                                                    #???chodzi o to ze w kazdej funkcji tworze cos nowego (to co mam w poleceniu) i nazywam to po prostu "dane"

    def wczytywanie_elementow_wektora_z_listy(self, input_list):  #???input_list to jest zmienna przechowujaca liste podana przez uzytkownika w testowaniu pozniej; funkcja len sprawdza jej dlugosc; czy moge zmienic nazwe input_list na inna polska, bo wszystkie mam polskie?
        """
        Metoda, ktora wczytuje elementy wektora z listy podanej jako argument.

        Parametry:
        input_list (list): Lista elementow do wczytania do wektora.
        """
        if len(input_list) != self.rozmiar:                 #jesli dlugosc mojej listy nie zgodzi sie z rozmiarem wektora, wyskakuje blad (funkcja len zwraca dlugosc obiektu)
            raise ValueError("Podana lista ma inna dlugosc niz rozmiar wektora")
        self.dane = input_list       #??? po co to??? jesli wszystko sie zgodzi, to moje nowe dane to ta lista wpisana przez uzytkownika?

    def __add__(self, inny):                                #dodawanie 2 wektorow; inny to nazwa drugiego wektora
        if self.rozmiar != inny.rozmiar:                    #jesli rozmiar (ilosc argumentow w nim) wektora bedzie inny od podanego (rozny od 3), wyskakuje blad
            raise ValueError("Wektory maja rozne rozmiary") 
        result = Vector(self.rozmiar)     #?????????????????????? czyli jesli rozmiar jest dobry, to jest ta lista przypisywana zmiennej result, czy co to jest za postać?
        for i in range(self.rozmiar):                       #petla idzie po kazdym elemencie wektora
            result.dane[i] = self.dane[i] + inny.dane[i]    #dodaje odpowiadajace elementy z jednego wektora do drugiego
        return result

    def __sub__(self, inny):                            #odejmowanie 2 wektorow
        if self.rozmiar != inny.rozmiar:
            raise ValueError("Wektory maja rozne rozmiary")
        result = Vector(self.rozmiar)
        for i in range(self.rozmiar):                    #odejmowanie odpowiadajacych sobie elementow obu wektorow
            result.dane[i] = self.dane[i] - inny.dane[i]
        return result

    def __mul__(self, skalar):                          #mnozenie przez skalar
        result = Vector(self.rozmiar)   #??? jeszcze raz, czym jest result, jak to wytlumaczyc?
        for i in range(self.rozmiar):                   #petla ide po kazdym wyrazie (elemencie tablicy) i mnoze przez wybrana liczbe
            result.dane[i] = self.dane[i] * skalar
        return result

    def wyliczanie_dlugosci_wektora(self):
        """
        Metoda, ktora wylicza dlugosc wektora.
        """
        result = []                              #????tworze pusta tablice
        for elem in self.dane:                          #patla, ktora idzie po kazdym elemencie podanej przez uzytkownika tablicy 
            result.append(elem**2)                      #dodanie do tablicy kwadratu elementu tablicy
        return sum(result)**0.5                         #obliczanie ostatecznej dlugosci tablicy ze wzoru - najpierw sumuje kwadraty, potem pierwiastek

    def wyliczanie_sumy_elementow_wektora(self):        
        """
        Metoda, ktora wylicza sume elementow wektora.
        """
        return sum(self.dane)                           #sumuje wszystkie elementy wektora (tablicy) - funkcja sum(), wewnatrz zmienna dane - podane przez uzytkownika

    def iloczyn_skalarny(self, inny):
        """
        Metoda, ktora wylicza iloczyn skalarny dwoch wektorow.

        Parametry:
        inny (Vector): Drugi wektor do obliczenia iloczynu skalarnego.
        """
        if self.rozmiar != inny.rozmiar:                            #najpierw sprawdzam, czy rozmiar jest taki sam
            raise ValueError("Wektory maja rozne rozmiary")
        result = Vector(self.rozmiar)
        for i in range(self.rozmiar):
            result.dane[i] = self.dane[i] * inny.dane[i]            #Mnozenie odpowiadajacych sobie elementow wektorow
        return sum(result)                                          #obliczanie iloczynu skalarnego 2 wektorow - sumuje wszystkie wyniki

    def __str__(self):
        return f"Vector: {self.dane}"                   #przesloniecie metody magicznej __str__ dla reprezentacji obiektu Vector jako string

    def __getitem__(self, index):
        return self.dane[index]                         #przesloniecie metody magicznej __getitem__ dla dostepu do elementow wektora po indeksie, nadpisuje nawiasy [], po wpisaniu okreslonego indeksu do nich, mozemy sie dostac do danego elementu z tablicy (z danej zmiennej)

    def __contains__(self, item):
        return item in self.dane                        #przesloniecie metody magicznej __contains__ dla sprawdzenia czy element znajduje sie w wektorze


def testing():                                          #nie nalezy tu do klasy Vector, jest zewnetrznie
    #1 sprawdzenie domyslnego rozmiaru wektora
    v1 = Vector()                      #??????czemu w tym testowaniu nie podaje rozmiaru wektora, a w nastepnych juz mam jakies dane
    assert v1.rozmiar == 3                              #za pomoca assert sprawdzam, czy cos jest rowne czemus; tutaj sprawdzam, czy rozmiar podanego wektora v1 jest rowny 3

    #2 testowanie metody generujacej losowe elementy wektora
    v1.generowanie_losowych_elementow() #?????? zmienna.funkcja? czyli sprawdzam dzialanie funkcji napisanej wczesniej na tej zmiennej?
    for element in v1.dane:
        assert element >= 1 and element <= 100          #sprawdzam przynaleznosc podanego elementu (kazdego z wektora) do przedzialu

    #3 testowanie wczytywania elementow wektora z listy
    lista = [1,2,3,4,5]                                 #podaje konkretny rozmiar listy
    v1 = Vector(len(lista))        #???????????czemu taka postac, co ona oznacza
    v1.wczytywanie_elementow_wektora_z_listy(lista)
    assert lista == v1.dane                             #sprawdzenie, czy wczytane dane sa jednakowe

    #4 testowanie dodawania i odejmowania wektorow
    lista1 = [1,2,3]
    lista2 = [2,3,4]
    v1 = Vector(len(lista1))
    v2 = Vector(len(lista2))
    v1.wczytywanie_elementow_wektora_z_listy(lista1)
    v2.wczytywanie_elementow_wektora_z_listy(lista2)
    v3 = v1 + v2                                                       #suma wektorow v1 i v2 to nowy wektor v3
    v4 = v1 - v2
    assert v3.dane == [v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2]]        #sprawdzenie wyniku dodawania; dane wektora v3 musza byc rowne nowopowstalej liscie (wektorowi)
    assert v4.dane == [v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2]]        #sprawdzenie wyniku odejmowania

    #testowanie rzucania wyjatku
    lista1 = [1,3]
    lista2 = [1,2]
    v1 = Vector(len(lista1))
    v2 = Vector(len(lista2))
    v1.wczytywanie_elementow_wektora_z_listy(lista1)
    v2.wczytywanie_elementow_wektora_z_listy(lista2)
    try:                                                          #probuje dodac do siebie 2 wektory
        v1 + v2                                                   #nie da sie, bo sa rozne rozmiary
    except ValueError as e:                                       #zapisuje blad jako e
        assert str(e) == "Wektory mają rozne rozmiary"            #sprawdzenie, czy zwracany jest odpowiedni komunikat błędu (czy string jest taki sam)

#??????    #5testowanie mnożenia wektora przez skalar ----- skalar to liczba R, nie chodzi tu chyba o iloczyn wektorowy, to dopiero pozniej
    lista1 = [1,2]
    lista2 = [1,2]
    v1 = Vector(len(lista1))
    v2 = Vector(len(lista2))
    v1.wczytywanie_elementow_wektora_z_listy(lista1)
    v2.wczytywanie_elementow_wektora_z_listy(lista2)
    assert v1.iloczyn_skalarny(v2) == 5

    #6 testowanie metody liczącej długość wektora
    lista1 = [4,3]
    v1 = Vector(len(lista1))                                #??? jeszcze raz, czemu taki zapis? nie potrafie go wytlumaczyc
    v1.wczytywanie_elementow_wektora_z_listy(lista1)        #????tu jakby przypisuje funkcje dla zmiennej v1, by wykorzystac ja na tej zmiennej? - to taki rodzaj zapisu? (improwizuje, bo nie wiem juz sama)
    assert v1.wyliczanie_dlugosci_wektora() == 5.0

    #7 testowanie metody wyliczającej sumę elementów wektora
    lista1 = [4,3]
    v1 = Vector(len(lista1))
    v1.wczytywanie_elementow_wektora_z_listy(lista1)
    assert v1.wyliczanie_sumy_elementow_wektora() == 7

    #8 testowanie str
    lista1 = [4,3]
    v1 = Vector(len(lista1))
    v1.wczytywanie_elementow_wektora_z_listy(lista1)
    assert v1.__str__() == "Vector: [4, 3]"                 #tutaj sprawdzam, czy zwrocone zostana wpisane dane, a nie te "znaczki"

    #9 testowanie operatora []
    lista1 = [4,3]
    v1 = Vector(len(lista1))
    v1.wczytywanie_elementow_wektora_z_listy(lista1)
    for i in range(len(lista1)):                        #tutaj sprawdzam, , czy moge uzyc [], czyli np. zamiast pisac v1.dane[0] moge pisac v1[0] by dostac sie do 1. argumentu
        assert v1[i] == lista1[i]

    #10 testowanie operatora in
    lista1 = [4,3]
    v1 = Vector(len(lista1))
    v1.wczytywanie_elementow_wektora_z_listy(lista1)
    assert 3 in lista1                                  #sprawdzenie, czy operator poprawnie znajduje liczbę w tablicy; czyli tutaj czy 3 znajduje sie w liscie
    

if __name__ == "__main__":
    testing()                   #testowanie funkcjonalnosci klasy Vector; wywolywanie funkcji testing, ktora mam u gory
   