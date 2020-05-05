#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 07:12:09 2019

@author: ubuntu
"""

fp = open('/home/ubuntu/Desktop/scripting_as2/ipl_auction.txt','r')

str1 = fp.readline()
ss = []
indians = []
foreigns = []
bat = []
bowl = []
alr = []
wk = []
fbat = []
fbowl = []
falr = []
fwk = []
ss = set(ss)

while str1:
    str2 = str1.split(":")
    print(str2[0]," ",str2[1]," ",str2[2])
    if str2[0] not in ss:
        ss.add(str2[0])
        if(str2[1] == "India"):
            print("in india")
            indians.append(str1)
            if(str2[2] == "All-Rounder"):
                alr.append(str1)
            elif(str2[2] == "Batsman"):
                bat.append(str1)
            elif(str2[2] == "Bowler"):
                bowl.append(str1)
            else:
                wk.append(str1)
        else:
            foreigns.append(str1)
            print("in others")
            if(str2[2] == "All-Rounder"):
                falr.append(str1)
            elif(str2[2] == "Batsman"):
                fbat.append(str1)
            elif(str2[2] == "Bowler"):
                fbowl.append(str1)
            else:
                fwk.append(str1)
    else:
        print("others")

    str1 = fp.readline()
fp.close()

print("Indian all-rounder = ", len(alr))
print("Indians batsman = ", len(bat))
print("Indians bowler = ", len(bowl))
print("Indians wicketkeeper = ", len(wk))
print("Other All-rounder = " , len(falr))
print("Other batsman = ", len(fbat))
print("Other bowler = ", len(fbowl))
print("Other wk = ", len(fwk))

teams = []
fp = open('/home/ubuntu/Desktop/scripting_as2/config.txt','r')
str1 = fp.readline()
print(str1)
while str1:
    print(str1)
    str2 = str1.split(":")
    print(str2[0])
    if(str2[0] == "team_names"):
        str2 = fp.readline()

        while str2:
            teams.append(str2)
            str2 = fp.readline()
    str1 = fp.readline()


fp.close()

no_of_teams = 8

for i in range(no_of_teams):
    j = 0;
    path = '/home/ubuntu/Desktop/scripting_as2/'
    path = path + 'Teams/'
    str1 = teams[i]
    str2 = str1
    str1 = str1[:-1]
    print(str1)
    path = path + str1
    path = path + '.txt'
    print(path)
    fp = open(path, "w+")
    fp.write(str2)
    ''' placed all indian batsman to the maximum constraint given
    placed 7 batsman in each team'''
    for i in range(0,7):
        str2 = bat[0]
        tokens = str2.split(":")
        playerno = "Player " + str(j+1) + '\n'
        fp.write(playerno)
        name = "Name: " + tokens[0] + '\n'
        fp.write(name)
        country = "Country: " + tokens[1] + '\n'
        fp.write(country)
        ability = "Ability: "+tokens[2] +'\n'
        fp.write(ability)
        fees = "Fees: "+tokens[3]
        fp.write(fees)
        j = j+1
        del bat[0]



    '''placed all indian bowlers - they were sufficient to satisfy the criteria
    placed 4 bowlers in each team'''
    for i in range(0,4):
        str2 = bowl[0]
        tokens = str2.split(":")
        playerno = "Player " + str(j+1) + '\n'
        fp.write(playerno)
        name = "Name: " + tokens[0] + '\n'
        fp.write(name)
        country = "Country: " + tokens[1] + '\n'
        fp.write(country)
        ability = "Ability: "+tokens[2] +'\n'
        fp.write(ability)
        fees = "Fees: "+tokens[3]
        fp.write(fees)
        j = j+1
        #str2 = str2[:-1]
        #fp.write(str2)
        del bowl[0]
    ''' based on the number of wicketkeepers available .. i selected the number of
    all-rounders from countries other than India

    if wicketkeepers are from india - selected an extra all-rounder
    if wicketkeepers were not from india - then selected two less allrounder
    if wk == 2 : all-rounders = 5
    if fwk == 2: all-rounders = 3
    '''
    if len(wk) > 1:
        #str2 = wk[0]
        for i in range(2):
            str2 = wk[0]
            tokens = str2.split(":")
            playerno = "Player " + str(j+1) + '\n'
            fp.write(playerno)
            name = "Name: " + tokens[0] + '\n'
            fp.write(name)
            country = "Country: " + tokens[1] + '\n'
            fp.write(country)
            ability = "Ability: "+tokens[2] +'\n'
            fp.write(ability)
            fees = "Fees: "+tokens[3]
            fp.write(fees)
            j = j+1
            #fp.write(str2)
            del wk[0]
        for i in range(5):
            str2 = falr[0]
            tokens = str2.split(":")
            playerno = "Player " + str(j+1) + '\n'
            fp.write(playerno)
            name = "Name: " + tokens[0] + '\n'
            fp.write(name)
            country = "Country: " + tokens[1] + '\n'
            fp.write(country)
            ability = "Ability: "+tokens[2] +'\n'
            fp.write(ability)
            fees = "Fees: "+tokens[3]
            fp.write(fees)
            j = j+1
            #fp.write(str2)
            del falr[0]
    else:
        for i in range(2):
            str2 = fwk[0]
            tokens = str2.split(":")
            playerno = "Player " + str(j+1) + '\n'
            fp.write(playerno)
            name = "Name: " + tokens[0] + '\n'
            fp.write(name)
            country = "Country: " + tokens[1] + '\n'
            fp.write(country)
            ability = "Ability: "+tokens[2] +'\n'
            fp.write(ability)
            fees = "Fees: "+tokens[3]
            fp.write(fees)
            j = j+1
            #fp.write(str2)
            del fwk[0]

        for i in range(5):
            str2 = falr[0]
            tokens = str2.split(":")
            playerno = "Player " + str(j+1) + '\n'
            fp.write(playerno)
            name = "Name: " + tokens[0] + '\n'
            fp.write(name)
            country = "Country: " + tokens[1] + '\n'
            fp.write(country)
            ability = "Ability: "+tokens[2] +'\n'
            fp.write(ability)
            fees = "Fees: "+tokens[3]
            fp.write(fees)
            j = j+1
            #fp.write(str2)
            del falr[0]

    fp.close()
