from itertools import combinations


wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
amount = 100

def main():
    combs_list = []
    for index in range(0, len(wallet)):
        comb = combinations(wallet, len(wallet) - index)
        comb = set(comb)
        combs_list.append(comb)

    combos = []
    [combos.append(comb) for item in combs_list for comb in item if sum(comb) == amount]
    for comb in combos: print(comb)
    print(len(combos))


if __name__ == "__main__":
    main()