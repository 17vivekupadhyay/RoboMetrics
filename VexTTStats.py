from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq
import time
import requests
#import pandas as pd

print("\n")
print("Author   : Vivek Upadhyay |1104X| ")
print("VEX SCOUTING")
print("\n")
print("||===} ====  ===== ===== ======  ======) ====== ====== =====  ")
print("||   }  ||   ||    ||    ||  ||  ||    ) ||  ||   ||   ||   ")
print("||   }  ||   ====  ||    ||  ||  ||===)  ||  ||   ||   ==== ")
print("||   }  ||     ||  ||    ||  ||  ||    ) ||  ||   ||     || ")
print("||===} ====  ====  ===== ======  ||===)  ======   ||   ====  ")
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

def vex():
    x = input("Enter Team Number")
    z = int(input("How many competitions?"))

    page_url = "https://vexdb.io/teams/view/" + x + "?t=rankings"
    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    containers = page_soup.findAll("div", {"class": "table-responsive"})

    filename = "Vex Stats1.csv"
    
    headers = "Team Number, opr, dpr, max, WP,  AP, SP, \n"
    f = open(filename, "w")
    f.write(headers)

    oprs=[]
    dprs=[]
    maxsc=[]
    wpap=[]
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

            
                
            print("\n")
            print("OPR: " +opr)
            print("DPR: " +dpr)
            print("MAX: " +maxs)
            print("WP/AP/SP: " +wpsp)
            print("\n")
            adder=(x + "," + opr + "," + dpr + "," + maxs + "," + wpsp.replace("/",",") + "\n")
            f.write(adder)


    imp=input("Another Team? (y/n)")
    if imp == 'y':
        vex()
    
vex()

   # yes = ["YES",
   #        "Yes",
   #        "yes",
   #        "y",
   #        "Y",
   #        "ye",
   #        "yer",
   #        "ya",
   #        "yeah",
   #         ]
    
    #no = ["NO",    
    #      "no",
    #      "No",
    #      "N",
    #      "n"]

