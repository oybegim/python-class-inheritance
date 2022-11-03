class Kompyuter:
    def __init__(self, rusumi, windows, xotira):
        self.rusumi = rusumi
        self.windows = windows
        self.xotira = xotira
    def __str__(self):
        return f"Rusumi: {self.rusumi}, Windows: {self.windows}, Xotira: {self.xotira}"

print("Kompyuter")

a = Kompyuter("Acer", 10, "247GB")

print(a)



class Telefon:
    def __init__(self, rusumi, xotirasi):
        self.rusumi = rusumi
        self.xotirasi = xotirasi
    def __str__(self):
        return f"Rusumi: {self.rusumi}, Xotirasi: {self.xotirasi}"

print("Telefon")

r = Telefon("Redmi8", "64GB")

print(r)