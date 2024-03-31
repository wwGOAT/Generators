import random


def tasodifiy_juft_sonlar(miqdor):
    """Berilgan miqdorda tasodifiy juft sonlar ro'yxatini qaytaradi."""
    juft_sonlar = []
    while len(juft_sonlar) < miqdor:
        son = random.randint(1, 100)
        if son % 2 == 0:
            juft_sonlar.append(son)
    return juft_sonlar


def main():
    miqdor = int(input("Qancha tasodifiy juft son chiqarishni istaysiz? -> "))
    juft_sonlar = tasodifiy_juft_sonlar(miqdor)
    print(f"Tasodifiy juft sonlar: {juft_sonlar}")


if __name__ == "__main__":
    main()
