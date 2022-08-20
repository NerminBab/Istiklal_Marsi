"""
İstiklal Marşımızın kelimeleri incelenmiştir.
"""

class Mars():
    def __init__(self):
        with open("Istiklal_Marsimiz.txt","r",encoding="utf-8") as file:
            mars_icerigi=file.read()
            kelimeler=mars_icerigi.split()
            self.sade_kelimeler=list()
            for k in kelimeler:
                k = k.strip("\n")
                k = k.strip(" ")
                k = k.strip(".")
                k = k.strip(",")
                k = k.strip(":")
                k = k.strip("!")
                k = k.strip("?")
                k = k.strip(";")
                self.sade_kelimeler.append(k)

    def tum_kelimeler(self):
        kelimeler_havuzu=set()
        for k in self.sade_kelimeler:
            kelimeler_havuzu.add(k)
        for k in kelimeler_havuzu:
            print(k)


    def kelime_frekansi(self):
        kelimeler_sozluk=dict()
        for k in self.sade_kelimeler:
            if (k in kelimeler_sozluk):
                kelimeler_sozluk[k]+=1
            else:
                kelimeler_sozluk[k]=1
        for kelime,sayi in kelimeler_sozluk.items():
            print("'{}' kelimesi; {} defa geçiyor.".format(kelime,sayi))


marsimiz=Mars()
marsimiz.tum_kelimeler()
# marsimiz.kelime_frekansi()

