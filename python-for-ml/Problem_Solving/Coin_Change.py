def coinChange(coins, amount):
    coins_arry = [float('inf')] * (amount + 1)
    coins_arry[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            coins_arry[i] = min(coins_arry[i], coins_arry[i - coin] + 1)
    
    return coins_arry[amount] if coins_arry[amount] != float('inf') else -1

input_array = input("Enter the coins array: ")
coins = list(map(int, input_array.split(',')))
amount = int(input("Enter the amount: "))
result = coinChange(coins, amount)
print("The minimum number of coins needed is:", result)