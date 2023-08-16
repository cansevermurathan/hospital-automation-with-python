#murathan cansever


liste=[ ]
karantina=[ ]
vefat_edenler=[ ()]
iyilesenler=[ ()]
yatak_sayisi=150  #karantina için ayırılmış yatak sayısı
n_yatak_sayisi=1000 #normalde hastanenin kapasitesi (normal hastalar için)
isim=""
soyisim=""
kimlik_no=0
teshis=""
y_yatak_sayisi=0
def yeni_kayit():
    t=0
    secim=0
    dosya=open("kaytlilar.txt","r")
    sonuc = dosya.readlines()
    dosya.close()
    dosya=open("kaytlilar.txt","a")
    print("PROGRAMIN İSTEDİĞİMİZ GİBİ ÇALIŞMASI İÇİN HASTA CPVID-19 HASTASI İSE TEŞHİSE COVID-19 YAZIN")
    while t==0:
        if n_yatak_sayisi > (len(sonuc)/4):
            isim = input("Kayıt olacak kişinin ismini giriniz")
            soyisim = input("Kayıt olacak kişinin soyismini giriniz")
            kimlik_no = int(input("Kayıt olacak kişinin kimlik numarasını giriniz"))
            teshis = input("Kayıt olacak hastaya konulan teshis nedir giriniz")
            if (str(kimlik_no)+"\n") in sonuc:
                print("Kayıt daha önceden yapılmıştır\n"
                      "Tekrar kayıt giriniz")
                continue


            if (str(kimlik_no) + "\n") not in sonuc:
                liste.append({"ad": isim, "soyad": soyisim, "kimlik_no": kimlik_no,"teshis": teshis})  # listeyi sadece hastanın COVID-19 teşhisi konulduğu zaman kullanıyoruz
                dosya.write("AD:\tSOYAD:\tTESHIS\n")
                dosya.write(isim + "\t")
                dosya.write(soyisim + "\t")
                dosya.write(teshis + "\n")  # TEK TEK YAZMAK DAHA DÜZENLİ OLACAĞINI DÜŞÜNDÜM
                dosya.write("KIMLIK NUMARASI:\n")
                dosya.write(str(kimlik_no) + "\n")
                secim = int(input(
                    "Yeni bir kayıt daha açmak istiyorsanız 1'e \n kayıt işlemini bitirmek istiyorsanız 2'ye basınız"))
                if secim == 2:
                    break
                if secim==1:
                    continue





    dosya.close()
#---------------------------------------------------------------------------------------------
#hastanın teşhisi koronaya ise hasta karantina altına alınır ve korona olan hastalar ile birlikte farklı bir listeye aktarılır
def corona_kontrol():
    dosya=open("corona.txt","w")
    dosya.close()
    dosya=open("corona.txt","a")
    for a in range(len(liste)):
        if liste[a]["teshis"] == "COVID-19":
            print("{} KARANTİNAYA ALINMIŞTIR YANINA EKİPMANSIZ YAKLAŞMAYINIZ".format(liste[a]))
            karantina.append(liste[a])
            dosya.write("AD:\tSOYAD:\tTESHIS:\n")
            dosya.write(liste[a]["ad"]+"\t")
            dosya.write(liste[a]["soyad"]+"\t")
            dosya.write(liste[a]["teshis"]+"\n")
            dosya.write("KIMLIK NUMARASI:\n")
            dosya.write(str(liste[a]["kimlik_no"])+"\n")

    dosya.close()
