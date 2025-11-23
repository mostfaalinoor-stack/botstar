import re
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def reg(cc):
    regex = r'\d+'
    matches = re.findall(regex, cc)
    data = matches
    cc = f"{data[0]}|{data[1].zfill(2)}|{data[2]}|{data[3]}"
    n = cc.split("|")[0]
    mm = cc.split("|")[1]
    yy = cc.split("|")[2]
    cvc = cc.split("|")[3]
    if len(mm) == 1:
        mm = '0' + mm
        mm = str(mm)
    if "20" in yy:
        yy = yy.split("20")[1]
    yy='20'+yy

    bi = n[0:1]
    if "3" in bi:
        cvc = cvc[0:4]
    else:
        cvc = cvc[0:3]
    cc = (f"{n}|{mm}|{yy}|{cvc}")
    return cc

#reg("374769010165999|07|28|6990")