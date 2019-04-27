import random
import time
import sys 

########## İskambil Oyunu için Kod
########## Hazırlayan: Görkem Seçkin
########## Başlangıç Tarihi: 15 Nisan 2019
########## Son Düzenleme Tarihi: 23 Nisan 2019

########## list_types ve list_card_values, Iskambil class'ının instance attribute'una verilmek için;cardType,cardValue
list_types = ["kupa","karo","maça","sinek"]
list_card_values = ["as",2,3,4,5,6,7,8,9,10,"vale","kız","papaz"]
########## list_abcd ve dict_for_creating sadece instance yaratmak için tek sefer kullanılıyor.
list_abcd = ["A","B","C","D"]
########## list_13 hem instance yaratmak hem de Iskambil class'ının instance attribute'una verilmek için var;cardValue_int
list_13 = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
dict_for_creating = {}
for a in range(0,13):
    for b in range(0,4):
        dict_for_creating.update({ (list_abcd[b] + list_13[a]) : [list_types[b],list_card_values[a],list_13[a]] })

########## oyun_raporu, oyun sırasında bütün olanları not ediyor
oyun_raporu = "\n\t\t\t OYUN RAPORU\n"


########## Bir destedeki bütün kağıtlar Iskambil class'ının instance'ı olarak tanımlanır. 
class Iskambil:
    tanimli = []
    def __init__(self,cardType,cardValue,cardValue_int):
        self.type = cardType
        self.value = cardValue
        self.value_int = cardValue_int
        self.name = "{}_{}".format(self.type,self.value)
        self.tanimli.append(self.name)
        self.mark10 = ""
        self.markAS = ""
        self.mark7 = 2

########## all_cards (52 iskambil kağıdı instance'larını içeren bir liste) oluşturuluyor.
all_cards = []
for a in dict_for_creating:
    all_cards.append(Iskambil(dict_for_creating[a][0],dict_for_creating[a][1],int(dict_for_creating[a][2])))

########## dict_lookup (bütün iskambil kağıtlarının all_cards'daki index numarasını bize gösteren bir dictionary. İleride kullanım amaçlı.
dict_lookup = {}
integer1 = 0
for a in Iskambil.tanimli:
    dict_lookup.update({ a : integer1 })
    integer1 +=1

########## Oyun oynanırken, ortada en üstteki kağıdın değerini tutuyor. Girdi olarak bir iskambil kağıdı instance'ı alıyor.
class Orta:
    ortada = []
    def __init__(self, card_instance):
        self.type = card_instance.type
        self.value = card_instance.value
        self.value_int = card_instance.value_int
        self.ortada.append(card_instance)
        self.ortadaki_kart = card_instance
        if self.value == "vale":
            global secim
            self.type = secim
    
    @classmethod
    def baslangic(cls):
        kart_degil = Iskambil("sinek",0,0)
        return Orta(kart_degil)

########## Karışık sıralanmış 52 kağıtlık deste oluşturuyor. all_cards listesini kullanıyor. Çıktı: deck adında liste. random modülünü kullanıyor.
def create_deck():
        sayi_listesi = list(range(52))
        random.shuffle(sayi_listesi)
        deck = []
        for i in sayi_listesi:
            deck.append(all_cards[i]) 
        return deck

########## Desteyi karıyor. deck adlı listenin elemanlarının sırasını depiştiriyor. Çıktı: deck adında liste. random modülünü kullanıyor.      
def shuffle_deck(input_deck):
    random.shuffle(input_deck)
    return input_deck

########## Bir oyuncunun eli. yeni_el, verilen sayıda kağıdı desteden çekip self.cards listesine ekliyor.
############### game eklemesi: self.playertype, bilgisayar ise 111, eğer kullanıcı ise string olarak kaydedilecek
############### game eklemesi: yeni_el_user(), kullanıcıya el oluşturmak için
class El:
    def __init__(self,player):
        self.playername = str(player)
        self.cards = []

    def yeni_el(self,a):
        self.cards = [deck.pop(0) for i in range(a)]
        self.playertype = 111

    def yeni_el_user(self,a):
        self.cards = [deck.pop(0) for i in range(a)]
        self.playertype = "user"