#----------------------------------------------------------------------------------------------
#hasta iyileşir veya vefat ederse hastane kayıtlarından silinmek yerine arşivleinr ki gerektiği zamanlar kontrol yapılabilinsin ve yeni listelere eklenirler
#ve hastanın teşhisi COVID-19 değilse ölüm sebebi sorulmaz
def kayit_arsivleme():

    e=0
    saay=0
    neden=0
    while e==0:
        dosya = open("kaytlilar.txt", "r")
        dosya2 = open("kayit_arsivi.txt", "a")
        dosya3 = open("corona.txt", "r")
        dosya4 = open("olum_list.txt", "a")
        dosya5 = open("iyilesen_list.txt", "a")
        kor_kay_ars = dosya3.readlines()
        kay_sil = dosya.readlines()
        kimlik_no = int(input("Kayıdını silmek istediğiniz hastanın kimlik numarasını giriniz"))
        if len(kay_sil) == 0:
            print("Kayıtlı hasta sayısı 0'dır\nBu yüzden kayıt silme işlemi gerçekleşemez")
            break
        for h in range(0, len(kay_sil)):
            if len(kay_sil)==0:              # herhangi bir silinme işlemi gerçekleşirse hata almamak için kontrol yapıldı
                break
            for s in range(len(kay_sil)):    #dögü içinde aynı döngü açılmadığı zaman out of range hatası alındı
                if str(kimlik_no) + "\n" == kay_sil[s]:
                    print(" kimlik no bulundu \n kayıt siliniyor")
                    dosya2.write("AD:\tSOYAD:\tTESHIS:\n")
                    dosya2.write(kay_sil[s-2])
                    dosya2.write("KIMLIK NUMARASI:\n")
                    dosya2.write(str(kay_sil[s]))
                    if (str(kimlik_no)+"\n") in kor_kay_ars:
                        def k_kayit_arsivleme():#İÇ İÇE FONKSİYON TANIMANLDI VE KULLANILDI
                            et = 0
                            saay = 0
                            neden = 0
                            uzun = len(kor_kay_ars)
                            while et == 0:
                                for a in range(uzun):
                                    if str(kimlik_no) + "\n" == kor_kay_ars[a]:
                                        neden = int(
                                            input(
                                                "Korona olmuş hastanın kayıt silinme sebebi \nHASTANIN VEFAT ETMESİ İSE 1'E BASINIZ\n"
                                                "HASTANIN İYİLEŞMESİ İSE 2'YE BASINIZ"))
                                        if neden == 1:
                                            dosya4.write("AD:\tSOYAD:\tTESHIS:\n")
                                            dosya4.write(kor_kay_ars[a])
                                            dosya4.write("KIMLIK NUMRASI\n")
                                            dosya4.write(kor_kay_ars[a-2])

                                        if neden == 2:
                                            dosya5.write("AD:\tSOYAD:\tTESHIS:\n")
                                            dosya5.write(kor_kay_ars[a])
                                            dosya5.write("KIMLIK NUMARASI\n")
                                            dosya5.write(kor_kay_ars[a-2])

                                        del kor_kay_ars[a]
                                        del kor_kay_ars[a - 1]
                                        del kor_kay_ars[a - 2]
                                        del kor_kay_ars[a - 3]
                                        break

                                break
                        k_kayit_arsivleme()
                    del kay_sil[s]
                    del kay_sil[s - 1]
                    del kay_sil[s - 2]
                    del kay_sil[s - 3]
                    break
            saay = int(input(
                "Yeni kayıt silme işlemi yapmak için 1'e \nKayıt silme işlmini bitirmek için 2'e basınız"))
            if saay == 1:
                break# iki ifadenin de break olmasının sebebi sonsuz döngüden sonra kurulan döngüyü kırıyor ve aslında continue görevi görüyor
            elif saay == 2:
                print("Kayıt silme işlemi bitirildi")
                break


            if str(kimlik_no) + "\n" not in kay_sil:
                print("kimlik no bulunamadı")
                break
            saay = int(
                input(
                    "Yeni kayıt silme işlemi yapmak için 1'e \nKayıt silme işlmini bitirmek için 2'e basınız"))
            if saay == 1:
                break
            elif saay == 2:
                print("Kayıt silme işlemi bitirildi")
                break

        dosya.close()
        dosya2.close()
        dosya3.close()
        dosya3 = open("corona.txt", "w")
        for m in range(len(kor_kay_ars)):
            dosya3.write(kor_kay_ars[m])
        dosya3.close()
        dosya = open("kaytlilar.txt", "w")
        for p in range(len(kay_sil)):
            dosya.write(kay_sil[p])
        dosya.close()
        dosya4.close()
        dosya5.close()
        k_yatak_say()  # --------------İÇ İÇE FONKSİYONUM-------------
        if saay == 2:
            break
        if saay == 1:
            continue



#-------------------------------------------------------------------------------------------
def hasta_kontrol():
    e = 0
    y=0
    istek=0
    dosya=open("kaytlilar.txt","r")
    liste2=dosya.readlines()
    while e==0:
        for i in range(len(liste2)):
            kimlik_no = int(input("Aramak istediğiniz hastanın kimlik numarasını giriniz"))
            for o in range(len(liste2)):
                if (str(kimlik_no) + "\n") == liste2[o]:
                    print("AD:\tSOYAD:\tTEŞHİS:")
                    print(liste2[o-2])
                    print("KİMLİK NUMARASI")
                    print(liste2[o])
                    y=1
                    break#kimlik no sadece bir kere olacağı için break olsun ki döngü boşa dönmesin
                else:
                    print("Kimlik numarası kayıtlı hasta bulunmamaktadır\n"
                          "Tekrar deneyiniz")
                    break

            if y==1:
                break
        istek = int(input("BAŞKA BİR HASTANIN KAYDINA DAHA BAKMAK İSTERSENİZ 1'E BASINIZ\n"
                          "İSLEMİ BİTİRMEK İÇİN 2'YE BASINIZ"))
        if istek==1:
            continue
        if istek==2:
            break
    dosya.close()

