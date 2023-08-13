f = open("26.5.txt")
n = int(f.readline())
prices = [int(f.readline()) for i in range(n)]
prices.sort(reverse=True)
print(sum(prices) - sum(prices[:2500]) * 0.5)
print(sum(prices) - sum(prices[7500:]) * 0.5)
# 3842495.0
# 4780982.0
# изи ЕГЭ 2022 2 день - найти сумму которую заплатили со стороны покупателя и магазина