class Tur:
    def __init__(self,oyuncu_el):
        self.oyuncu = oyuncu_el
        if orta.value == 7:
            cards_7 = []
            for card in self.oyuncu.cards:
                if card.value == 7:
                    cards_7.append(card)
            if len(cards_7) != 0:
                selected_7 = random.choice(cards_7)
                selected_7.mark7 += orta.ortadaki_kart.mark7
                self.kart_oyna(selected_7)

            else: 
                self.kart_cek(orta.ortadaki_kart.mark7)
                self.olasi_hamleleri_bul()
                if len(self.hamleler) == 0:
                    self.kart_cek(1)
                    self.olasi_hamleleri_bul()
                    if len(self.hamleler) != 0:
                        self.kart_oyna(random.choice(self.hamleler))
                else:
                    self.kart_oyna(random.choice(self.hamleler))
        else:
            self.olasi_hamleleri_bul()
            if len(self.hamleler) == 0:
                self.kart_cek(1)
                self.olasi_hamleleri_bul()
                if len(self.hamleler) != 0:
                    self.kart_oyna(random.choice(self.hamleler))
            else:
                self.kart_oyna(random.choice(self.hamleler))

    def olasi_hamleleri_bul(self):
        global oyun_raporu
        self.hamleler = []
        for card in self.oyuncu.cards:
            if card.type == orta.type:
                self.hamleler.append(card)
            elif card.value == orta.value:
                self.hamleler.append(card)
            elif card.value == "vale":
                self.hamleler.append(card)
        if i < 4:
            hamleler_ilk_tur = []
            for card in self.hamleler:
                if card.type != "sinek":
                    continue
                if card.value == "as" or card.value == 7 or card.value == 10 or card.value == "vale":
                    continue
                hamleler_ilk_tur.append(card)
            self.hamleler = hamleler_ilk_tur
        oyun_raporu += "olası hamleler: {}\n".format([h.name for h in self.hamleler])
        

########## kart_cek'te, tek deste oynandığı için "if len(deck) < 8: ifadesi" var. 
##########Eğer çift deste oynanırsa, burayı 16 yap! (çünkü bir anda çekilebilecek max. kart sayısı 16 olur(8tane7))
    def kart_cek(self,a):
        global deck
        global oyun_raporu
        
        try:
            global orta
            oyun_raporu += "\ndeste uzunluğu, kart çekemeden önce: {}\n".format(len(deck))
            cards_to_be_drawn = [deck.pop(0) for i in range(a)]
            self.oyuncu.cards.extend(cards_to_be_drawn)
            print("\n{} {} kart çekti".format(self.oyuncu.playername,a))
            oyun_raporu += "deste uzunluğu, kart çektiktikten sonra: {}\n".format(len(deck))
            oyun_raporu += "{}'in yeni eli: {}\n".format(self.oyuncu.playername,[k.name for k in self.oyuncu.cards])
            if len(deck) < 8:
                print("\ndestedeki kart sayısı:",len(deck))
                oyun_raporu += "\ndestedeki kart sayısı: {}\n".format(len(deck))
                oyun_raporu += "ortadaki kart sayısı: {}\n".format(len(orta.ortada))
                temporary_deck1 = orta.ortada[1:-1]
                temporary_deck1 = shuffle_deck(temporary_deck1)
                deck.extend(temporary_deck1)
                Orta.ortada = [orta.ortada[0],orta.ortada[-1]]
                for card in deck:
                    card.mark10 = ""
                    card.markAS = ""
                    card.mark7 = 2
                print("ortadaki kağıtlar karılıp yeni deste yapıldı")
                oyun_raporu += "ortadaki kağıtlar karılıp yeni deste yapıldı\n"
                time.sleep(1)
                print("destedeki kart sayısı:{}".format(len(deck)))
                oyun_raporu += "destedeki kart sayısı:{}\n".format(len(deck))
                oyun_raporu += "Deste:{}\n".format([k.name for k in deck])
                oyun_raporu += "ortada kalanlar: {}\n".format([k.name for k in orta.ortada])
        except Exception as hata :
            print("\n\n\t\tKART ÇEK HATA VERDİ,\t adım: {},\n deste uzunluğu: {},\n ortanın uzunluğu: {},\n destedeki kartlar: {}\n".format(i,len(deck),len(orta.ortada),[k.name for k in deck]))
            oyun_raporu += "\n\n\t\tKART ÇEK HATA VERDİ,\t adım: {},\n deste uzunluğu: {},\n ortanın uzunluğu: {},\n destedeki kartlar: {}\n\n".format(i,len(deck),len(orta.ortada),[k.name for k in deck])
            print(hata)
            oyun_raporu += "Hata:{}\n".format(hata)

    def kart_oyna(self,card_instance):
        global oyun_raporu
        if card_instance.value == "vale":
            global secim
            secim = random.choice(list_types)
        global orta
        orta = Orta(card_instance)
        self.oyuncu.cards.remove(card_instance)
        print("\n\t\t\t{} {} oynadı".format(self.oyuncu.playername,card_instance.name))
        oyun_raporu += "{} {} oynadı\n".format(self.oyuncu.playername,card_instance.name)
        oyun_raporu += "ortadaki kart sayısı: {}\n".format(len(orta.ortada))
        if card_instance.value == "vale":
            print("valeden dolayı değişen orta: {}".format(secim))
            oyun_raporu += "valeden dolayı değişen orta: {}\n".format(secim)




