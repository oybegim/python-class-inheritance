class Talaba:
    def __init__(self, ism, familiya, otchestva, yosh,):
        self.ism = ism
        self.familiya = familiya
        self.otchestva = otchestva
        self.yosh = yosh

print("Talabalar")

t1 = Talaba("Durbek", "Xoliqov", "Javohir o'g'li", 18)
t2 = Talaba("Dilshoda", "Amrullayeva", "Sanjar qizi", 19)

print(t1.ism, t1.familiya, t1.otchestva, t1.yosh)
print(t2.ism, t2.familiya, t2.otchestva, t2.yosh)


class Abituriyent:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        
print("Abituriyentlar")

a1 = Abituriyent("Mehrangiz", "Salimova", 18)
a2 = Abituriyent("Xusniddin", "Sanjarov", 19)

print(a1.ism, a1.familiya, a1.yosh)
print(a2.ism, a2.familiya, a2.yosh)