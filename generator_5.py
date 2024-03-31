def three_divisible_number(data):
    """Berilgan ro'yxatdan 3 ga bo'linadigan sonlarni topadi."""
    natija = [son for son in data if son % 3 == 0]
    return natija


def main():
    data = [2, 5, 9, 12, 15, 18, 21, 25, 30, 33, 36]  # Beringan ro'yxat
    three_divisible = three_divisible_number(data)
    print("Uchga bo'linadigan sonlar:", three_divisible)


if __name__ == "__main__":
    main()
