# -*- coding: utf-8 -*-
"""
This code created on Thu Sep 29 10:38:44 2022

@author: belvandini
"""
uname = input("hi what's your name? ")
print(f"nice to see you, {uname} ")
print("put the data on down below, don't forget to enter! ")

#proses input data kota A
import math
input("Masukan Nama Kota A = ")
x1 = float(input("Masukan garis bujur kota A : ")) 
y1 = float(input("Masukan garis lintang Kota A : "))

print("***********************************")

#proses input data kota B
input("Masukan Nama Kota B = ")
x2= float(input("Masukan garis bujur kota B : "))
y2= float(input("Masukan garis lintang Kota B : "))

#rumus
xlat = x2-x1
ylon = y2-y1

a = math.sin(math.radians(xlat/2)) **2 + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.sin(math.radians(ylon/2)) **2

b = 2 * math.asin(math.sqrt(a))

r = 6371.01

print("************************************")

#hasil dari penghitungan jarak
print("jarak antara dua kota adalah" , b*r , "kilometer")
