import pygame

from setting import W,H

class Apple():
    def __init__(self):
        print("apple is created")

    def __str__(self):
        return("Type=Apple Class")



if __name__=="__main__":
    a = Apple()
    print(a)