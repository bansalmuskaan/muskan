# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:17:32 2019

@author: Dell
"""

for i in range(1,20):
    if(i%3==0 and i%5==0):
        print(str(i)+'=fizzbuzz')
    else:
        if(i%3==0):
            print(i,'=fizz')
        else:
            if(i%5==0):
                print(i,'buzz')
            else:
                print(i)
            