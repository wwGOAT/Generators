import random


def generator():
    ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim", "Soli", "Bahrom", "Farruh", "Davron", "Javohir"]
    familiyalar = ["Nazarov", "Qodirov", "Rahmonov", "Usmonov", "Sultonov", "Salimov", "Xakimov", "Tursunov", "Saidov",
                   "Yunusov"]

    ism = random.choice(ismlar)
    familiya = random.choice(familiyalar)

    return ism + " " + familiya


if __name__ == "__main__":
    print("Tug'ilgan kundagi ism-familiya kombinatsiyalari:")
    for _ in range(10):
        print(generator())
