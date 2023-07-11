import random
import matplotlib.pyplot as plt

def shuffle():
    arr = ['goat', 'goat', 'car']
    random.shuffle(arr)
    initialization(arr)

def initialization(arr):
    firstChoice = int(input("Kaçıncı kapını seçiyorsun[3 kapı var]: "))
    if (firstChoice < 1) or (firstChoice > 3):
        print("Böyle kapımız yok, ne yazık ki ))");
        initialization()
    start(firstChoice, arr)

def start(firstChoice, arr):
    firstChoice = firstChoice - 1
    is_True = True
    for i in range(len(arr)):
        if i == firstChoice:
            continue
        else:
            if arr[i] == 'goat' and is_True:
                print(str(i+1) + "-ci kapı açıldı => " + arr[i] + "\n\n" + "Sizin seçdiyiniz qapı: " + str(firstChoice + 1))
                openDoor = i;
                nextChoice = input("Seçiminizi değiştirmek istermisiniz ? E/H: ")
                print(arr)
                is_True = False


shuffle()
