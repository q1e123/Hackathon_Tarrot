output = open("dataset","w")

temp = open("tempm.txt","r")
hum = open("hum.txt","r")
wind = open("wspdm.txt","r")

linesT = temp.readlines()
linesH = hum.readLines()
linesW = wind.readLines()

for i in range(0, len(linesT)):
    dataT = [] 
    dataH = []
    dataW = []
    dataT = linesT.split(',')
    dataH = linesH.split(',')
    dataW = linesW.split(',')

    for j in range(0, len(dataT)):
        recT = dataT[j].split('"')
        key = recT[1] 
        valueT = recT[3]
        recH = dataH[j].split('"')
        valueH = recH[3]
        recW = dataW[j].split('"')
        valueW = recW[3]
        output.write(key + ";" + valueT + "; " + valueH + "; " + valueW)
        
    

