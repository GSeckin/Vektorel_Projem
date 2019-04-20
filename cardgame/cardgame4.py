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
        
    
    def kart_cek(self,a):
        cards_to_be_drawn = [deck.pop(0) for i in range(a)]
        self.oyuncu.cards.extend(cards_to_be_drawn)
        # cards_to_be_drawn = []

    def kart_oyna(self,card_instance):
        global orta
        orta = Orta(card_instance)
        self.oyuncu.cards.remove(card_instance)



def oyuna_basla():
    # oyuncu_listesi = [a for i in range(oyuncu_sayisi)]
    global orta
    orta = Orta.baslangic()
    global deck
    deck = create_deck()
    oyuncu1_el = El()
    oyuncu1_el.yeni_el(7)
    oyuncu2_el = El()
    oyuncu2_el.yeni_el(7)
    oyuncu3_el = El()
    oyuncu3_el.yeni_el(7)
    oyuncu4_el = El()
    oyuncu4_el.yeni_el(7)
    return oyuncu1_el,oyuncu2_el,oyuncu3_el,oyuncu4_el
