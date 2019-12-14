def mean(vector):
    return sum(vector)/len(vector)

def sum(items):
    sum = 0
    for x in items:
        sum+= x
    return sum

def product(x,y):
    for i in range(0,len(x)):
        x[i]*=y[i]
    return x    

def get_coefs(x,y):
    n = len(x)
    mx = mean(x)
    my = mean(y)
    yx = product(y,x)
    xx = product(x,x)
    SS_xy = sum(yx) - n*mx*my
    SS_xx = sum(xx) -n*mx*mx

    b1 = SS_xy/SS_xx
    b0 = my - b1*mx

    return b0, b1

def predict(b0,b1,x):
    return b0 + b1*x

x = [1,2,3]
y = [2,4,6]

b0, b1 = get_coefs(x,y)
print(predict(b0,b1,2.5))