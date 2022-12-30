

from datetime import datetime
#Write class and imports here!

class tuote:
    def __init__(self, nimi, hinta, hylly, koodi):
        self.nimi = nimi
        self.hinta = float(hinta)
        self.hylly = hylly
        self.koodi = koodi

    
    @property
    def nimi(self):
        return self._nimi
    @nimi.setter
    def nimi(self, value):
        self._nimi = value

    @property
    def hinta(self):
        return self._hinta
    @hinta.setter
    def hinta(self, value):
        if value < 0.0:
            value = 0.0
        self._hinta = value

    @property
    def hylly(self):
        return self._hylly
    @hylly.setter
    def hylly(self, value):
        self._hylly = value

    @property
    def koodi(self):
        return self._koodi
    @koodi.setter
    def koodi(self, value):
        self._koodi = value


    def __str__(self):
        
        print("Nimi:\t\t", self.nimi)
        print("Hinta:\t\t", self.hinta)
        print("Hylly:\t\t", self.hylly)
        print("Koodi:\t\t", self.koodi)

               

class vaate(tuote):
    def __init__(self, nimi, hinta, hylly, koodi, koko, materiaali):
        super().__init__(nimi, hinta, hylly, koodi)
        self.koko = koko
        self.materiaali = materiaali

    def __str__(self):
        super().__str__()
        #return "Koko:\t\t" + str(self.koko) + "\n" + "Materiaali:\t" + str(self.materiaali)
        print("Koko:\t\t", self.koko)
        print("Maateriaali:\t", self.materiaali)
        return ""


class ruoka(tuote):
    def __init__(self, nimi, hinta, hylly, koodi, alkuperamaa, paivays):
        super().__init__(nimi, hinta, hylly, koodi)
        self.alkuperamaa = alkuperamaa
        self.paivays = paivays

        #@property
        #def paivays(self):
        #    return self._paivays
        #@paivays.setter
        #def paivays(self, value):
        #    if value < datetime.now():
        #        value = datetime.now()
        #    self._paivays = value

    def __str__(self):
        super().__str__()
        print("Alkuperä:\t", self.alkuperamaa)
        print("Päiväys:\t", self.paivays)
        return ""



class kodinkone(tuote):
    def __init__(self, nimi, hinta, hylly, koodi, takuu, paino):
        super().__init__(nimi, hinta, hylly, koodi)
        self.takuu = takuu
        self.paino = paino
    
    def __str__(self):
        super().__str__()
        print("Takuu:\t\t", self.takuu)
        print("Paino:\t\t", self.paino)
        return ""               

if __name__ == "__main__":
    lista = []
    
    while True:

        print()
        valinta = input("Mikä tuote lisätään listaan (1 = ruoka, 2 = vaate, 3 = kodinkone, muu = lopetus: ")
        if not(valinta == "1" or valinta == "2" or valinta == "3"):
            print()
            break
        tavara = input("Anna tuotteen nimi: ")
        hinta = float(input("Anna hinta: "))
        hyllypaikka = input("Anna hyllypaikka: ")
        koodi = input("Anna koodi: ")

        if valinta == "1":

            alkuperamaa = input("Ruuan alkuperämaa: ")
            paivays = input("Päiväys: ")
            lista.append(ruoka(tavara, hinta, hyllypaikka, koodi, alkuperamaa, paivays))

        elif valinta == "2":

            koko = input("Vaatteen koko: ")
            materiaali = input("Vaatteen materiaali: ")
            lista.append(vaate(tavara, hinta, hyllypaikka, koodi, koko, materiaali))

        elif valinta == "3":

            takuu = input("Kodinkoneen takuu: ")
            paino = input("Kodinkoneen paino: ")
            lista.append(kodinkone(tavara, hinta, hyllypaikka, koodi, takuu, paino))


        
    for i in lista:
        print(i)

    