import random


def tasodifiy_toq_sonlar(miqdor):
    """Berilgan miqdorda tasodifiy toq sonlar ro'yxatini qaytaradi."""
    toq_sonlar = []
    while len(toq_sonlar) < miqdor:
        son = random.randint(1, 100)
        if son % 2 != 0:
            toq_sonlar.append(son)
    return toq_sonlar


def main():
    miqdor = int(input("Qancha tasodifiy toq son chiqarishni istaysiz? -> "))
    toq_sonlar = tasodifiy_toq_sonlar(miqdor)
    print(f"Tasodifiy toq sonlar: {toq_sonlar}")


if __name__ == "__main__":
    main()
