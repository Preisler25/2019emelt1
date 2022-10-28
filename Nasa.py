class Keres():
    def __init__(self, list):
        self.domain = list[0]
        self.time = list[1]
        self.req = list[2]
        self.resp = list[3].split(" ")[0]
        self.size = list[3].split(" ")[1]
        self.has_domain = self.isDomain()

    def showObj(self):
        print(f'Cim: "{self.domain}"\nDatumIdo: "{self.time}"\nGet: "{self.req}"\nHttpKod: "{self.resp}"\nMeret: "{self.size}"\n')

    def isDomain(self):
        if self.domain[-1] == "0" or self.domain[-1] == "1" or self.domain[-1] == "2" or self.domain[-1] == "3" or self.domain[-1] == "4" or self.domain[-1] == "5" or self.domain[-1] == "6" or self.domain[-1] == "7" or self.domain[-1] == "8" or self.domain[-1] == "9":
            return False
        return True
def importFromTXT():
    temp = []
    f= open('NASAlog.txt', 'r').read()
    lines = f.split("\n")
    for i in lines:
        temp.append(Keres(i.split("*")))
    return temp
def byteMeret(list):
    temp = 0
    for i in range(len(list)):
        if list[i].size != "-":
            temp += int(list[i].size)
    return temp
def calcDomain(list):
    temp = 0
    for i in range(len(list)):
        if list[i].has_domain == True:
            temp += 1
    return round(temp/len(list)*100, 2) 
def createList(list):
    temp = []
    for i in range(len(list)):
        if list[i].resp not in temp:
            temp.append(list[i].resp)
    return temp
def showStat(list):
    temp = f""
    var = createList(list)
    for i in var:
        count_temp = 0
        for j in range(len(list)):
            if i == list[j].resp:
                count_temp += 1
        temp += f"\n       {i}: {count_temp} db"
    return temp
def main():
    main_list = importFromTXT()
    print(f"5. feladat: Kérések száma: {len(main_list)}")
    print(f"6. feladat: Válaszok össtes mérete: {byteMeret(main_list)} byte")
    print(f"8. feladat: Domain-es kérések: {calcDomain(main_list)}%")
    print(f"9. feladat: Statisztika:{showStat(main_list)}")

main()