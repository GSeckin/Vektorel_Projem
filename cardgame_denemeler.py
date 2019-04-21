# liste = ["a","b","c","d"]
# class Canta:
#     def __init__(self):
#         self.renk = ""

# for oyuncu in liste:
#     oyuncu = Canta()

# print("a".renk)



# class Aclass:
#     a = "a"
#     def __init__(self):
#         self.b = "b"
    
#     def Bfunction(self):
#         self.c = "m"
#         if self.c == masa:
#             print("yes")
#         else:
#             print("no")

# def Dfunction():
#     global masa 
#     masa = "m"

# Dfunction()
# instance1 = Aclass()
# instance1.Bfunction()
###################################################################################

# list1 = ["a","b","c","d","e"]

# i = 0
# while i < 2:
#     for a in list1:
#         print(a)
#     i += 1

###################################################################################

# list1 = ["a","b","c","d","e"]

# i = 0
# while i < 2:
#     for a in reversed(list1):
#         print(a)
#     i += 1

###################################################################################

# list1 = ["a","b","c","d","e"]

# i = 0
# alert1 = 0
# while i < 4:
#     for a in list1:
#         if a == "d":
#             alert1 = 1
#         if alert1 == 0:
#             print(a)
#         alert1 = 0
#     i += 1

###################################################################################


# list1 = ["a","b","c","d","e","f"]

# i = 0

# def duz():
#     global i
#     while i < 40:
#         for a in list1:
#             if a == "d":
#                 i += 1
#                 ters()
#             print(a)
#             i += 1

# def ters():
#     global i
#     while i < 40:
#         for a in reversed(list1):
#             if a == "d":
#                 i += 1
#                 duz()
#             print(a)
#             i +=1

# duz()

###################################################################################
#this works this works this works this works this works this works

# list1 = ["a","b","c","d"]
# i = 0

# def duz():
#     global i
#     while i < 10:
#         current = list1[0]
#         print(current)
#         del list1[0]
#         list1.append(current)
#         print(list1)
#         i +=1

# def ters():
#     global i
#     while i < 10:
#         current = list1[-1]
#         print(current)
#         del(list1[-1])
#         list1.insert(0,current)
#         print(list1)
#         i +=1

# duz()
# print("\n\n")
# i = 0
# ters()
###################################################################################
list1 = ["a","b","c","d"]
i = 0

def duz():
    global i
    while i < 14:
        current = list1[0]
        if current == "d":
            i +=1
            ters()

        print(current)
        del list1[0]
        list1.append(current)
        print(list1)
        i +=1

def ters():
    global i
    while i < 14:
        current = list1[-1]
        if current == "d":
            i+=1
            duz()

        print(current)
        del(list1[-1])
        list1.insert(0,current)
        print(list1)
        i +=1

duz()



###################################################################################