############# Tutorial için Tur_user class'ı, oyunu öğrenmek isteyen kullanıcı için uyarlanmış Tur class'ı
class Tur_user:
    def __init__(self,oyuncu_el):
        self.oyuncu = oyuncu_el
        time.sleep(1)
        print("\n\tTur sende")
        global oyun_raporu
        oyun_raporu += "\n\tTur sende\n"
        time.sleep(1)
        print("\n\tElinde {} kart var".format(len(self.oyuncu.cards)))
        oyun_raporu += "\n\tElinde {} kart var\n".format(len(self.oyuncu.cards))
        time.sleep(1)
        print("\n\t{}".format([k.name for k in self.oyuncu.cards]))
        oyun_raporu += "\n\t{}\n".format([k.name for k in self.oyuncu.cards])
        time.sleep(3)
        print("\n\tortanın değeri:\n\t{} {}".format(orta.type,orta.value))
        oyun_raporu += "\n\tortanın değeri:\n\t{} {}\n".format(orta.type,orta.value)
        time.sleep(2)

        if orta.value == 7:
            print("\n\tEn son {} oynandı".format(orta.ortadaki_kart.name))
            oyun_raporu += "\n\tEn son {} oynandı\n".format(orta.ortadaki_kart.name)
            time.sleep(2)
            print("\n\tEğer elinde 7'li varsa hemen onu oyna!")
            oyun_raporu += "\n\tEğer elinde 7'li varsa hemen onu oyna!\n"
            time.sleep(1)
            cards_7 = []
            for card in self.oyuncu.cards:
                if card.value == 7:
                    cards_7.append(card)
            if len(cards_7) != 0:
                selected_7 = self.hamle_sec7_user(cards_7)
                selected_7.mark7 += orta.ortadaki_kart.mark7
                self.kart_oyna_user(selected_7)

            else:
                time.sleep(1)
                print("\n\tMaalesef, elinde hiç 7'li yok")
                oyun_raporu += "\n\tMaalesef, elinde hiç 7'li yok\n"
                time.sleep(2)
                print("\n\tDesteden {} kart çekmek zorundasın".format(orta.ortadaki_kart.mark7))
                oyun_raporu += "\n\tDesteden {} kart çekmek zorundasın\n".format(orta.ortadaki_kart.mark7)
                time.sleep(2)
                self.kart_cek_user(orta.ortadaki_kart.mark7)

                self.olasi_hamleleri_bul()
                if len(self.hamleler) == 0:
                    print("\n\tElinde, bu tur oynayabileceğin kart yok")
                    oyun_raporu += "\n\tElinde, bu tur oynayabileceğin kart yok\n"
                    time.sleep(2)
                    print("\n\tDesteden bir kart çek")
                    oyun_raporu += "\n\tDesteden bir kart çek\n"
                    time.sleep(2)
                    self.kart_cek_user(1)
                    self.olasi_hamleleri_bul()
                    if len(self.hamleler) != 0:
                        selected = self.hamle_sec_user()
                        self.kart_oyna_user(selected)
                    else:
                        time.sleep(1)
                        print("\n\tElinde, bu tur oynayabileceğin kart yok")
                        oyun_raporu += "\n\tElinde, bu tur oynayabileceğin kart yok\n"
                        time.sleep(1)
                        print("\n\tTurun bitti")
                        oyun_raporu += "\n\tTurun bitti\n"
                        time.sleep(1)
                else:
                    selected = self.hamle_sec_user()
                    self.kart_oyna_user(selected)
        else:
            self.olasi_hamleleri_bul()
            if len(self.hamleler) == 0:
                print("\n\tElinde, bu tur oynayabileceğin kart yok")
                oyun_raporu += "\n\tElinde, bu tur oynayabileceğin kart yok\n"
                time.sleep(2)
                print("\n\tDesteden bir kart çek")
                oyun_raporu += "\n\tDesteden bir kart çek\n"
                time.sleep(2)
                self.kart_cek_user(1)
                self.olasi_hamleleri_bul()
                if len(self.hamleler) != 0:
                    selected = self.hamle_sec_user()
                    self.kart_oyna_user(selected)
                else:
                    time.sleep(1)
                    print("\n\tElinde, bu tur oynayabileceğin kart yok")
                    oyun_raporu += "\n\tElinde, bu tur oynayabileceğin kart yok\n"
                    time.sleep(1)
                    print("\n\tTurun bitti")
                    oyun_raporu += "\n\tTurun bitti\n"
                    time.sleep(1)
            else:
                selected = self.hamle_sec_user()
                self.kart_oyna_user(selected)

    def olasi_hamleleri_bul(self):
        self.hamleler = []
        global oyun_raporu
        for card in self.oyuncu.cards:
            if card.type == orta.type:
                self.hamleler.append(card)
            elif card.value == orta.value:
                self.hamleler.append(card)
            elif card.value == "vale":
                self.hamleler.append(card)
        if i < 4:
            time.sleep(1)
            print("\n\tBu oyunda, tur sana ilk kez geldi")
            oyun_raporu += "\n\tBu oyunda, tur sana ilk kez geldi\n"
            time.sleep(2)
            print("\n\tİlk turunda sadece sinek oynayabilirsin")
            oyun_raporu += "\n\tİlk turunda sadece sinek oynayabilirsin\n"
            time.sleep(3)
            print("\n\tAyrıca bu tur,")
            oyun_raporu += "\n\tAyrıca bu tur,\n"
            time.sleep(1)
            print("\n\tsinek de olsa 7'li, 10'lu, as veya vale oynayamazsın")
            oyun_raporu += "\n\tsinek de olsa 7'li, 10'lu, as veya vale oynayamazsın\n"
            time.sleep(3)
            print("\n\tMerak etme,")
            oyun_raporu += "\n\tMerak etme,\n"
            time.sleep(1)
            print("\n\therkes bir el oynayınca bu kısıtlama kalkacak")
            oyun_raporu += "\n\therkes bir el oynayınca bu kısıtlama kalkacak\n"
            time.sleep(1)
            hamleler_ilk_tur = []
            for card in self.hamleler:
                if card.type != "sinek":
                    continue
                if card.value == "as" or card.value == 7 or card.value == 10 or card.value == "vale":
                    continue
                hamleler_ilk_tur.append(card)
            self.hamleler = hamleler_ilk_tur
        print("\n\tolası hamlelerin: {}".format([h.name for h in self.hamleler]))
        oyun_raporu += "\n\tolası hamlelerin: {}\n".format([h.name for h in self.hamleler])
        time.sleep(3)


