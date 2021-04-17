
def vigenere_sifreleme():
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    sifrelenecek_metin = ""
    sifreleme_anahtari = ""
    sifrelenmis_metin = ""

    sifreleme_anahtari = input("Sifrelemek icin anahtar giriniz: ")
    sifreleme_anahtari = sifreleme_anahtari.lower()

    sifrelenecek_metin = input("Sifrelenecek metini giriniz: ")
    sifrelenecek_metin = sifrelenecek_metin.lower()

    metin_uzunlugu = len(sifrelenecek_metin)

    genisletilmis_anahtar = sifreleme_anahtari
    genisletilmis_anahtar_uzunlugu = len(genisletilmis_anahtar)

    while genisletilmis_anahtar_uzunlugu < metin_uzunlugu:
        genisletilmis_anahtar = genisletilmis_anahtar + sifreleme_anahtari
        genisletilmis_anahtar_uzunlugu = len(genisletilmis_anahtar)


    anahtar_pozisyonu = 0

    for harf in sifrelenecek_metin:
        if harf in alfabe:
            pozisyon = alfabe.find(harf)
            anahtar_karakteri = genisletilmis_anahtar[anahtar_pozisyonu]
            anahtar_karakteri_pozisyonu = alfabe.find(anahtar_karakteri)
            anahtar_pozisyonu = anahtar_pozisyonu + 1
            yeni_pozisyon = pozisyon + anahtar_karakteri_pozisyonu
            if yeni_pozisyon > 26:
                yeni_pozisyon = yeni_pozisyon - 26
            yeni_karakter = alfabe[yeni_pozisyon]
            sifrelenmis_metin = sifrelenmis_metin + yeni_karakter
        else:
            sifrelenmis_metin = sifrelenmis_metin + harf
    return (sifrelenmis_metin)


def vigenere_desifreleme():
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    sifrelenecek_metin = ""
    desifre_anahtari = ""
    desifre_metin = ""


    desifre_anahtari = input("Lutfen sifreleme anahtarini giriniz: ")
    desifre_anahtari = desifre_anahtari.lower()
    sifrelenecek_metin = input("Sifreli metini giriniz: ")
    sifrelenecek_metin = sifrelenecek_metin.lower()


    metin_uzunlugu = len(sifrelenecek_metin)
    genisletilmis_anahtar = desifre_anahtari
    genisletilmis_anahtar_uzunlugu = len(genisletilmis_anahtar)


    while genisletilmis_anahtar_uzunlugu < metin_uzunlugu:
        genisletilmis_anahtar = genisletilmis_anahtar + desifre_anahtari
        genisletilmis_anahtar_uzunlugu = len(genisletilmis_anahtar)


    anahtar_pozisyonu = 0

    for harf in sifrelenecek_metin:
        if harf in alfabe:
            pozisyon = alfabe.find(harf)
            anahtar_karakteri = genisletilmis_anahtar[anahtar_pozisyonu]
            anahtar_karakteri_pozisyonu = alfabe.find(anahtar_karakteri)
            anahtar_pozisyonu = anahtar_pozisyonu + 1
            yeni_pozisyon = pozisyon - anahtar_karakteri_pozisyonu
            if yeni_pozisyon > 26:
                yeni_pozisyon = yeni_pozisyon + 26
            yeni_karakter = alfabe[yeni_pozisyon]
            desifre_metin = desifre_metin + yeni_karakter
        else:
            desifre_metin = desifre_metin + harf
    return (desifre_metin)


print(vigenere_sifreleme())
print(vigenere_desifreleme())
