import random

########## İskambil Oyunu için Kod
########## Hazırlayan: Görkem Seçkin
########## Başlangıç Tarihi: 15 Nisan 2019
########## Son Düzenleme Tarihi: 18 Nisan 2019

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
def shuffle_deck():
    random.shuffle(deck)
    return deck

########## Bir oyuncunun eli. yeni_el, verilen sayıda kağıdı desteden çekip self.cards listesine ekliyor.
class El:
    def __init__(self):
        self.player = ""
        self.cards = []

    def yeni_el(self,a):
        self.cards = [deck.pop(0) for i in range(a)]



class Tur:
    def __init__(self,oyuncu_el):
        self.oyuncu = oyuncu_el
        # self.oynanana_bak()
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
        print("olası hamleler:",[h.name for h in self.hamleler])
    
    # def oynanana_bak(self):
    #     if orta.value_int == 7:
    #         for card in self.oyuncu.cards:
    #             if card.value == 7:
    #                 self.kart_oyna(card)
    #                 break
    #         self.kart_cek(2)
        
        
    def kart_cek(self,a):
        cards_to_be_drawn = [deck.pop(0) for i in range(a)]
        self.oyuncu.cards.extend(cards_to_be_drawn)
        # cards_to_be_drawn = []
        print("{} {} kart çekti".format(self.oyuncu,a))
        print("{}'in yeni eli:".format(self.oyuncu),[k.name for k in self.oyuncu.cards])

    def kart_oyna(self,card_instance):
        if card_instance.value == "vale":
            global secim
            secim = random.choice(list_types)
        global orta
        orta = Orta(card_instance)
        self.oyuncu.cards.remove(card_instance)
        print("{} {} oynadı".format(self.oyuncu,card_instance.name))
        if card_instance.value == "vale":
            print("valeden dolayı değişen orta: {}".format(secim))










def oyuna_basla():
    # oyuncu_listesi = [a for i in range(oyuncu_sayisi)]
    global orta
    orta = Orta.baslangic()
    global deck
    deck = create_deck()

    print([k.name for k in deck],"\n")
    oyuncu1_el = El()
    oyuncu1_el.yeni_el(7)
    print("Oyuncu1'in eli:",[k.name for k in oyuncu1_el.cards])
    print([k.name for k in deck],"\n")
    oyuncu2_el = El()
    oyuncu2_el.yeni_el(7)
    print("Oyuncu2'nin eli:",[k.name for k in oyuncu2_el.cards])
    print([k.name for k in deck],"\n")
    oyuncu3_el = El()
    oyuncu3_el.yeni_el(7)
    print("Oyuncu3'ün eli:",[k.name for k in oyuncu3_el.cards])
    print([k.name for k in deck],"\n")
    oyuncu4_el = El()
    oyuncu4_el.yeni_el(7)
    print("Oyuncu4'ün eli:",[k.name for k in oyuncu4_el.cards])
    print([k.name for k in deck],"\n")

    # print(orta.ortada)
    # orta = Orta(Iskambil(1,1,1))
    # print(orta.ortada)


    print("başlangıçta ortada:",orta.type,orta.value,orta.value_int,"\n")
    # print(type(orta.type),type(orta.value),type(orta.value_int))

    t1 = Tur(oyuncu1_el)
    
    # print("hamleler",[h.name for h in t1.hamleler])
    print("orta:",orta.type,orta.value)
    # t1.kart_oyna(oyuncu1_el.cards[5])
    t2 = Tur(oyuncu2_el)
    
    # print("hamleler",[h.name for h in t2.hamleler])
    print("orta:",orta.type,orta.value)
    # t2.kart_oyna(oyuncu2_el.cards[0])
    t3 = Tur(oyuncu3_el)
    
    # print("hamleler",[h.name for h in t3.hamleler])
    print("orta:",orta.type,orta.value)
    # t3.kart_oyna(oyuncu3_el.cards[2])
    t4 = Tur(oyuncu4_el)
    
    # print("hamleler",[h.name for h in t4.hamleler])
    print("orta:",orta.type,orta.value)
    # t4.kart_oyna(oyuncu4_el.cards[6])
    
    t1 = Tur(oyuncu1_el)
    print("orta:",orta.type,orta.value)
    t2 = Tur(oyuncu2_el)
    print("orta:",orta.type,orta.value)
    t3 = Tur(oyuncu3_el)
    print("orta:",orta.type,orta.value)
    t4 = Tur(oyuncu4_el)
    
    # print("hamleler",[h.name for h in t4.hamleler])
    print("orta:",orta.type,orta.value)
    print("\nortada oynanmış kartlar:",[j.name for j in orta.ortada])
    # print(orta.type,orta.value,orta.value_int)
    print("oyuncu1:",[k.name for k in oyuncu1_el.cards],"oyuncu2:",[k.name for k in oyuncu2_el.cards],"oyuncu3:",[k.name for k in oyuncu3_el.cards],"oyuncu4:",[k.name for k in oyuncu4_el.cards],sep="\n") 
    print(len(deck))
    print([k.name for k in deck])


    return oyuncu1_el,oyuncu2_el,oyuncu3_el,oyuncu4_el




# # deck = create_deck()
# # ali = El()
# # ali.yeni_el(5)
# # ayse = El()
# # ayse.yeni_el(5)

# # print([a.name for a in deck],[a.name for a in ali.cards],[a.name for a in ayse.cards],sep="\n\naaaaaaaaaaaaaaaaa\n\n")
# # print(len(ali.cards),len(ayse.cards),len(deck))

# # a1 = Orta.baslangic()
# # print(a1.type,a1.value,a1.value_int)



# k,l,m,n = oyuna_basla()
oyuna_basla()
# print(orta.ortada)
# orta = Orta(Iskambil(1,1,1))
# print(orta.ortada)


# print(orta.type,orta.value,orta.value_int)

# t1 = Tur(l)
# t1.kart_oyna(l.cards[5])
# t1 = Tur(n)
# t1.kart_oyna(n.cards[0])
# t1 = Tur(k)
# t1.kart_oyna(k.cards[2])
# t1 = Tur(m)
# t1.kart_oyna(m.cards[6])
# print([j.name for j in orta.ortada])
# print(orta.type,orta.value,orta.value_int)
# print(len(deck)) 



