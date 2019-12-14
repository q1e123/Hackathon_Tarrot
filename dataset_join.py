output = open("dataset","w")

temp = open("tempm.txt",'r')
hum = open("hum.txt",'r')
wind = open("wspdm.txt",'r')

lines = temp.readlines()
for line in lines:
    data = []
    data  = line.split(',')
    #print(data)
    for record in data:
        recspt = record.split('"')
        #print(recspt)
        key = recspt[1] 
        value = recspt[3]
        #print(key, value)
        #print(key)
        #key = key[2:-1]
        #value = value[1:-1] 
        output.write(key + ";" + value+'\n')