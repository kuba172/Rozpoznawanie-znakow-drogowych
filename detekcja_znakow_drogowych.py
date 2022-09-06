import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

kolor_linii = 1
kolor_czcionki = 1
grubosc_linii=2
wielkosc_czcionki=1
bgr_linii=(0,255,255)
bgr_czcionki=(0,255,255)

def wyjdz():
    global okno
    pytanie = messagebox.askquestion("Pytanie","Czy na pewno chcesz wyjść z programu?")
    if(pytanie=="yes"):
        okno.destroy()

def ustawienia():
    ustawienia = tk.Toplevel(okno)
    ustawienia.title("Ustawienia")
    ustawienia.geometry("500x600")
    ustawienia.resizable(False,False)
    ustawienia.iconbitmap(r'ikona.ico')
    ustawienia.focus_set()
    ustawienia.grab_set()
    tk.Label(ustawienia, text="Ustawienia", font=("Arial", 25)).pack()
    tk.Label(ustawienia, text="Grubość lini:", font=("Arial", 16)).place(x=20,y=50)
    tk.Label(ustawienia, text="Wielkość czcionki:", font=("Arial", 16)).place(x=20,y=150)
    tk.Label(ustawienia, text="Kolor lini:", font=("Arial", 16)).place(x=20,y=250)
    tk.Label(ustawienia, text="Kolor czcionki:", font=("Arial", 16)).place(x=20,y=350)
    global rb_kolor_linii
    global kolor_linii
    rb_kolor_linii = IntVar()
    rb_kolor_linii.set(kolor_linii)
    rb_kolor_linii_zolty = Radiobutton(ustawienia, variable=rb_kolor_linii, value=1, text="Żółty",command=lambda: ustaw_kolor_linii(rb_kolor_linii.get()))
    rb_kolor_linii_czerwony = Radiobutton(ustawienia, variable=rb_kolor_linii, value=2, text="Czerwony",command=lambda: ustaw_kolor_linii(rb_kolor_linii.get()))
    rb_kolor_linii_niebieski = Radiobutton(ustawienia, variable=rb_kolor_linii, value=3, text="Niebieski",command=lambda: ustaw_kolor_linii(rb_kolor_linii.get()))
    rb_kolor_linii_zielony = Radiobutton(ustawienia, variable=rb_kolor_linii, value=4, text="Zielony",command=lambda: ustaw_kolor_linii(rb_kolor_linii.get()))
    rb_kolor_linii_czarny = Radiobutton(ustawienia, variable=rb_kolor_linii, value=5, text="Czarny",command=lambda: ustaw_kolor_linii(rb_kolor_linii.get()))
    rb_kolor_linii_szary = Radiobutton(ustawienia, variable=rb_kolor_linii, value=6, text="Szary",command=lambda: ustaw_kolor_linii(rb_kolor_linii.get()))
    rb_kolor_linii_bialy = Radiobutton(ustawienia, variable=rb_kolor_linii, value=7, text="Biały",command=lambda: ustaw_kolor_linii(rb_kolor_linii.get()))
    rb_kolor_linii_zolty.place(x=20,y=280)
    rb_kolor_linii_czerwony.place(x=120, y=280)
    rb_kolor_linii_niebieski.place(x=220, y=280)
    rb_kolor_linii_zielony.place(x=320, y=280)
    rb_kolor_linii_czarny.place(x=120, y=320)
    rb_kolor_linii_szary.place(x=220, y=320)
    rb_kolor_linii_bialy.place(x=20, y=320)

    def ustaw_kolor_linii(value):
        global kolor_linii
        global bgr_linii
        kolor_linii=value
        if(kolor_linii==1):
            bgr_linii=(0,255,255)
        elif(kolor_linii==2):
            bgr_linii=(0,0,255)
        elif (kolor_linii == 3):
            bgr_linii=(255,255,0)
        elif (kolor_linii == 4):
            bgr_linii=(0,255,0)
        elif (kolor_linii == 5):
            bgr_linii=(0,0,0)
        elif (kolor_linii == 6):
            bgr_linii=(128,128,128)
        elif (kolor_linii == 7):
            bgr_linii=(255,255,255)

    global rb_kolor_czcionki
    global kolor_czcionki
    rb_kolor_czcionki = IntVar()
    rb_kolor_czcionki.set(kolor_czcionki)
    rb_kolor_czcionki_zolty = Radiobutton(ustawienia, variable=rb_kolor_czcionki, value=1, text="Żółty",
                                       command=lambda: ustaw_kolor_czcionki(rb_kolor_czcionki.get()))
    rb_kolor_czcionki_czerwony = Radiobutton(ustawienia, variable=rb_kolor_czcionki, value=2, text="Czerwony",
                                          command=lambda: ustaw_kolor_czcionki(rb_kolor_czcionki.get()))
    rb_kolor_czcionki_niebieski = Radiobutton(ustawienia, variable=rb_kolor_czcionki, value=3, text="Niebieski",
                                           command=lambda: ustaw_kolor_czcionki(rb_kolor_czcionki.get()))
    rb_kolor_czcionki_zielony = Radiobutton(ustawienia, variable=rb_kolor_czcionki, value=4, text="Zielony",
                                         command=lambda: ustaw_kolor_czcionki(rb_kolor_czcionki.get()))
    rb_kolor_czcionki_czarny = Radiobutton(ustawienia, variable=rb_kolor_czcionki, value=5, text="Czarny",
                                        command=lambda: ustaw_kolor_czcionki(rb_kolor_czcionki.get()))
    rb_kolor_czcionki_szary = Radiobutton(ustawienia, variable=rb_kolor_czcionki, value=6, text="Szary",
                                       command=lambda: ustaw_kolor_czcionki(rb_kolor_czcionki.get()))
    rb_kolor_czcionki_bialy = Radiobutton(ustawienia, variable=rb_kolor_czcionki, value=7, text="Biały",
                                       command=lambda: ustaw_kolor_czcionki(rb_kolor_czcionki.get()))
    rb_kolor_czcionki_zolty.place(x=20, y=380)
    rb_kolor_czcionki_czerwony.place(x=120, y=380)
    rb_kolor_czcionki_niebieski.place(x=220, y=380)
    rb_kolor_czcionki_zielony.place(x=320, y=380)
    rb_kolor_czcionki_czarny.place(x=120, y=420)
    rb_kolor_czcionki_szary.place(x=220, y=420)
    rb_kolor_czcionki_bialy.place(x=20, y=420)

    def ustaw_kolor_czcionki(value):
        global kolor_czcionki
        global bgr_czcionki

        kolor_czcionki=value
        if(kolor_czcionki==1):
            bgr_czcionki=(0,255,255)
        elif(kolor_czcionki==2):
            bgr_czcionki=(0,0,255)
        elif (kolor_czcionki == 3):
            bgr_czcionki=(255,255,0)
        elif (kolor_czcionki == 4):
            bgr_czcionki=(0,255,0)
        elif (kolor_czcionki== 5):
            bgr_czcionki=(0,0,0)
        elif (kolor_czcionki == 6):
            bgr_czcionki=(128,128,128)
        elif (kolor_czcionki == 7):
            bgr_czcionki=(255,255,255)

    global rb_grubosc_linii
    global grubosc_linii
    rb_grubosc_linii = IntVar()
    rb_grubosc_linii.set(grubosc_linii)
    rb_grubosc_linii_1 = Radiobutton(ustawienia, variable=rb_grubosc_linii, value=1, text="1",
                                     command=lambda: ustaw_grubosc_linii(rb_grubosc_linii.get()))
    rb_grubosc_linii_2 = Radiobutton(ustawienia, variable=rb_grubosc_linii, value=2, text="2",
                                     command=lambda: ustaw_grubosc_linii(rb_grubosc_linii.get()))
    rb_grubosc_linii_3 = Radiobutton(ustawienia, variable=rb_grubosc_linii, value=3, text="3",
                                     command=lambda: ustaw_grubosc_linii(rb_grubosc_linii.get()))
    rb_grubosc_linii_4 = Radiobutton(ustawienia, variable=rb_grubosc_linii, value=4, text="4",
                                     command=lambda: ustaw_grubosc_linii(rb_grubosc_linii.get()))
    rb_grubosc_linii_6 = Radiobutton(ustawienia, variable=rb_grubosc_linii, value=6, text="6",
                                     command=lambda: ustaw_grubosc_linii(rb_grubosc_linii.get()))
    rb_grubosc_linii_8 = Radiobutton(ustawienia, variable=rb_grubosc_linii, value=8, text="8",
                                     command=lambda: ustaw_grubosc_linii(rb_grubosc_linii.get()))
    rb_grubosc_linii_12 = Radiobutton(ustawienia, variable=rb_grubosc_linii, value=12, text="12",
                                      command=lambda: ustaw_grubosc_linii(rb_grubosc_linii.get()))
    rb_grubosc_linii_16 = Radiobutton(ustawienia, variable=rb_grubosc_linii, value=16, text="16",
                                      command=lambda: ustaw_grubosc_linii(rb_grubosc_linii.get()))
    rb_grubosc_linii_1.place(x=20, y=80)
    rb_grubosc_linii_2.place(x=120, y=80)
    rb_grubosc_linii_3.place(x=220, y=80)
    rb_grubosc_linii_4.place(x=320, y=80)
    rb_grubosc_linii_6.place(x=20, y=120)
    rb_grubosc_linii_8.place(x=120, y=120)
    rb_grubosc_linii_12.place(x=220, y=120)
    rb_grubosc_linii_16.place(x=320, y=120)

    def ustaw_grubosc_linii(value):
        global grubosc_linii
        grubosc_linii = value

    global rb_wielkosc_czcionki
    global wielkosc_czcionki
    rb_wielkosc_czcionki = IntVar()
    rb_wielkosc_czcionki.set(wielkosc_czcionki)
    rb_wielkosc_czcionki_1 = Radiobutton(ustawienia, variable=rb_wielkosc_czcionki, value=1, text="1",
                                     command=lambda: ustaw_wielkosc_czcionki(rb_wielkosc_czcionki.get()))
    rb_wielkosc_czcionki_2 = Radiobutton(ustawienia, variable=rb_wielkosc_czcionki, value=2, text="2",
                                     command=lambda: ustaw_wielkosc_czcionki(rb_wielkosc_czcionki.get()))
    rb_wielkosc_czcionki_3 = Radiobutton(ustawienia, variable=rb_wielkosc_czcionki, value=3, text="3",
                                     command=lambda: ustaw_wielkosc_czcionki(rb_wielkosc_czcionki.get()))
    rb_wielkosc_czcionki_4 = Radiobutton(ustawienia, variable=rb_wielkosc_czcionki, value=4, text="4",
                                     command=lambda: ustaw_wielkosc_czcionki(rb_wielkosc_czcionki.get()))
    rb_wielkosc_czcionki_6 = Radiobutton(ustawienia, variable=rb_wielkosc_czcionki, value=6, text="6",
                                     command=lambda: ustaw_wielkosc_czcionki(rb_wielkosc_czcionki.get()))
    rb_wielkosc_czcionki_8 = Radiobutton(ustawienia, variable=rb_wielkosc_czcionki, value=8, text="8",
                                     command=lambda: ustaw_wielkosc_czcionki(rb_wielkosc_czcionki.get()))
    rb_wielkosc_czcionki_12 = Radiobutton(ustawienia, variable=rb_wielkosc_czcionki, value=12, text="12",
                                      command=lambda: ustaw_wielkosc_czcionki(rb_wielkosc_czcionki.get()))
    rb_wielkosc_czcionki_16 = Radiobutton(ustawienia, variable=rb_wielkosc_czcionki, value=16, text="16",
                                      command=lambda: ustaw_wielkosc_czcionki(rb_wielkosc_czcionki.get()))
    rb_wielkosc_czcionki_1.place(x=20, y=180)
    rb_wielkosc_czcionki_2.place(x=120, y=180)
    rb_wielkosc_czcionki_3.place(x=220, y=180)
    rb_wielkosc_czcionki_4.place(x=320, y=180)
    rb_wielkosc_czcionki_6.place(x=20, y=220)
    rb_wielkosc_czcionki_8.place(x=120, y=220)
    rb_wielkosc_czcionki_12.place(x=220, y=220)
    rb_wielkosc_czcionki_16.place(x=320, y=220)

    def ustaw_wielkosc_czcionki(value):
        global wielkosc_czcionki
        wielkosc_czcionki = value

    ok = tk.Button(ustawienia, text="Ok", font=("Arial", 12), height=2, width=20, command=lambda: ustawienia.destroy())
    ok.place(x=100,y=500)



