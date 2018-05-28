from time import time

def knapsack(target, weights, values, n=None):
  n = len(values) if n is None else n
  if n == 0 or target == 0:
    return 0
  
  return max(
    values[n - 1] + knapsack(target - weights[n -1], weights, values, n - 1),
    knapsack(target, weights, values, n - 1)
  )

def knapsack_dp(target, weights, values, n=None):
  n = len(values) if n is None else n
  memo = [[0 for j in range(target + 1)] for i in range(n + 1)]

  for i in range(n + 1):
    for j in range(target + 1):
      if i == 0 or j == 0:
        memo[i][j] = 0
      elif weights[i - 1] <= j:
        memo[i][j] = max(values[i - 1] + memo[i - 1][target - weights[i - 1]], memo[i - 1][j])
      else:
        memo[i][j] = memo[i - 1][j]
  
  return memo[n][target]

val = [60, 100, 120]
wt = [10, 20, 30]
weight = 50

start = time()
result = knapsack(weight, wt, val)
end = time() 
print(f'Answer - {result} in {end - start}')

start = time()
result = knapsack_dp(weight, wt, val)
end = time() 
print(f'Answer - {result} in {end - start}')
