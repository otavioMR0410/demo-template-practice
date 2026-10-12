def moyenne(valeurs):
    if not valeurs:
        raise ValueError("This list cannot be empty")


    return sum(valeurs) / len(valeurs)


if __name__ == "__main__":
    print(moyenne([10, 20, 30]))