def informacje():
    global zdjecie
    global zdj
    informacje = tk.Toplevel(okno)
    informacje.title("Informacje")
    informacje.geometry("1200x800")
    informacje.resizable(False,False)
    informacje.iconbitmap(r'ikona.ico')
    informacje.focus_set()
    informacje.grab_set()
    tk.Label(informacje, text="Informacje o programie:", font=("Arial", 25)).pack()
    tk.Label(informacje, text="Program służy do rozpoznawania i klasyfikowania 46 różnych znaków drogowych ze zdjęć.\n Autorem programu jest Jakub Rogalski.\n Wykrywane znaki:", font=("Arial", 16)).pack()
    zdjecie = Image.open(r'znaki.jpg')
    zdjecie.thumbnail((600,319))
    zdj = ImageTk.PhotoImage(zdjecie)
    label = Label(informacje, image=zdj)
    label.place(x=20,y=120)
    f = open(r"opisy_znakow.txt","r",encoding="utf-8")
    informacje_znaki = Label(informacje, text=f.read(),font=("Arial", 8))
    informacje_znaki.place(x=660,y=120)

    ok = tk.Button(informacje, text="Ok", font=("Arial", 12), height=2, width=20, command=lambda: informacje.destroy())
    ok.place(x=390, y=500)

