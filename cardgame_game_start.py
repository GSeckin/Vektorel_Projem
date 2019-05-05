import time
import cardgame_game_tutorial as cg_tutorial
import cardgame_game_normalgame_v2 as cg_normal


def giris_karsilama2():
    karsilama_yazisi = """
    \n\t\t\tPYTHON'LA OYNAYALIM
    \n\tMerhaba,\n\tPis Yedili oyununa hoşgeldin!\n
    """
    print("_"*125)
    print(karsilama_yazisi)
    time.sleep(2)

    cevap1 = str(input("\n\tPis Yedili'nin kurallarını öğrenmek ister misin?'\n<Evet/Hayır>\n")).lower()
    if cevap1 == "evet":
        print("\n\tBu oyunda amacın: Elindeki kartları bitirmek")
        time.sleep(1)
        print("\n\tOyuna 7 kartla başlıyorsun,")
        time.sleep(1)
        print("\n\tve her tur, desteden kart çekebilir ve elinden ortaya kart atabilirsin")
        time.sleep(1)
        print("\n\tBir kartı oynayabilmen için, kartın çeşidinin veya değerinin ortadaki kartla aynı olması gerekli.")
        time.sleep(1)
        print("\n\tÖrneğin; ortada 'maça 4' varsa,")
        time.sleep(1)
        print("\n\tElinden 'maça 8' ya da 'kupa 4' oynayabilirsin, ama 'karo 6' oynayamazsın.")
        time.sleep(1)
        print("\n\tTur sana geldiğinde,")
        time.sleep(1)
        print("\n\toynayabileceğin bir kartın yoksa, desteden bir kart çek.")
        time.sleep(1)
        print("\n\tEğer yeni çektiğin kart uygunsa, oynayabilirsin,")
        time.sleep(1)
        print("\n\to da ugun değilse, turun biter.")
        time.sleep(1)
        print("\n\tÖzel kartlar:")
        time.sleep(1)
        print("\n\t10'lu oynandığında, oyun sırası tersine döner")
        time.sleep(1)
        print("\n\tas oynandığında, sıradaki kişinin turu atlanır ")
        time.sleep(1)
        print("\n\tvale, ortada ne olursa olsun oynanabilir ve oyuncu ortadanın çeşidini belirler (maça/sinek/karo/kupa)")
        time.sleep(1)
        print("\n\tve 7'li oynandığında, sıradaki kişi turuna 2 kart çekerek başlar")
        time.sleep(1)
        print("\n\tama, sıradaki kişinin de elinde 7'lisi varsa, kart çekmeden onu oynayabilir")
        time.sleep(1)
        print("\n\tve bir sonraki oyuncu 4 kart çeker, veya bu, katlanarak devam edebilir.")
        time.sleep(1)
        print("\n\tAyrıca, ilk tur sadece sinek oynayabilirsin ve sinek de olsa, özel kartları oynayamazsın.")
        time.sleep(1)
        print("\n\tArtık oynamaya hazırsın!")
        time.sleep(1)
    else:
        print("\n\tPeki")
        time.sleep(1)

    k1 = 0
    while k1 < 1:
        cevap2 = str(input("\n\tNormal oyuna başlamak istersin yoksa tutorial'a mı?\n\t <normal oyun/tutorial>\n"))
        if cevap2 == "tutorial":
            k1 = 1
            cg_tutorial.oyunabasla()

        elif cevap2 == "normal oyun":
            k1 = 1
            cg_normal.oyunabasla()
        
        else:
            print("\n\tGeçerli bir cevap vermedin")
            time.sleep(1)
            print("\n\tBir daha dene")
            time.sleep(1)
 

giris_karsilama2()