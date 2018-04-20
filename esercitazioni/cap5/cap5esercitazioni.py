import numpy as np
import csv
from random import randint
arr = np.random.binomial(5,0.5,size=100)
arr = arr[1:]-arr[:-1]
#print(arr)
"""

UNITID,OPEID,OPEID6,INSTNM,COUNT_ED,AGEGE24,PCT_WHITE,PCT_BLACK,PCT_ASIAN,PCT_HISPANIC,PCT_BA,PCT_GRAD_PROF,PCT_BORN_US,MEDIAN_HH_INC,POVERTY_RATE,UNEMP_RATE,LN_MEDIAN_HH_INC,COUNT_NWNE_P10,COUNT_WNE_P10,MN_EARN_WNE_P10,MD_EARN_WNE_P10,PCT10_EARN_WNE_P10,PCT25_EARN_WNE_P10,PCT75_EARN_WNE_P10,PCT90_EARN_WNE_P10,SD_EARN_WNE_P10,COUNT_WNE_INC1_P10,COUNT_WNE_INC2_P10,COUNT_WNE_INC3_P10,COUNT_WNE_INDEP0_INC1_P10,COUNT_WNE_INDEP0_P10,COUNT_WNE_INDEP1_P10,COUNT_WNE_MALE0_P10,COUNT_WNE_MALE1_P10,GT_25K_P10,MN_EARN_WNE_INC1_P10,MN_EARN_WNE_INC2_P10,MN_EARN_WNE_INC3_P10,MN_EARN_WNE_INDEP0_INC1_P10,MN_EARN_WNE_INDEP0_P10,MN_EARN_WNE_INDEP1_P10,MN_EARN_WNE_MALE0_P10,MN_EARN_WNE_MALE1_P10,COUNT_NWNE_P6,COUNT_WNE_P6,MN_EARN_WNE_P6,MD_EARN_WNE_P6,PCT10_EARN_WNE_P6,PCT25_EARN_WNE_P6,PCT75_EARN_WNE_P6,PCT90_EARN_WNE_P6,SD_EARN_WNE_P6,COUNT_WNE_INC1_P6,COUNT_WNE_INC2_P6,COUNT_WNE_INC3_P6,COUNT_WNE_INDEP0_INC1_P6,COUNT_WNE_INDEP0_P6,COUNT_WNE_INDEP1_P6,COUNT_WNE_MALE0_P6,COUNT_WNE_MALE1_P6,GT_25K_P6,MN_EARN_WNE_INC1_P6,MN_EARN_WNE_INC2_P6,MN_EARN_WNE_INC3_P6,MN_EARN_WNE_INDEP0_INC1_P6,MN_EARN_WNE_INDEP0_P6,MN_EARN_WNE_INDEP1_P6,MN_EARN_WNE_MALE0_P6,MN_EARN_WNE_MALE1_P6,COUNT_NWNE_P7,COUNT_WNE_P7,MN_EARN_WNE_P7,SD_EARN_WNE_P7,GT_25K_P7,COUNT_NWNE_P8,COUNT_WNE_P8,MN_EARN_WNE_P8,MD_EARN_WNE_P8,PCT10_EARN_WNE_P8,PCT25_EARN_WNE_P8,PCT75_EARN_WNE_P8,PCT90_EARN_WNE_P8,SD_EARN_WNE_P8,GT_25K_P8,COUNT_NWNE_P9,COUNT_WNE_P9,MN_EARN_WNE_P9,SD_EARN_WNE_P9,GT_25K_P9
Purtroppo il dataset indicato nel libbro non c'è il campo latitude e longitude
"""
dic=[]
reader = []
with open("cap5.csv",newline='') as infile:
    reader = list(csv.reader(infile, delimiter=','))

index_black = reader[0].index("PCT_BLACK")
index_white = reader[0].index("PCT_WHITE")
pctBlack= []
pctWhite= []
for index, row in enumerate(reader):
    if index > 0 and index<150:
        pctWhite.append(row[index_white])
        pctBlack.append(row[index_black])
        #dic.append(dict(zip(reader[randint(0,len(reader)-1)],row)))

_t1 = [not n.isdigit() for n in pctBlack]
_t2 = [not n.isdigit() for n in pctWhite]


_t1 = [not n == "NULL" or n.isdigit() for n in pctBlack]
_t2 = [not n == "NULL" or n.isdigit() for n in pctWhite]

for index, number in enumerate(_t1):
    if not number or pctBlack[index] == 'PrivacySuppressed':
        pctBlack[index] = 0.0

for index, number in enumerate(_t1):
    if not number:
        pctWhite[index]=0.0


print(pctWhite)
print(pctBlack)



pctBlack = np.array(pctBlack).astype(np.float)
mediaPctBlack = np.median(pctBlack)

pctWhite = np.array(pctWhite).astype(np.float)
mediapctWhite = np.median(pctWhite)

print("mediaPctBlack: ", mediaPctBlack)
print("mediapctWhite: ", mediapctWhite)


def calcoloDista(p1,p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])
