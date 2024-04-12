liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
MaxBalance = 0
nowArray = ["tokenB"]
ansArray = []

def getAmountOut(x, y, dx):
  return 997*dx*y/(1000*x+997*dx)

def recursion(nowToken, balance, t):
    global MaxBalance

    if nowToken == "tokenB" and balance > 22:
        MaxBalance = balance
        global ansArray
        ansArray = []
        for i in nowArray:
            ansArray.append(i)
        return True

    if t==6 : return False
    for token in tokens:
        if token == nowToken: continue
        X, Y = nowToken, token
        if(X[5] > Y[5]): y, x = liquidity[(Y, X)]
        else: x, y = liquidity[(X, Y)]
        dx = balance
        dy = getAmountOut(x, y, dx)
        if dy > 0: 
            nowArray.append(token)
            if(X[5] > Y[5]): liquidity[(Y, X)] = (y-dy, x+997*dx/1000)
            else: liquidity[(X, Y)] = (x+997*dx/1000, y-dy)
            if recursion(token, dy, t+1): return True
            if(X[5] > Y[5]): liquidity[(Y, X)] = (y, x)
            else: liquidity[(X, Y)] = (x, y)
            nowArray.pop()
    return False

def output():
    print("path: ", end="")
    for i in range(len(ansArray)):
        if i>0: print("->", end="")
        print(ansArray[i], end="")
    print(", tokenB balance=", end="")
    print(MaxBalance)

recursion("tokenB", 5, 0)
output()