#------------------------------------------------------------------------------------------
def k_yatak_say():
    dosyax=open("corona.txt","r")
    yatak_say=dosyax.readlines()
    y_yatak_sayisi=yatak_sayisi-(len(yatak_say)/4)
    print("COVİD-19 teşhisli hastalar için ayrılan şuan ki yatak sayısı=",y_yatak_sayisi)
    dosyax.close()
#------------------------------------------------------------------------------------------
def arsiv_arama():
    e = 0
    y = 0
    istek = 0
    dosya = open("kayit_arsivi.txt", "r")
    liste2 = dosya.readlines()
    while e == 0:
        for i in range(len(liste2)):
            kimlik_no = int(input("Aramak istediğiniz hastanın kimlik numarasını giriniz"))
            for o in range(len(liste2)):
                if (str(kimlik_no) + "\n") == liste2[o]:
                    print(liste2[o-3])
                    print(liste2[o -2])
                    print(liste2[o-1])
                    print(liste2[o])
                    y = 1
                    break
                else:
                    print("Kimlik numarası bulunamadı\n"
                          "Tekrar deneyiniz")
                    break
            if y == 1:
                break
        istek = int(input("BAŞKA BİR HASTANIN KAIYDINA DAHA BAKMAK İSTERSENİZ 1'E BASINIZ\n"
                          "İSLEMİ BİTİRMEK İÇİN 2'YE BASINIZ"))
        if istek == 1:
            continue
        if istek == 2:
            break
    dosya.close()
#------------------------------------------------------------------------------------------
def kayit_guncelleme():

    e=0
    tc=0
    while e==0:
        dosya = open("kaytlilar.txt", "r")
        kayit_list = dosya.readlines()
        dosya.close()
        dosya2 = open("corona.txt", "r")
        coro_kayit_list = dosya2.readlines()
        dosya2.close()

        tc=int(input("KAYDI GÜNCELLENECEK KİŞİNİN KİMLİK NUMARASINI GİRİNİZ\n"))
        if str(tc)+"\n" not in kayit_list:
            print("BÖYLE BİR KİMLİK NUMARASI KAYITLI DEĞİLDİR TEKRAR DENEYİNİZ\n")
            continue
        for i in range(len(kayit_list)):
            if str(tc)+"\n" == kayit_list[i]:
                del kayit_list[i]
                del kayit_list[i-1]
                del kayit_list[i-2]
                del kayit_list[i-3]
        dosya = open("kaytlilar.txt", "w")
        for a in range(len(kayit_list)):
            dosya.write(kayit_list[a])
        dosya.close()
        for p in range(len(coro_kayit_list)):
            if str(tc)+"\n"==coro_kayit_list[p]:
                del coro_kayit_list[p]
                del coro_kayit_list[p-1]
                del coro_kayit_list[p-2]
                del coro_kayit_list[p-3]
        dosya2=open("corona.txt","w")
        for o in range(len(coro_kayit_list)):
            dosya2.write(coro_kayit_list[o])
        dosya2.close()

        print("KAYIDI TEKRAR ALIN\n")
        yeni_kayit()
        corona_kontrol()
        k_yatak_say()
        break




