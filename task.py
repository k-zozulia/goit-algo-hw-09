coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            num_of_coins = amount // coin
            result[coin] = num_of_coins
            amount -= num_of_coins * coin
    return result

def find_min_coins(amount):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    result = {}
    while amount > 0:
        for coin in coins:
            if amount >= coin and min_coins[amount] == min_coins[amount - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break
    return result

if __name__ == "__main__":
    amount = 113

    greedy_result = find_coins_greedy(amount)
    print("Жадібний алгоритм результат:", greedy_result)

    dp_result = find_min_coins(amount)
    print("Алгоритм динамічного програмування результат:", dp_result)