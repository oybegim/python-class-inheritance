class Odam:
    def __init__(self, ismi, familiyasi):
        self.ismi = ismi
        self.familiyasi = familiyasi
    def __str__(self):
        return f"Ismi: {self.ismi}, Familiyasi: {self.familiyasi}"

class Talaba(Odam):
    def __init__(self, ismi, familiyasi, yoshi, vazni):
        super().__init__(ismi, familiyasi)
        self.yoshi = yoshi
        self.vazni = vazni
    def talaba1(self):
        print(self.ismi, self.familiyasi, self.yoshi, self.vazni)

print("Talaba")

t = Talaba("Ismi: Farangiz,", "Familiyasi: Salimova,", "yoshi: 18,", "vazni: 50")


print(t.talaba1())

class Abituriyent(Odam):
    def __init__(self, ismi, familiyasi, otchestvasi, yoshi, vazni):
        super().__init__(ismi, familiyasi)
        self.otchestvasi = otchestvasi
        self.yoshi = yoshi
        self.vazni = vazni
    def abituriyent1(self):
        print(self.ismi, self.familiyasi, self.otchestvasi, self.yoshi, self.vazni)

print("Abituriyent")

a = Abituriyent("Ismi: Jamol,", "Familiyasi: Kamolov,", "Otchestvasi: Javohir o'g'li,", "Yoshi: 19,", "vazni: 70")



print(a.abituriyent1())