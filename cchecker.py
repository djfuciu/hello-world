def checker(numero):
    AMEX = ["37","34"]
    MASTER = ["51","52","53","54","55"]
    if len(str(numero)) == 15 and (str(numero)[0:2] in AMEX):
        return "AMEX\n"
    elif len(str(numero)) == 16 and (str(numero)[0:2] in MASTER):
        return "MASTERCARD\n"
    elif (len(str(numero)) == 16 or len(str(numero)) == 13) and str(numero)[0:1] == "4":
        return "VISA\n"
    else:
        return "INVALID\n"

cnumber = int(raw_input("Number :"))
clist = list()
cardtype = checker(cnumber)

for i in str(cnumber):
    clist.append(i)
secdigi = 0
firdigi = list()
y = 1
while (y < len(clist) + 1):
    for x in reversed(clist):
        if y % 2 == 0:
            firdigi.append(str(2 * int(x)))
            y += 1
        else:
            secdigi += int(x)
            y += 1

firdigi_str = ''.join(firdigi)
firdigi_new = list(firdigi_str)
pproduct = 0
for x in firdigi_new:
    pproduct += int(x)
finaldigi = pproduct + secdigi
if int(finaldigi) % 10 == 0:
    print cardtype
else:
    cardtype = "INVALID\n"
    print cardtype
