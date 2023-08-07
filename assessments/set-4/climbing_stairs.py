# Climbing Stairs: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def func(x):
  return 1 if x==0 else (0 if x<0 else func(x-1)+func(x-2))

print(func(3))
