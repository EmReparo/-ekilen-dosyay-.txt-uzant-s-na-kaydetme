import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

#-------------------------------------------------------------------------------------------------------
#arayüzün tanıtılması ve boyutu ve isminin belirlenmesi.
root=Tk()
root.title("Yorum Çekme")
root.geometry("600x300")
def button_command(): # kullanıcıdan girdilerin alınır button ile birlikte fonksyon aktifleşir
    lnk = girdi.get()
    dosya=girdi2.get()
    r = requests.get(lnk)
    s = BeautifulSoup(r.content, "html.parser")
    s.prettify()

    detay = s.find_all("div", {"class": "bbWrapper"})
    for det in detay:
        yorum = det.text
        print(yorum)
        print("\n", "------------------------------------------------------------------", "\n")
        metin = str(yorum)
        with open(dosya+".txt", "a", encoding="utf-8") as f:
            f.write("\n" + "------------------------------------------------------------------" + "\n")
            f.write(metin)

    return messagebox.showinfo("showinfo", "Konudaki yorumlar txt dosyasına aktarıldı")
# Arayüzün widgetlarının yerleştirilmesi ve özelleştirilmesi
etiket = Label(root, text="Yorumlarını çekmek isteğin konu sayfasının linkini giriniz", font="ariel")
etiket.pack(padx=10, pady=10)
girdi = Entry(root, width=60)
girdi.pack()
etiket2 = Label(root, text="Oluşturulacak dosyaya isim veriniz..", font="ariel")
etiket2.pack(padx=10, pady=10)
girdi2 = Entry(root, width=60)
girdi2.pack()
b1 = Button(root, text="aktar", height=2, width=5, command=button_command)
b1.pack()
root = mainloop()
#-------------------------------------------------------------------------------------------------------