def zaladuj_zdjecie():
     try:
        wypisane_znaki = tk.Frame(okno, width=500, height=550).place(x=1010, y=100)
        global zdj
        global zdjecie
        maksymalny_rozmiar=(960,540)
        tk.Frame(okno, width=970, height=550).place(x=30, y=120)
        global sciezka_do_zdjecia
        sciezka_do_zdjecia = filedialog.askopenfilename()
        zdjecie = Image.open(sciezka_do_zdjecia)
        zdjecie.thumbnail(maksymalny_rozmiar)
        zdj = ImageTk.PhotoImage(zdjecie)
        label = Label(okno, image=zdj)
        label.place(x=30,y=120)
        tk.Label(okno, text="Ścieżka do pliku: " + sciezka_do_zdjecia, font=("Arial", 11)).place(x=30, y=680)
        return sciezka_do_zdjecia
     except:
        tk.Frame(okno, width=970,height=550).place(x=30, y=120)
        tk.Label(okno,text="Nie można załadować zdjęcia " ,font=("Arial",16)).place(x=400,y=400)
        tk.Frame(okno,width=1200,height=30).place(x=30, y=680)

def wykryj_znaki(sciezka_do_zdjecia):
    try:
        wypisywanie_znakow = []
        wypisywanie_opisow = []
        wagi = "yolov3_znaki_drogowe.weights"
        konfiguracja = "yolov3_znaki_drogowe.cfg"

        siec = cv2.dnn.readNet(wagi, konfiguracja)
        siec.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

        f1 = open(r"classes.txt", "r", encoding="utf-8")
        i = 0
        znaki_drogowe = []
        while i <= 46:
            znaki_drogowe.append(f1.readline().replace("\n",""))
            i+=1

        f2 = open(r"opisy.txt", "r", encoding="utf-8")
        i = 0
        opisy_znakow = []
        while i <= 46:
            opisy_znakow.append(f2.readline().replace("\n",""))
            i += 1


        nazwy_warstw = siec.getLayerNames()
        warstwy_wyjsciowe = [nazwy_warstw[i[0] - 1] for i in siec.getUnconnectedOutLayers()]

        f = open(sciezka_do_zdjecia, "rb")
        sciezka = f.read()
        sciezka_arr = np.frombuffer(sciezka, dtype=np.uint8)
        img = cv2.imdecode(sciezka_arr, cv2.IMREAD_COLOR)
        #img = cv2.imread(sciezka_do_zdjecia)
        img = cv2.resize(img, None, fx=1, fy=1,interpolation=cv2.INTER_NEAREST)#TU JEST BLAD
        wysokosc, szerokosc, kanaly_kolorow = img.shape

        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)


        siec.setInput(blob)
        wyjscia = siec.forward(warstwy_wyjsciowe)

        znaki_drogowe_ids = []
        poziom_ufnosci = []
        pudelka = []
        for w in wyjscia:
            for detekcja_znaku in w:
                wyniki = detekcja_znaku[5:]  # szukamy wartosci o najwiekszym prawdopodobienstwie pomijajac pierwsze 5 wartosci w tablicy
                znaki_drogowe_id = np.argmax(wyniki)  # argmax zwraca indeks maksymalnej wartości w tablicy.
                prog = wyniki[znaki_drogowe_id]
                if prog > 0.5:
                    # Wykrycie obiektu

                    srodek_x = int(detekcja_znaku[0] * szerokosc)
                    srodek_y = int(detekcja_znaku[1] * wysokosc)
                    sz = int(detekcja_znaku[2] * szerokosc)
                    wys = int(detekcja_znaku[3] * wysokosc)

                    # Koordynaty prostokata
                    x = int(srodek_x - sz / 2)
                    y = int(srodek_y - wys / 2)

                    pudelka.append([x, y, sz, wys])
                    poziom_ufnosci.append(float(prog))
                    znaki_drogowe_ids.append(znaki_drogowe_id)

        indeksy = cv2.dnn.NMSBoxes(pudelka, poziom_ufnosci, 0.5, 0.4)

        # print(indeksy)
        font = cv2.FONT_HERSHEY_DUPLEX
        for i in range(len(pudelka)):
            if i in indeksy:
                x, y, w, wys = pudelka[i]
                etykieta = str(znaki_drogowe[znaki_drogowe_ids[i]])
                opis = str(opisy_znakow[znaki_drogowe_ids[i]])
                cv2.rectangle(img, (x, y), (x + sz, y + wys), bgr_linii, grubosc_linii)
                cv2.putText(img, etykieta, (x, y + 50), font, wielkosc_czcionki, bgr_czcionki, wielkosc_czcionki*2)
                wypisywanie_znakow.append(etykieta)
                wypisywanie_opisow.append(opis)

        cv2.imwrite(r'wynik/wynik.jpg', img)

        try:
            global zdj
            global zdjecie
            maksymalny_rozmiar = (960, 540)
            tk.Frame(okno, width=970, height=550).place(x=30, y=120)
            sciezka_do_zdjecia = r'wynik/wynik.jpg'
            zdjecie = Image.open(sciezka_do_zdjecia)
            zdjecie.thumbnail(maksymalny_rozmiar)
            zdj = ImageTk.PhotoImage(zdjecie)
            label = Label(okno, image=zdj)
            label.place(x=30, y=120)
        except:
            tk.Frame(okno, width=970, height=550).place(x=30, y=120)
            tk.Label(okno, text="Nie można wykryć znaków ", font=("Arial", 16)).place(x=400, y=400)
            tk.Frame(okno, width=1200, height=30).place(x=30, y=680)
    except:
        tk.Frame(okno, width=970, height=550).place(x=30, y=120)
        tk.Label(okno, text="Nie można wykryć znaków ", font=("Arial", 16)).place(x=400, y=400)
        tk.Frame(okno, width=1200, height=30).place(x=30, y=680)

    x = 0
    if(len(wypisywanie_znakow)==0):
        wypisane_znaki = tk.Label(okno, text="Nie wykryto żadnego znaku drogowego ", font=("Arial", 11)).place(x=1010,y=100)
    else:
        for i in range(len(wypisywanie_znakow)):
            #print(i)
            wypisane_znaki = tk.Label(okno, text=wypisywanie_znakow[i] + "  " + wypisywanie_opisow[i], font=("Arial", 11)).place(x=1010,y=100 +  30 * x)
            x += 1
        liczba_znakow = tk.Label(okno, text="Liczba wykrytych znaków drogowych: " + str(len(wypisywanie_znakow)), font=("Arial", 11)).place(x=1010, y=100 + 30 * (x + 1))

