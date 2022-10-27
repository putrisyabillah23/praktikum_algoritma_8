# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 12:23:21 2022

@author: putri
"""

def bulan(): 
    print ("menentukan hari dan bulan")

while True:
    print ("tekan 0 untuk menghentikan program")
    x = int(input("sekarang bulan ke berapa (1-12) ?"))
    if (x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12):
        print ("jumlah harinya adalah 31\n")
    elif (x==2):
        print ("jumlah harinya adalah 28\n")
    elif (x==0):
        print ("terimakasih, semoga bulan ini menyenangkan...\n")
        break
    else :
        print ("jumlah harinya adalah 30\n")
        
x = bulan
print (x)
        
        