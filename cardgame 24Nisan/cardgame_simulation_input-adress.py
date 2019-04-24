import random
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
class El:
    def __init__(self,player):
        self.playername = str(player)
        self.cards = []

    def yeni_el(self,a):
        self.cards = [deck.pop(0) for i in range(a)]



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
        print("olası hamleler:",[h.name for h in self.hamleler])
        

########## kart_cek'te, tek deste oynandığı için "if len(deck) < 8: ifadesi" var. 
##########Eğer çift deste oynanırsa, burayı 16 yap! (çünkü bir anda çekilebilecek max. kart sayısı 16 olur(8tane7))
    def kart_cek(self,a):
        global deck
        
        try:
            global orta
            print("\ndeste uzunluğu, kart çekemeden önce: {}".format(len(deck)))
            cards_to_be_drawn = [deck.pop(0) for i in range(a)]
            self.oyuncu.cards.extend(cards_to_be_drawn)
            print("{} {} kart çekti".format(self.oyuncu.playername,a))
            print("deste uzunluğu, kart çektiktikten sonra: {}\n".format(len(deck)))
            print("{}'in yeni eli:".format(self.oyuncu.playername),[k.name for k in self.oyuncu.cards])
            if len(deck) < 8:
                print("\ndestedeki kart sayısı:",len(deck))
                print("ortadaki kart sayısı:",len(orta.ortada))
                temporary_deck1 = orta.ortada[1:-1]
                temporary_deck1 = shuffle_deck(temporary_deck1)
                deck.extend(temporary_deck1)
                Orta.ortada = [orta.ortada[0],orta.ortada[-1]]
                for card in deck:
                    card.mark10 = ""
                    card.markAS = ""
                    card.mark7 = 2
                print("ortadaki kağıtlar karılıp yeni deste yapıldı")
                print("destedeki kart sayısı::",len(deck))
                print([k.name for k in deck])
                print("ortada kalanlar: {}\n".format(len(orta.ortada),[k.name for k in orta.ortada]))
        except Exception as hata :
            print("\n\n\t\tKART ÇEK HATA VERDİ,\t adım: {},\n deste uzunluğu: {},\n ortanın uzunluğu: {},\n destedeki kartlar: {}\n\n".format(i,len(deck),len(orta.ortada),[k.name for k in deck]))
            print(hata)

    def kart_oyna(self,card_instance):
        if card_instance.value == "vale":
            global secim
            secim = random.choice(list_types)
        global orta
        orta = Orta(card_instance)
        self.oyuncu.cards.remove(card_instance)
        print("{} {} oynadı".format(self.oyuncu.playername,card_instance.name))
        print("\nortadaki kart sayısı:",len(orta.ortada))
        if card_instance.value == "vale":
            print("valeden dolayı değişen orta: {}".format(secim))




def oyunabasla(yol):
    try:
        dosya = open(yol,"w+")
        sys.stdout = dosya
    except Exception as hata:
        print("\n\tBir Sorun Var!!!\nSimulasyon sonucunu kaydederken hata olustu\nLutfen klasor adresini ve belge adini kontrol edin")
        print(hata)

    global orta
    orta = Orta.baslangic()
    global deck
    deck = create_deck()
    print("oyundaki kart sayısı: {}".format(len(Iskambil.tanimli)))

    print([k.name for k in deck],"\n")
    oyuncu1_el = El("oyuncu1")
    oyuncu1_el.yeni_el(7)
    print("Oyuncu1'in eli:",[k.name for k in oyuncu1_el.cards])
    print([k.name for k in deck],"\n")
    oyuncu2_el = El("oyuncu2")
    oyuncu2_el.yeni_el(7)
    print("Oyuncu2'nin eli:",[k.name for k in oyuncu2_el.cards])
    print([k.name for k in deck],"\n")
    oyuncu3_el = El("oyuncu3")
    oyuncu3_el.yeni_el(7)
    print("Oyuncu3'ün eli:",[k.name for k in oyuncu3_el.cards])
    print([k.name for k in deck],"\n")
    oyuncu4_el = El("oyuncu4")
    oyuncu4_el.yeni_el(7)
    print("Oyuncu4'ün eli:",[k.name for k in oyuncu4_el.cards])
    print([k.name for k in deck],"\n")

    print("başlangıçta ortada:",orta.type,orta.value,orta.value_int,"\n")

    list1 = [oyuncu1_el,oyuncu2_el,oyuncu3_el,oyuncu4_el]
    print("oyun sırası:{}".format([k.playername for k in list1]))


    tur_limiti = 600
    global i
    i = 0

    def duz():
        global i
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
                del list1[0]
                list1.append(current)
                Tur(current)
                check_singlewin(current)
                print("orta:",orta.type,orta.value)
                if orta.value == 10 and orta.ortadaki_kart.mark10 == "":
                    var_for_change_list = list1[-1]
                    del list1[-1]
                    list1.insert(0,var_for_change_list)
                print("oyun sırası: {}".format([k.playername for k in list1]))
                i +=1
                print("i={}".format(i))

    def ters():
        global i
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
                del list1[-1]
                list1.insert(0,current)
                Tur(current)
                check_singlewin(current)
                print("orta:",orta.type,orta.value)
                if orta.value == 10 and orta.ortadaki_kart.mark10 == "":
                    var_for_change_list = list1[0]
                    del list1[0]
                    list1.append(var_for_change_list)
                print("oyun sırası(tersten): {}".format([k.playername for k in list1]))
                i +=1
                print("i={}".format(i))

    def duz_atla():
        global i
        current = list1[0]
        print("Sırada: {}".format(current.playername))
        del list1[0]
        list1.append(current)
        print("{} atlandı".format(current.playername))
        print("orta:",orta.type,orta.value)
        print("oyun sırası: {}".format([k.playername for k in list1]))
        i +=1
        print("i={}".format(i))


    def ters_atla():
        global i
        current = list1[-1]
        print("Sırada: {}".format(current.playername))
        del list1[-1]
        list1.insert(0,current)
        print("{} atlandı".format(current.playername))
        print("orta:",orta.type,orta.value)
        print("oyun sırası(tersten): {}".format([k.playername for k in list1]))
        i +=1
        print("i={}".format(i))

    def check_singlewin(current_player_el):
        global i
        if len(current_player_el.cards) == 0:
            print("\n\tTebrikler!\n\t{} kazandı!\n\telindeki kartlar: {}\n\n\n\n".format(current_player_el.playername,current_player_el.cards))
            i = tur_limiti
            




    listabc = [k.playername for k in list1]

    duz()
    dosya.close()

s_klasor_adres = str(input("Pis Yedili simulasyonunun kaydedileceği klasörün adresini yazınız\n"))
s_belge_ad = str(input("\nPis Yedili simulasyonu ne adla kaydedilsin?\n"))
dosyayolu = "{}\{}.txt".format(s_klasor_adres,s_belge_ad)


oyunabasla(dosyayolu)