# -*- coding: UTF-8 -*-

import random

group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0

realCount = 0;

temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
temp5 = 0

for i in range(1000000):
    temp1 = random.randint(1,96)
    #print temp1
    temp2 = random.randint(1,97-temp1)
    #print temp1,temp2
    temp3 = random.randint(1,98-temp1-temp2)
    #print temp1,temp2,temp3
    temp4 = random.randint(1,99-temp1-temp2-temp3)
    #print temp1,temp2,temp3,temp4
    temp5 = 100-temp1-temp2-temp3-temp4
    #print temp1,temp2,temp3,temp4,temp5

    orderList = [];
    orderList.append(temp1);
    orderList.append(temp2);
    orderList.append(temp3);
    orderList.append(temp4);
    orderList.append(temp5);

    orderList.sort()

    if(orderList[0] == orderList[1] | orderList[3] == orderList [4]):
        continue
    realCount = realCount + 1
    maxOrder = orderList[4]
    if(temp1 == maxOrder):
        group_1 = group_1 + 1
    elif (temp2 == maxOrder):
        group_2 = group_2 + 1
    elif (temp3 == maxOrder):
        group_3 = group_3 + 1
    elif (temp4 == maxOrder):
        group_4 = group_4 + 1
    elif (temp5 == maxOrder):
        group_5 = group_5 + 1

    minOrder = orderList[0]
    if (temp1 == minOrder):
        group_1 = group_1 + 1
    elif (temp2 == minOrder):
        group_2 = group_2 + 1
    elif (temp3 == minOrder):
        group_3 = group_3 + 1
    elif (temp4 == minOrder):
        group_4 = group_4 + 1
    elif (temp5 == minOrder):
        group_5 = group_5 + 1

realCount = realCount*2.0

rate1 = group_1/realCount
rate2 = group_2/realCount
rate3 = group_3/realCount
rate4 = group_4/realCount
rate5 = group_5/realCount

print rate1,rate2,rate3,rate4,rate5