import random

def tasodifiy_elementlar_royxati(tur, miqdor):
    """Berilgan tur va miqdorda tasodifiy elementlar ro'yxatini qaytaradi."""
    if tur == "butun":
        return [random.randint(1, 100) for _ in range(miqdor)]
    elif tur == "haqiqiy":
        return [random.random() for _ in range(miqdor)]
    elif tur == "matn":
        alfavit = "abcdefghijklmnopqrstuvwxyz"
        return [''.join(random.choices(alfavit, k=random.randint(5, 10))) for _ in range(miqdor)]
    else:
        raise ValueError("Noto'g'ri tur")

def main():
    print("Turini tanlang:")
    print("1. Butun sonlar")
    print("2. Haqiqiy sonlar")
    print("3. Matnlar")
    tur = input("Tanlov: ")

    if tur in ("1", "2", "3"):
        miqdor = int(input("Miqdorni kiriting: "))
        royxat = tasodifiy_elementlar_royxati("butun" if tur == "1" else "haqiqiy" if tur == "2" else "matn", miqdor)
        print("Natija:", royxat)
    else:
        print("Noto'g'ri tanlov")

if __name__ == "__main__":
    main()
