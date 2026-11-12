#                  1-masala
# class Kitob:
        
#     def kiritish(self):
#         self.nomi = input("Kitob nomi: ")
#         self.muallifi = input("Muallifi: ")
#         self.narxi = int(input("Narxi: "))
#         self.nashriyoti = input("Nashriyoti: ")
        
#     def chiqarish(self):
#         print(self.nomi, self.muallifi, self.narxi, self.nashriyoti)

# kitoblar = []

# for i in range(5):
#     k = Kitob()
#     k.kiritish()
#     kitoblar.append(k)
    
# for i in kitoblar:
#     bosh_harf = i.nashriyoti[0].upper()
#     if "A"<= bosh_harf <= "H":
#         i.chiqarish()

#                    2-masala
# class Kompyuter:
        
#     def kiritish(self):
#         self.nomi = input("Kampyuter nomi: ")
#         self.rami = input("RAMI: ")
#         self.narxi = int(input("Narxi: "))
#         self.protsesor = input("Protsessori: ")
        
#     def chiqarish(self):
#         print(self.nomi, self.rami, self.narxi, self.protsesor)
        

# kampyuter = []

# for i in range(4):
#     k = Kompyuter()
#     k.kiritish()
#     kampyuter.append(k)
    
# for i in kampyuter:
#     if int(i.rami) >= 4 and int(i.rami) <= 16:
#         i.chiqarish()