#------------------------------------------------------------------------------------------
def menu_m():
    dosya=open("corona.txt","r")#-------HER DOSYANIN LİSTESİNİN ADINI UNUTUNCA EN BAŞA ÇIKMAYALIM DİYE HER FONKSİYONDA AYRI AYRI OKUTTUM
    corona_listesi=dosya.readlines()
    dosya1=open("kaytlilar.txt","r")
    tum_hastalar=dosya1.readlines()
    dosya2=open("kayit_arsivi.txt","r")
    arsiv_kayitlar=dosya2.readlines()
    dosya3=open("iyilesen_list.txt","r")
    iyilesenler_listesi=dosya3.readlines()
    dosya4=open("olum_list.txt","r")
    olum_listesi=dosya4.readlines()
    dosya.close()
    dosya1.close()#DOSYALARI KAPATMAMIN SEBEBİ READLİNES KOMUTUNU KULLANDIĞIM ZAMAN OKUMA MODUNDA OLSA BİLE READ MODUNUN DÜZGÜN ÇALIŞMAMASI
    dosya2.close()
    dosya4.close()
    dosya3.close()

    sayiii = 0
    islemm = 0
    devam = 0
    silme = 0
    oran = 0
    dosya4 = open("olum_list.txt", "r")
    while sayiii == 0:
        print("-----------------------MENU---------------------------"
              "YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ\n"
              "1-YENİ HASTA KAYDI OLUŞTURMAK\n"
              "2-KAYITLI HASTANIN KAYDINI SİLMEK\n"
              "3-HASTANDEDKİ TÜM KAYITLI COVİD-19 HASTALARINI GÖRMEK\n"
              "4-HASTANEDEİ TÜM KAYITLI HASTALARI GÖRMEK\n"
              "5-KAYITLI HASTANIN DURUMUNU KONTROL ETMEK\n"
              "6-COVİD-19 SEBEBİ İLE VEFAT EDEN HASTALARI GÖRMEK\n"
              "7-COVİD-19 TEDAVİSİ BAŞARILI BİR ŞEKİLDE BİTMİŞ HASTALARI GÖRMEK\n"
              "8-İYİLEŞNLER VE VEFAT EDENLERİN SAYISINI GÖRMEK\n"
              "9-ARŞİVLENEN KAYITLARIN HEPSİNİ GÖRMEK \n"
              "10-ARŞİVDE KAYITLI BİR KİŞİYİ GÖRMEK\n"
              "11-KAYIT GÜNCELLEME YAPMAK\n")
        islemm = int(input("HANGİ İŞLEMİ YAPMAK İSTİYORSANIZ NUMARASINI TUŞLAYIN"))
        if islemm == 1:
            yeni_kayit()
            corona_kontrol()
            k_yatak_say()
        if islemm == 2:
            kayit_arsivleme()

        if islemm == 3:
            dosya=open("corona.txt","r")
            print(dosya.read())
            dosya.close()

        if islemm == 4:
            dosya1 = open("kaytlilar.txt", "r")

            print(dosya1.read())
            dosya1.close()

        if islemm == 5:
            hasta_kontrol()
        if islemm == 6:
            dosya_yeni2 = open("olum_list.txt", "r")
            dosya_yeni3=dosya_yeni2.readlines()
            dosya_yeni2.close()
            if len(dosya_yeni3) == 0:
                print("COVİD-19 SEBEBİ İLE VEFAT EDEN HASTA SAYISI 0. HEP BÖYLE KALMASI DİLEĞİ İLE")
            else:
                dosya_yeni2=open("olum_list.txt","r")
                print("COVİD-19 SEBEBİ İLE VEFAT EDEN HASTALAR:")
                print(dosya_yeni2.read())
                dosya_yeni2.close()

        if islemm == 7:
            dosya_yeni = open("iyilesen_list.txt", "r")
            dosya_yeni1 = dosya_yeni.readlines()
            dosya_yeni.close()
            if len(dosya_yeni1) == 0:
                print("HASTANEDE COVİD-19 TEDAVİSİ OLUMLU SONUÇLANAN KİMSE YOKTUR")
            else:
                dosya_yeni=open("iyilesen_list.txt","r")
                print("COVİD-19 TEDAVİSİ BAŞARI İLE TAMAMLANMIŞ HASTALAR")
                print(dosya_yeni.read())
                dosya_yeni.close()

        if islemm == 8:
            sayma_dosya1 = open("olum_list.txt", "r")
            vefat_say=sayma_dosya1.readlines()
            print("COVİD-19 NEDENİ İLE VEFAT EDEN HASTA SAYISI")
            print(len(vefat_say)/4)
            sayma_dosya2=open("iyilesen_list.txt","r")
            iyilesen_say=sayma_dosya2.readlines()
            print("COVİD-19 TEDAVİSİ BAŞARI İLE SONUCLANAN HASTA SAYISI")
            print(len(iyilesen_say)/4)
        if islemm==9:

            dosya2=open("kayit_arsivi.txt","r")
            arsiv_listesi = dosya2.read()
            print("HASTANE KAYDI ARŞİVLENMİŞ TÜM HASTALAR:")
            print(arsiv_listesi)


        if islemm==10:
            arsiv_arama()
        if islemm==11:
            kayit_guncelleme()


        devam = int(input("MENÜYE DÖNMEK İÇİN 1'E\n"
                          "UYGULAMADAN CIKMAK İÇİN 2'YE BASINIZ"))
        if devam == 1:
            continue
        if devam == 2:
            break



#-------------------------------------------

menu_m()
