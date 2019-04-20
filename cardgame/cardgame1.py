
########## İskambil Oyunu için Kod
########## Hazırlayan: Görkem Seçkin
########## Tarih: 15 Nisan 2019

########## list_types ve list_card_values, Iskambil class'ının instance attribute'una verilmek için
list_types = ["kupa","karo","maça","sinek"]
list_card_values = ["as",2,3,4,5,6,7,8,9,10,"vale","kız","papaz"]

########## Bir destedeki bütün kağıtlar Iskambil class'ının instance'ı olarak tanımlanır. 
class Iskambil:
    tanimli = []
    def __init__(self,cardType,cardValue,cardValue_int):
        self.type = cardType
        self.value = cardValue
        self.value_int = cardValue_int
        self.name = "{}_{}".format(self.type,self.value)
        self.tanimli.append(self.name)

########## list_abcd ve dict_for_creating sadece instance yaratmak için tek sefer kullanılıyor.
########## list_13 hem instance yaratmak hem de Iskambil class'ının instance attribute'una verilmek için var
list_abcd = ["A","B","C","D"]
list_13 = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
dict_for_creating = {}

for a in range(0,13):
    for b in range(0,4):
        dict_for_creating.update({(list_abcd[b] + list_13[a]) : [list_types[b],list_card_values[a],list_13[a]] })
# print(dict_for_creating)

########## all_cards (52 iskambil kağıdı instance'larını içeren bir liste) oluşturuluyor.
all_cards = []
for a in dict_for_creating:
    all_cards.append(Iskambil(dict_for_creating[a][0],dict_for_creating[a][1],int(dict_for_creating[a][2])))
#     print(all_cards)

# print(Iskambil.tanimli)

########## dict_lookup (bütün iskambil kağıtlarının all_cards'daki index numarasını bize gösteren bir dictionary. İleride kullanım amaçlı.
dict_lookup = {}
i = 0
for a in Iskambil.tanimli:
    dict_lookup.update({ a : i })
    i +=1


print(dict_lookup)

# print(all_cards[0].type)
# print(all_cards[49].type)
# print(all_cards[40].value)
# print(all_cards[23].value)
# print(all_cards[5].name)
# print(all_cards[33].name)
# print(all_cards[16].type)
# print(all_cards[17].type)

# print(all_cards[0].value_int)
# print(all_cards[2].value_int)
# print(all_cards[4].value_int)
# print(all_cards[15].value_int)
# print(all_cards[16].value_int)
# print(all_cards[22].value_int)
# print(all_cards[50].value_int)
# print(all_cards[41].value_int)

# print(all_cards[dict_lookup["maça_kız"]].name)
# print(all_cards[dict_lookup["sinek_5"]].name)
# print(all_cards[dict_lookup["karo_as"]].name)

# print([a.type for a in all_cards])
# print([a.value for a in all_cards])
# print([a.value_int for a in all_cards])



class Orta:
    def __init__(self, card_instance):
        self.type = card_instance.type
        self.value = card_instance.value
        self.value_int = card_instance.value_int

print(all_cards[25].type)
print(all_cards[25].value)
print(all_cards[25].value_int)
print(all_cards[25].name)

orta1 = Orta(all_cards[25])

print(orta1.type)
print(orta1.value)
print(orta1.value_int)

 