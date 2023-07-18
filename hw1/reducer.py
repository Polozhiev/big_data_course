#!/usr/bin/env python
 
import sys
 
def main():
    cur_var=0
    cur_mean=0
    cur_size=0
    for line in sys.stdin:
        ck, mk, vk = map(float,line.split())
        new_size=cur_size+ck
        new_mean=(cur_mean*cur_size+mk*ck)/new_size
        new_var=((cur_var*(cur_size-1)+cur_size*cur_mean**2 + vk*(ck-1)+ck*mk**2) - new_size*new_mean**2)/(new_size-1)

        cur_size=new_size
        cur_mean=new_mean
        cur_var=new_var
    print(cur_mean, cur_var)
 
if __name__=="__main__":
    main()
 
