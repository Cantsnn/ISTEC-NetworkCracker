#!/usr/bin/env python
import os 
import subprocess   
from subprocess import check_call
from scapy.all import *
import sys, signal 
from multiprocessing import Process
import time
import csv


if os.path.exists('output.txt'):
  os.remove('output.txt')
#interface adını 9-17. satırlarda alıyoruz
os.system('airmon-ng >> output.txt')
f = open('output.txt', 'r')
i = 0
for line in f:
  for word in line.split():
    i+=1
    if i == 6:
      interface = word
      print(interface)
order = "airmon-ng start {} && airmon-ng check kill".format(interface)
geny  = os.system(order)
os.system('airmon-ng >> output2.txt')
f = open('output2.txt', 'r')
i = 0
for line in f:
  for word in line.split():
    i+=1
    if i == 6:
      interfacemon = word
      print(interfacemon)
order = f"airodump-ng {interfacemon} -M -w myOutput --output-format csv & sleep 10; kill $!"
geny = os.system(order)


with open('myOutput-01.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	lines = list(reader)
	print(lines)
readFile.close()