########## kart_cek'te, tek deste oynandığı için "if len(deck) < 8: ifadesi" var. 
##########Eğer çift deste oynanırsa, burayı 16 yap! (çünkü bir anda çekilebilecek max. kart sayısı 16 olur(8tane7))
    def kart_cek_user(self,a):
        global deck
        global oyun_raporu
        
        try:
            global orta
            oyun_raporu += "\ndeste uzunluğu, kart çekemeden önce: {}\n".format(len(deck))
            cards_to_be_drawn = [deck.pop(0) for i in range(a)]
            self.oyuncu.cards.extend(cards_to_be_drawn)
            time.sleep(1)
            print("\n\t{} kart çektin".format(a))
            oyun_raporu += "\n\t{} kart çektin\n".format(a)
            time.sleep(1)
            oyun_raporu += "deste uzunluğu, kart çektiktikten sonra: {}\n".format(len(deck))
            print("\n\tÇektiğin kartlar\n\t{}".format([k.name for k in cards_to_be_drawn]))
            oyun_raporu += "\n\tÇektiğin kartlar\n\t{}\n".format([k.name for k in cards_to_be_drawn])
            time.sleep(2)
            print("\n\tŞu an elindekiler\n\t{}".format([k.name for k in self.oyuncu.cards]))
            oyun_raporu += "\n\tŞu an elindekiler\n\t{}\n".format([k.name for k in self.oyuncu.cards])
            time.sleep(2)
            if len(deck) < 8:
                print("\ndestedeki kart sayısı: {}".format(len(deck)))
                oyun_raporu += "\ndestedeki kart sayısı: {}\n".format(len(deck))
                oyun_raporu += "ortadaki kart sayısı: {}\n".format(len(orta.ortada))
                temporary_deck1 = orta.ortada[1:-1]
                temporary_deck1 = shuffle_deck(temporary_deck1)
                deck.extend(temporary_deck1)
                Orta.ortada = [orta.ortada[0],orta.ortada[-1]]
                for card in deck:
                    card.mark10 = ""
                    card.markAS = ""
                    card.mark7 = 2
                print("ortadaki kağıtlar karılıp yeni deste yapıldı")
                oyun_raporu += "ortadaki kağıtlar karılıp yeni deste yapıldı\n"
                time.sleep(1)
                print("destedeki kart sayısı:",len(deck))
                oyun_raporu += "destedeki kart sayısı: {}\n".format(len(deck))
                oyun_raporu += "Deste: {}\n".format([k.name for k in deck])
                oyun_raporu += "ortada kalanlar: {}\n".format([k.name for k in orta.ortada])
                time.sleep(2)
        except Exception as hata :
            print("\n\n\t\tKART ÇEK HATA VERDİ,\t adım: {},\n deste uzunluğu: {},\n ortanın uzunluğu: {},\n destedeki kartlar: {}\n\n".format(i,len(deck),len(orta.ortada),[k.name for k in deck]))
            oyun_raporu += "\n\n\t\tKART ÇEK HATA VERDİ,\t adım: {},\n deste uzunluğu: {},\n ortanın uzunluğu: {},\n destedeki kartlar: {}\n".format(i,len(deck),len(orta.ortada),[k.name for k in deck])
            print(hata)
            oyun_raporu += "Hata: {}\n".format(hata)

    def kart_oyna_user(self,card_instance):
        global oyun_raporu
        if card_instance.value == "vale":
            time.sleep(1)
            print("\n\tOrtaya bir vale oynamak istiyorsun")
            oyun_raporu += "\n\tOrtaya bir vale oynamak istiyorsun\n"
            time.sleep(1)
            print("\n\tValeyle ortayı istediğin şekle değiştirebilirsin")
            oyun_raporu += "\n\tValeyle ortayı istediğin şekle değiştirebilirsin\n"
            time.sleep(2)
            cevap_vale = str(input("\n\tOrta ne olsun istersin?\n\t<kupa/karo/maça/sinek>\n\t")).lower()
            global secim
            secim = cevap_vale
        global orta
        orta = Orta(card_instance)
        self.oyuncu.cards.remove(card_instance)
        time.sleep(1)
        print("\n\t{} oynadın".format(card_instance.name))
        oyun_raporu += "\n\t{} oynadın\n".format(card_instance.name)
        time.sleep(1)
        print("\n\tElindekiler\n\t{}".format([k.name for k in self.oyuncu.cards]))
        oyun_raporu += "\n\tElindekiler\n\t{}\n".format([k.name for k in self.oyuncu.cards])
        time.sleep(2)
        oyun_raporu += "\nortadaki kart sayısı: {}\n".format(len(orta.ortada))
        time.sleep(1)
        if card_instance.value == "vale":
            print("valeden dolayı değişen orta: {}".format(secim))
            oyun_raporu += "valeden dolayı değişen orta: {}\n".format(secim)
            time.sleep(1)

    def hamle_sec_user(self):
        global oyun_raporu
        kontrol1 = 0
        while kontrol1 < 1:
            cevap_hamle_sec = str(input("\n\tHangi kartı oynamak istersin?\n\t"))
            oyun_raporu += "\n\toynanmak istenen kart: {}\n".format(cevap_hamle_sec)
            for card in self.hamleler:
                if card.name == cevap_hamle_sec:
                    hamle = card
                    kontrol1 = 1
                    return hamle
            print("\n\tOynayabileceğin bir kartı yazmadın")
            oyun_raporu += "\n\tOynayabileceğin bir kartı yazmadın\n"
            time.sleep(1)
            print("\n\tolası hamlelerin: {}".format([h.name for h in self.hamleler]))
            oyun_raporu += "\n\tolası hamlelerin: {}\n".format([h.name for h in self.hamleler])
            time.sleep(1)

    def hamle_sec7_user(self,cards7):
        global oyun_raporu
        kontrol1 = 0
        while kontrol1 < 1:
            cevap7li = str(input("\n\tOynayacağın kartın adını yaz\n\t{}\n\t".format(self.oyuncu.cards)))
            oyun_raporu += "\n\toynanmak istenen kart: {}\n".format(cevap7li)
            for card in cards7:
                if card.name == cevap7li:
                    hamle7 = card
                    kontrol1 = 1
                    return hamle7
            print("\n\tOynayabileceğin bir kartı yazmadın")
            oyun_raporu += "\n\tOynayabileceğin bir kartı yazmadın\n"
            time.sleep(1)
            print("\n\tolası hamlelerin: {}".format([h.name for h in self.hamleler]))
            oyun_raporu += "\n\tolası hamlelerin: {}\n".format([h.name for h in self.hamleler])
            time.sleep(1)


