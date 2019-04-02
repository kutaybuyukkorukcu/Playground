# 4, 4, 9, 2, 3 = 10

def calculateAmount(prices):
  number = prices.pop(0)
  sum = prices.pop(0)
  listem = [sum] 
  for i in range(number - 1):
    for az in range(i):
      listem.append(prices[az])
    val = prices[i] - min(listem)
    print(listem)
    if (val < 0):
      val = 0
    sum = sum + val
  print(sum)

calculateAmount([4,1,2,3,4])