
f = open('a.txt')
line = " "
out =  []
res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
while line:
    # print(line)
    line = f.readline()
    line.split()
    if (line.find("node") > 0):
        # print(line)
        n = line.find("node")
        out.append(line[n:-1])
        # print(line.find("node"))
        print(line[n:])
f.close()

for i in range(1, 11):
    print(i)
    # print(i[4:])