def giris_karsilama():
    karsilama_yazisi = """
    \n\t\t\tPYTHON'LA OYNAYALIM
    \n\tMerhaba,\n\tPis Yedili oyununa hoşgeldin!\n
    """
    print("_"*125)
    print(karsilama_yazisi)
    time.sleep(2)
    cevap1 = str(input("\n\tPis Yedili oynamaya hazır mısın?\n<Evet/Hayır>\n")).lower()
    if cevap1 == "evet":
        print("\n\tHemen başlayalım!")
        time.sleep(2)
    else:
        print("\n\tMerak etme, oyunu öğrenmende yardımcı olacağım")
        time.sleep(2)
    cevap2 = str(input("\n\tÖncelikle, adını aşağıya yazar mısın?\n"))
    print("\n\tTeşekkürler {}".format(cevap2))
    time.sleep(2)
    print("\n\tKartları dağıtmaya başlıyorum")
    time.sleep(1)
    return cevap2
    

def oyunabasla():
    dosya = open("C:\My folder for Visual Studio Code\cardgame\cardgame_game_tutorial_ciktilari\\tutorial3.txt","w+")

    global orta
    orta = Orta.baslangic()
    global deck
    deck = create_deck()
    global oyun_raporu
    oyun_raporu += "Oyun başlatıldı\n"

    user_playername = giris_karsilama()
    oyun_raporu += "Oyuncunun(kullanıcı) adı: {}\n".format(user_playername)

    oyun_raporu += "oyundaki kart sayısı: {}\n52 kart + başlangıçta ortayı belirten 'kart',(joker yok)\n".format(len(Iskambil.tanimli))
    oyun_raporu += "Destedeki kartlar, sırayla:\n{}\n".format([k.name for k in deck])
    
    time.sleep(1)
    oyuncu1_el = El("oyuncu1")
    oyuncu1_el.yeni_el(7)
    print("{}, 7 kartı var".format(oyuncu1_el.playername))
    oyun_raporu += "Oyuncu1'in eli: {}\n".format([k.name for k in oyuncu1_el.cards])
    oyun_raporu += "Deste: {}\n".format([k.name for k in deck])
    time.sleep(1)
    oyuncu2_el = El("oyuncu2")
    oyuncu2_el.yeni_el(7)
    print("{}, 7 kartı var".format(oyuncu2_el.playername))
    oyun_raporu += "Oyuncu2'nin eli: {}\n".format([k.name for k in oyuncu2_el.cards])
    oyun_raporu += "Deste: {}\n".format([k.name for k in deck])
    time.sleep(1)
    oyuncu3_el = El("oyuncu3")
    oyuncu3_el.yeni_el(7)
    print("{}, 7 kartı var".format(oyuncu3_el.playername))
    oyun_raporu += "Oyuncu3'ün eli: {}\n".format([k.name for k in oyuncu3_el.cards])
    oyun_raporu += "Deste: {}\n".format([k.name for k in deck])

    time.sleep(2)
    user_el = El(user_playername)
    user_el.yeni_el_user(7)
    print("\n\tElindeki kartlar:\n\t{}\n\n\n\n".format([k.name for k in user_el.cards]))
    time.sleep(4)
    oyun_raporu += "Kullanıcının eli: {}\n".format([k.name for k in user_el.cards])
    oyun_raporu += "Deste: {}\n".format([k.name for k in deck])

    oyun_raporu += "başlangıçta ortada: {},{},{}\n".format(orta.type,orta.value,orta.value_int)
    list1 = [oyuncu1_el,oyuncu2_el,oyuncu3_el,user_el]
    oyun_raporu += "list1: {}\n".format([k.playername for k in list1])
    random.shuffle(list1)
    oyun_raporu += "list1 karıştırıldı: {}\n".format([k.playername for k in list1])
    print("\n\toyun sırası:{}".format([k.playername for k in list1]))
    oyun_raporu += "oyun sırası: {}\n".format([k.playername for k in list1])
    time.sleep(2)


    tur_limiti = 600
    global i
    i = 0

    def duz():
        global i
        global oyun_raporu
        while i < tur_limiti:
            if orta.value == 10 and orta.ortadaki_kart.mark10 == "":
                orta.ortadaki_kart.mark10 = "marked"
                ters()
            elif orta.value == "as" and orta.ortadaki_kart.markAS == "":
                orta.ortadaki_kart.markAS = "marked"
                duz_atla()
            else:
                current = list1[0]
                print("Sırada: {}".format(current.playername))
                oyun_raporu += "Sırada: {}\n".format(current.playername)
                del list1[0]
                list1.append(current)

                if current.playertype == "user":
                    Tur_user(current)
                    time.sleep(1)
                    check_singlewin_user(current)

                else:
                    Tur(current)
                    time.sleep(2)
                    check_singlewin(current)

                print("orta:",orta.type,orta.value)
                oyun_raporu += "orta:{},{}\n".format(orta.type,orta.value)
                if orta.value == 10 and orta.ortadaki_kart.mark10 == "":
                    var_for_change_list = list1[-1]
                    del list1[-1]
                    list1.insert(0,var_for_change_list)
                print("oyun sırası: {}".format([k.playername for k in list1]))
                oyun_raporu += "oyun sırası: {}\n".format([k.playername for k in list1])
                i +=1
                oyun_raporu += "i(tur sayısı)={}\n".format(i)

    def ters():
        global i
        global oyun_raporu
        while i < tur_limiti:
            if orta.value == 10 and orta.ortadaki_kart.mark10 == "":
                orta.ortadaki_kart.mark10 = "marked"
                duz()
            elif orta.value == "as" and orta.ortadaki_kart.markAS == "":
                orta.ortadaki_kart.markAS = "marked"
                ters_atla()
            else:
                current = list1[-1]
                print("Sırada: {}".format(current.playername))
                oyun_raporu += "Sırada: {}\n".format(current.playername)
                del list1[-1]
                list1.insert(0,current)

                if current.playertype == "user":
                    Tur_user(current)
                    time.sleep(1)
                    check_singlewin_user(current)

                else:
                    Tur(current)
                    time.sleep(2)
                    check_singlewin(current)

                print("orta:",orta.type,orta.value)
                oyun_raporu += "orta:{},{}\n".format(orta.type,orta.value)
                if orta.value == 10 and orta.ortadaki_kart.mark10 == "":
                    var_for_change_list = list1[0]
                    del list1[0]
                    list1.append(var_for_change_list)
                print("oyun sırası(tersten): {}".format([k.playername for k in list1]))
                oyun_raporu += "oyun sırası(tersten): {}\n".format([k.playername for k in list1])
                i +=1
                oyun_raporu += "i(tur sayısı)={}\n".format(i)

    def duz_atla():
        global i
        global oyun_raporu
        current = list1[0]
        print("Sırada: {}".format(current.playername))
        oyun_raporu += "Sırada: {}\n".format(current.playername)
        del list1[0]
        list1.append(current)
        print("{} atlandı".format(current.playername))
        oyun_raporu += "{} atlandı\n".format(current.playername)
        print("orta:",orta.type,orta.value)
        oyun_raporu += "orta:{},{}\n".format(orta.type,orta.value)
        print("oyun sırası: {}".format([k.playername for k in list1]))
        oyun_raporu += "oyun sırası: {}\n".format([k.playername for k in list1])
        i +=1
        oyun_raporu += "i(tur sayısı)={}\n".format(i)

    def ters_atla():
        global i
        global oyun_raporu
        current = list1[-1]
        print("Sırada: {}".format(current.playername))
        oyun_raporu += "Sırada: {}\n".format(current.playername)
        del list1[-1]
        list1.insert(0,current)
        print("{} atlandı".format(current.playername))
        oyun_raporu += "{} atlandı\n".format(current.playername)
        print("orta:",orta.type,orta.value)
        oyun_raporu += "orta:{},{}\n".format(orta.type,orta.value)
        print("oyun sırası(tersten): {}".format([k.playername for k in list1]))
        oyun_raporu += "oyun sırası(tersten): {}\n".format([k.playername for k in list1])
        i +=1
        oyun_raporu += "i(tur sayısı)={}\n".format(i)


    def check_singlewin(current_player_el):
        global i
        global oyun_raporu
        if len(current_player_el.cards) == 0:
            time.sleep(1)
            print("\n\n\tÜzgünüm,\n\t{} kazandı!\n\tonun elindeki kartlar: {}\n".format(current_player_el.playername,current_player_el.cards))
            oyun_raporu += "\n\n\tÜzgünüm,\n\t{} kazandı!\n\tonun elindeki kartlar: {}\n".format(current_player_el.playername,current_player_el.cards)
            list1.remove(current_player_el)
            endplayer1,endplayer2,endplayer3 = list1[0],list1[1],list1[2]
            time.sleep(2)
            print("Son durum:\n{}: {}\n{}: {}\n{}: {}\n".format(endplayer1.playername,[k.name for k in endplayer1.cards],endplayer2.playername,[k.name for k in endplayer2.cards],endplayer3.playername,[k.name for k in endplayer3.cards]))
            time.sleep(3)
            oyun_raporu += "Son durum:\n{}: {}\n{}: {}\n{}: {}\n".format(endplayer1.playername,[k.name for k in endplayer1.cards],endplayer2.playername,[k.name for k in endplayer2.cards],endplayer3.playername,[k.name for k in endplayer3.cards])
            oyun_raporu += "bu oyun {} tur sürdü".format(i)
            i = tur_limiti
            cevap_win = input("\n\tÇıkmak için 'enter'a tıklayın\n")


    def check_singlewin_user(current_player_el):
        global i
        global oyun_raporu
        if len(current_player_el.cards) == 0:
            time.sleep(1)
            print("\n\n\tTebrikler!\n\tBu oyunu sen kazandın!\n\telindeki kartlar: {}\n".format(current_player_el.cards))
            oyun_raporu += "\n\n\tTebrikler!\n\tBu oyunu sen kazandın!\n\telindeki kartlar: {}\n".format(current_player_el.cards)
            time.sleep(2)
            print("Son durum:\n{}: {}\n{}: {}\n{}: {}\n".format(oyuncu1_el.playername,[k.name for k in oyuncu1_el.cards],oyuncu2_el.playername,[k.name for k in oyuncu2_el.cards],oyuncu3_el.playername,[k.name for k in oyuncu3_el.cards]))
            time.sleep(3)
            oyun_raporu += "Son durum:\n{}: {}\n{}: {}\n{}: {}\n".format(oyuncu1_el.playername,[k.name for k in oyuncu1_el.cards],oyuncu2_el.playername,[k.name for k in oyuncu2_el.cards],oyuncu3_el.playername,[k.name for k in oyuncu3_el.cards])
            oyun_raporu += "bu oyun {} tur sürdü".format(i)
            i = tur_limiti
            cevap_win = input("\n\tÇıkmak için 'enter'a tıklayın\n")


    listabc = [k.playername for k in list1]

    duz()
    
    dosya.writelines(oyun_raporu)
    dosya.close()


oyunabasla()