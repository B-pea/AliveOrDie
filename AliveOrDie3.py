# -*- coding: UTF-8 -*-

import random
import numpy as np
import pylab as pl


def eachRate(order):
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

    for i in range(100000):
        temp1 = order #random.randint(0, 100)
        # print temp1
        temp2 = random.randint(0, 100 - temp1)
        # print temp1,temp2
        temp3 = random.randint(0, 100 - temp1 - temp2)
        # print temp1,temp2,temp3
        temp4 = random.randint(0, 100 - temp1 - temp2 - temp3)
        # print temp1,temp2,temp3,temp4
        temp5 = 100 - temp1 - temp2 - temp3 - temp4
        # print temp1,temp2,temp3,temp4,temp5

        orderList = [];
        orderList.append(temp1);
        orderList.append(temp2);
        orderList.append(temp3);
        orderList.append(temp4);
        orderList.append(temp5);

        orderList.sort()

        # realCount = realCount + 1
        maxOrder = orderList[4]

        if (temp1 == maxOrder):
            group_1 = group_1 + 1
            realCount = realCount + 1
        if (temp2 == maxOrder):
            group_2 = group_2 + 1
            realCount = realCount + 1
        if (temp3 == maxOrder):
            group_3 = group_3 + 1
            realCount = realCount + 1
        if (temp4 == maxOrder):
            group_4 = group_4 + 1
            realCount = realCount + 1
        if (temp5 == maxOrder):
            group_5 = group_5 + 1
            realCount = realCount + 1

        minOrder = orderList[0]
        if (temp1 == minOrder):
            group_1 = group_1 + 1
            realCount = realCount + 1
        if (temp2 == minOrder):
            group_2 = group_2 + 1
            realCount = realCount + 1
        if (temp3 == minOrder):
            group_3 = group_3 + 1
            realCount = realCount + 1
        if (temp4 == minOrder):
            group_4 = group_4 + 1
            realCount = realCount + 1
        if (temp5 == minOrder):
            group_5 = group_5 + 1
            realCount = realCount + 1

    realCount = realCount * 1.0

    rate1 = group_1 / realCount
    rate2 = group_2 / realCount
    rate3 = group_3 / realCount
    rate4 = group_4 / realCount
    rate5 = group_5 / realCount

    return rate1

rateList = range(0,100)

for i in range(0,100):
    rateList[i] = eachRate(i)*100
    print i

xAxis = range(0,100)
pl.plot(xAxis,rateList)
pl.show()

