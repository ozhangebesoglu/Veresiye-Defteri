import sqlite3
import time

db = sqlite3.connect('veresiye.db')

yetki = db.cursor()

yetki.execute('CREATE TABLE IF NOT EXISTS veresiye(Isim,Borc)')

print('**** VERESIYE DEFTERINE HOSGELDINIZ PROGRAM ACILIYOR , LUTFEN BEKLEYINIZ ****')

time.sleep(2)

while True:
    print('---------MENU---------')
    print('1. Borclu Ekle\n2. Borclular Listele\n3. Borclu Sil\n4. Programdan Cikis\n')
    secim = input('Seciminizi giriniz: ')

    if secim == '1':
        isim = input('Borclu kisinin ismini giriniz: ')
        borc = float(input('Borclu miktarini giriniz: '))
        yetki.execute(f"INSERT INTO veresiye VALUES('{isim}', {borc})")
        db.commit()
        print(f'{isim} isimli kisi veresiye defterine kaydedildi.')
        print('*' * 30)
        time.sleep(1)
        input("Isleme devam etmek icin enter'a basiniz")
    
    elif secim == '2':
        yetki.execute("SELECT *FROM veresiye")
        yazdir = yetki.fetchall()
        say = 1
        for i in yazdir:
            print('*** VERESIYE DEFTERI ***')
            print(f"\n{say}: Borclu Adi: {i[0]}\nBorcun Miktari: {i[1]}\n")
            print('*' * 30)
            say += 1
        input("Isleme devam etmek icin enter'a basiniz")
    
    elif secim == '3':
        isim = input('Borclu ismini giriniz: ')
        yetki.execute(f"DELETE FROM veresiye WHERE Isim='{isim}'")
        db.commit()
        print(f'{isim} isimli kisi veresiye defterinden silindi.')
        print('*' * 30)
        time.sleep(1)
        input("Isleme devam etmek icin enter'a basiniz")
    
    elif secim == '4':
        print('Programdan cikis yapiliyor...')
        db.close()
        time.sleep(2)
        exit()

    else:
        print('Yanlis secim yaptiniz. Lutfen tekrar deneyiniz.')
        print('*' * 30)
        time.sleep(1)
    
    