import sys
from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq
import time
import requests
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean
import numpy as np 

print("\n")
print("Author   : Vivek Upadhyay |1104V| ")
print("VEX SCOUTING")
print("\n")
print("\n")
print("   \|\          /|/  =========   \|\      /|/")
print("    \|\        /|/   ||           \|\    /|/")
print("     \|\      /|/    ||            \|\  /|/")
print("      \|\    /|/     ||-----|       \|\/|/")   
print("       \|\  /|/      ||-----|       /|/\|\\")
print("        \|\/|/       ||            /|/  \|\\")
print("         \||/        ||           /|/    \|\\")
print("          \/         =========   /|/      \|\\")
print("\n")
print("=======================VEXDB WEBSCRAPPER======================")
print( "[   ] 0% ")
time.sleep(2)
print("[=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+] 100%")

#def vex():

oprs=[]
dprs=[]
maxsc=[]
wpap=[]
oplist = []
dplist = []
mxlist = []    

x = input("Enter Team Number ")
done = False

filename = "Vex Stats1.csv"
headers = "Team Number, opr, dpr, max, WP,  AP, SP, \n"
f = open(filename, "w")
f.write(headers)

teams = []
teams.append(x)
while done == False:
    page_url = "https://vexdb.io/teams/view/" + x + "?t=rankings"
    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    containers = page_soup.findAll("div", {"class": "table-responsive"})

   
    z = int(input("How many competitions? "))

    for i in range(0,z):
        for container in containers: 
            
            opr_container = container.findAll("td", {"class": "opr"})
            opr = opr_container[i].text.strip()

            dpr_container = container.findAll("td", {"class": "dpr"})
            dpr = dpr_container[i].text.strip()

            score_container = container.findAll("td", {"class": "max_score"})
            maxs = score_container[i].text.strip()

            wpsp_container = container.findAll("td", {"class": "wpsp"})
            wpsp = wpsp_container[i].text.strip()
            wpap.append(float(maxs))

            print("\n")
            print("OPR: " +opr)
            print("DPR: " +dpr)
            print("MAX: " +maxs)
            print("WP/AP/SP: " +wpsp)
            print("\n")
            adder=(x + "," + opr + "," + dpr + "," + maxs + "," + wpsp.replace("/",",") + "\n")
            f.write(adder)
            
            oprs.append(float(opr))
            dprs.append(float(dpr))
            maxsc.append(float(maxs))
    oplist.append(sum(oprs) / len(oprs))
    dplist.append(sum(dprs) / len(dprs))
    mxlist.append(sum(maxsc) / len(maxsc))
    
    
        
    imp=input("Another Team? (y/n) ")
    if imp == 'y':
        x = input("Enter Team Number ")
        teams.append(x)
        oprs=[]
        dprs=[]
        maxsc=[]
        wpap=[]

    if imp == 'n':
        done = True

print(oplist)
print(dplist)
print(mxlist)

X = teams
opers = oplist
dpers = dplist
maxers = mxlist

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, opers, 0.2, color='#000080', label = 'OP')
plt.bar(X_axis + 0.2, dpers, 0.2, color='#0F52BA', label = 'DP')
plt.bar(X_axis + 0, maxers, 0.2, color='#6593F5', label = 'Max')


#plt.bar(X_axis + 0.4, maxers, 0.2, label = 'WPSP')

plt.xticks(X_axis, X)
plt.xlabel("Teams")
plt.ylabel("Points")
plt.title("Statics of Vex Teams")
plt.legend()
plt.show()
    


#print(walist)


    

'''
    imp=input("Another Team? (y/n)")
    if imp == 'y':
        vex()
    
vex()
'''
