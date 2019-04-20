import cardgame1 as cg 
import random

# class Orta:
#     def __init__(self, card_instance):
#         self.type = card_instance.type
#         self.value = card_instance.value
#         self.value_int = card_instance.value_int

# print(cg.all_cards[25].type)
# print(cg.all_cards[25].value)
# print(cg.all_cards[25].value_int)
# print(cg.all_cards[25].name)

# orta1 = Orta(cg.all_cards[25])

# print(orta1.type)
# print(orta1.value)
# print(orta1.value_int)


def create_deck():
        sayi_listesi = list(range(52))
        # print(sayi_listesi)
        random.shuffle(sayi_listesi)
        # print(sayi_listesi)
        deck = []
        for i in sayi_listesi:
            deck.append(cg.all_cards[i]) 
        # print(deck)
        # print([a.type for a in deck])
        # print([a.value for a in deck])
        # print([a.value_int for a in deck])
        # print([a.name for a in deck])
        return deck
        

def shuffle_deck():
    random.shuffle(deck)
    # print([a.type for a in deck])
    # print([a.value for a in deck])
    # print([a.value_int for a in deck])
    return deck



deck = create_deck()
deck = shuffle_deck()
print(type(deck))
print([a.name for a in deck])


class El:
    def __init__(self):
        self.player = ""
        self.cards = []

    def yeni_el(self,a):
        self.cards = [deck.pop(0) for i in range(a)]



ali_el = El()
ali_el.yeni_el(0)
print(ali_el.cards)
print([a.name for a in ali_el.cards])
print([a.name for a in deck])
print(len(ali_el.cards),len(deck))

veli_el = El()
veli_el.yeni_el(1)
print(veli_el.cards)
print([a.name for a in veli_el.cards])
print([a.name for a in deck])
print(len(ali_el.cards),len(veli_el.cards),len(deck))


class Tur:
    def __init__(self,oyuncu_el):
        self.oyuncu = oyuncu
        
    
    def kart_cek(self,a):
        cards_to_be_drawn = [deck.pop(0) for i in range(a)]
        self.oyuncu.cards.extend(cards_to_be_drawn)
        # cards_to_be_drawn = []

    def kart_oyna(self,card_instance):
        orta = Orta(card_instance)
        self.oyuncu.cards.remove(card_instance)





def oyuna_basla(oyuncu_sayisi):
    # oyuncu_listesi = [a for i in range(oyuncu_sayisi)]
    orta = Orta.baslangic()
    deck = create_deck()
    oyuncu1_el = El()
    oyuncu1_el.yeni_el(7)
    oyuncu2_el = El()
    oyuncu2_el.yeni_el(7)
    oyuncu3_el = El()
    oyuncu3_el.yeni_el(7)
    oyuncu4_el = El()
    oyuncu4_el.yeni_el(7)

 








