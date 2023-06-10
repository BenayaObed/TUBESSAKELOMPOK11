import time
from itertools import combinations
import os

def greedy(hand):
    print("\nPilih metode greedy")
    print("1. Greedy by power")
    print("2. Greedy by cost")
    print("0. back")
    pilihan = int(input("Masukkan no metode yang pilih: "))
    if pilihan == 1:
        start_time = time.perf_counter()
        for i in range(len(hand)):
            for j in range(i+1, len(hand)):
                if hand[j].power > hand[i].power:
                    hand[i], hand[j] = hand[j], hand[i]
    elif pilihan == 2:
        start_time = time.perf_counter()
        for i in range(len(hand)):
            for j in range(i+1, len(hand)):
                if hand[j].cost < hand[i].cost:
                    hand[i], hand[j] = hand[j], hand[i]
    else:
        menu()

    solusi = [] 
    totalCost = 0
    totalPower = 0
    for card in range(len(hand)):
        if len(solusi) < 3 and (totalCost + hand[card].cost) <= maxCost:
            totalCost += hand[card].cost
            totalPower += hand[card].power
            solusi.append(hand[card])
            hand[card].play = 1
    #Hentikan timer dan hitung waktu eksekusi
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    #Tampilkan hasil
    os.system('cls')
    print("--------------->> GREEDY <<---------------")
    print ("{:<2} {:<20} {:<4} {:<5} {:<4}".format('No', 'Name', 'Cost', 'Power', 'Play'))
    for i in range(len(hand)):
        print ("{:<2} {:<20} {:<4} {:<5} {:<4}".format(i+1, hand[i].name, hand[i].cost, hand[i].power, hand[i].play))
        hand[i].play = 0

    print("\nBest Card To Play:")
    print ("{:<2} {:<20} {:<4} {:<5}".format('No', 'Name', 'Cost', 'Power'))
    for i in range(len(solusi)):
        print ("{:<2} {:<20} {:<4} {:<5}".format(i+1, solusi[i].name, solusi[i].cost, solusi[i].power,))
    print("\nTotal Cost card yang di play\t:" , totalCost)
    print("Total Power card yang di play\t:" , totalPower)
    print("Execution Time: {:.6f} seconds\n".format(execution_time))
    input("Press any key to continue")
    menu()

def bruteForce(hand):
    #Mulai timer untuk menghitung waktu eksekusi
    start_time = time.perf_counter()

    #Generate semua combinasi kartu
    all_combinations = []
    for r in range(1, len(hand) + 1):
        combinations_r = combinations(hand, r)
        all_combinations.extend(combinations_r)

    HighestCost = 0 #untuk menyimpan total cost kartu yang terpilih
    HighestPower = 0 #untuk menyimpan total power kartu dengan pow
    BestPlay = [] #menyimpan combinasi kartu terbaik untuk dimainkan

    #Mencari solusi terbaik
    for combination in all_combinations:
        tempCost = 0
        tempPower = 0
        tempCards = []
        #menghitung total power dan cost dari kombinasi kartu
        for card in combination:
            tempCost += card.cost
            tempPower += card.power
            tempCards.append(card)
        #mengecek kombinasi apakah sudah sesuai dengan contraint dan memiliki power tertinggi
        if tempCost <= maxCost and tempPower > HighestPower and len(tempCards) <= 3:
            HighestPower = tempPower
            HighestCost = tempCost
            BestPlay = tempCards

    #Hentikan timer dan hitung waktu eksekusi
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    #Tampilkan hasil
    os.system('cls')
    print("--------------->> Brute Force <<---------------")
    print("Semua kombinasi Kartu:\n")
    for combination in all_combinations:
        tempCost = 0
        tempPower = 0
        for card in combination:
            print(card.name, end=", ")
            tempCost += card.cost
            tempPower += card.power
        print("\nCost={} Power={}".format(tempCost, tempPower), end=" ")
        if tempCost <= maxCost and len(combination) <= 3:
            print("Bisa dimainkan\n")
        else:
            print("Tidak bisa dimainkan\n")
    
    print("\nBest Card To Play:")
    print ("{:<2} {:<20} {:<4} {:<5}".format('No', 'Name', 'Cost', 'Power'))
    for i in range(len(BestPlay)):
        print ("{:<2} {:<20} {:<4} {:<5}".format(i+1, BestPlay[i].name, BestPlay[i].cost, BestPlay[i].power,))
    print("\nTotal cost kartu yang dimainkan:", HighestCost)
    print("Total power kartu yang dimainkan:", HighestPower)
    print("\nExecution Time: {:.6f} seconds\n".format(execution_time))
    input("Press any key to continue")
    menu()

def showHand():
    os.system('cls')
    print ("{:<2} {:<20} {:<4} {:<3}".format('No', 'Name', 'Cost', 'Power'))
    for i in range(len(hand)):
        print ("{:<2} {:<20} {:<4} {:<3}".format(i+1, hand[i].name, hand[i].cost, hand[i].power))

class Card:
    def __init__(self, name, cost, power, play):
        self.name = name
        self.cost = cost
        self.power = power
        self.play = play

maxCost = int(input("Masukkan Max Cost: "))
hand = []
for i in range(5):
    print("Kartu %d" %(i+1))
    name = input("Nama: ")
    cost = int(input("Cost: "))
    power = int(input("Power: "))
    tempcard = Card(name, cost, power, 0)
    hand.append(tempcard)

def menu():
    showHand()
    print("\nPilih metode (1 atau 2)")
    print("1. Greedy")
    print("2. Brute Force")
    print("0. Exit")
    pilihan = int(input("Masukkan no metode yang pilih: "))
    if pilihan == 1:
        greedy(hand)
    elif pilihan == 2:
        bruteForce(hand)
    else:
        quit()
    
menu()