okno = Tk()
okno.resizable(False,False)
okno.title("Detekcja znaków drogowych")
okno.geometry("1600x800")
okno.iconbitmap(r'ikona.ico')
tk.Label(okno,text="Detekcja znaków drogowych", font=("Arial",25)).pack()
tk.Label(okno,text="Załadowane zdjęcie: ",font=("Arial",16)).place(x=30,y=50)
tk.Label(okno,text="Wykryte znaki drogowe: " ,font=("Arial",16)).place(x=1010,y=50)
tk.Label(okno,text="Nie wczytano żadnego zdjęcia " ,font=("Arial",11)).place(x=400,y=400)
wczytaj_plik_przycisk = tk.Button(okno, text = "Wczytaj plik",font=("Arial",12),height=2,width=20, command= lambda: zaladuj_zdjecie())
wczytaj_plik_przycisk.place(x=20, y=740)
wyjscie_przycisk = tk.Button(okno, text = "Wyjście",font=("Arial",12),height=2,width=20, command=wyjdz)
wyjscie_przycisk.place(x=1010, y=740)
wykryj_znaki_przycisk = tk.Button(okno, text = "Wykryj znaki",font=("Arial",12),height=2,width=20, command= lambda: wykryj_znaki(sciezka_do_zdjecia))
wykryj_znaki_przycisk.place(x=230, y=740)
opcje_przycisk = tk.Button(okno, text = "Ustawienia",font=("Arial",12),height=2,width=20, command= lambda: ustawienia())
opcje_przycisk.place(x=650, y=740)
informacje_przycisk = tk.Button(okno, text = "Informacje o programie",font=("Arial",12),height=2,width=20, command= lambda: informacje())
informacje_przycisk.place(x=440, y=740)

okno.mainloop()

