#                  1-masala
class Kitob:
        
    def kiritish(self):
        self.nomi = input("Kitob nomi: ")
        self.muallifi = input("Muallifi: ")
        self.narxi = int(input("Narxi: "))
        self.nashriyoti = input("Nashriyoti: ")
        
    def chiqarish(self):
        print(self.nomi, self.muallifi, self.narxi, self.nashriyoti)