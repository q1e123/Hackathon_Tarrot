import linear_regression as lr
import utils

utils.dataset_join()

data_file = open("dataset","r")

data_lines = data_file.readlines()

# f(x) = y , x = data y = {temp, umid, vant}

def get_x(date):
    date = date.split('T')
    x = 0
    x += utils.stoi(date[0],'-')
    x += utils.stoi(date[1],':')
    return x

x = []
y0 = []
y1 = []
y2 = []

for line in data_lines:
    date, temp, hum, wind = line.split(';')
    x.append(get_x(date))
    
    if temp is "" or temp is " ":
        temp = y0[-1]
    y0.append(float(temp))
    if hum is "" or hum is " ":
        hum = y1[-1]
    y1.append(float(hum))

    wind = wind.split('\n')
    if wind[0] is "" or wind[0] is " ":
        wind[0] = y2[-1]
    y2.append(float(wind[0]))
b0, b1 = lr.get_coefs(x,y0)

date = "2014-02-13T06:20:00"
date = get_x(date)
print(b0,b1,date, x[0])
print(lr.predict(b0,b1,date))
