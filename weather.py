import linear_regression as lr
import utils

utils.dataset_join()

data_file = open("dataset","r")

data_lines = data_file.readlines()


def get_x(date):
    date = date.split('T')
    x = 0
    x += (utils.stoi(date[0],'-')*1000000)
    x += utils.stoi(date[1],':')
    return x

def get_year():
    ds = open("dataset","r")
    fl = ds.readline()
    ds.close()
    return fl[:4]
    
# f(x) = y , x = data y = {temp, umid, vant}
def predict(input):
    x = []
    y0 = []
    y1 = []
    y2 = []
    year = get_year()
    for line in data_lines:
        date, temp, hum, wind = line.split(';')
        date = get_x(date)
        x.append(date)
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

    _x = x.copy()

    date = input
    date = year + date[4:]
    date = get_x(date)

    b0, b1_temp = lr.get_coefs(x,y0)
    temp_predict = lr.predict(b0,b1_temp,date)
    
    x = _x.copy()
    b0, b1_umid = lr.get_coefs(x,y1)
    umid_predict = lr.predict(b0,b1_umid,date)
    
    x = _x.copy()
    b0, b1_vant = lr.get_coefs(x,y2)
    vant_predict = lr.predict(b0,b1_vant,date)    
    
    return temp_predict, umid_predict, vant_predict
