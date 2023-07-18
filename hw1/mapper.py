#!/usr/bin/env python
 
import sys
import csv

def main():
    s=0
    ck=0
    s_quad=0
    reader=csv.reader(sys.stdin)
    for line in reader:
        s+=int(line[9])
        s_quad+=int(line[9])**2
        ck+=1
    mk=s/ck
    vk=(s_quad-ck*mk**2)/(ck-1)
    print (ck, mk, vk)    
 
if __name__=="__main__":
    main()
 