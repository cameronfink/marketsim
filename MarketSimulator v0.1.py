# Import necessary things
import random
import string
import uuid
import sqlite3
from random import randint, seed, randrange
from time import sleep
from os import system, name

# Seed random generator
seed(randint(0,1000))

# Clear screen function
def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

# Print copyright and welcome screen
print('')
print('')
print('')
print('')
print('Welcome to MarketSimulator v0.1 Icahn')
print('Developed by Cameron Fink, Copyright Cameron Fink 2020')

# Clear screen
sleep(3)
clear()

# Ticker generator function
def randomticker(stringLength=8):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Set original variables
price1 = randint(0,100)
price2 = randint(0,100)
price3 = randint(0,100)
price4 = randint(0,100)
price5 = randint(0,100)

# Set tickers
ticker1 = randomticker(4)
ticker2 = randomticker(4)
ticker3 = randomticker(4)
ticker4 = randomticker(4)
ticker5 = randomticker(4)

# Print day 1 stocks
print('Day 1:')
print("Ticker", ticker1, 'Price : ', price1)
print("Ticker", ticker2, 'Price : ', price2)
print("Ticker", ticker3, 'Price : ', price3)
print("Ticker", ticker4, 'Price : ', price4)
print("Ticker", ticker5, 'Price : ', price5)
print('')

# Adjust variables for day 2
price1_2 = price1 + randint(-50,50)
price2_2 = price2 + randint(-50,50)
price3_2 = price3 + randint(-50,50)
price4_2 = price4 + randint(-50,50)
price5_2 = price5 + randint(-50,50)

# Negative price checker
if price1_2 < 1:
    price1_2 = 'Stock Crashed'

if price2_2 < 1:
    price2_2 = 'Stock Crashed'

if price3_2 < 1:
    price3_2 = 'Stock Crashed'

if price4_2 < 1:
    price4_2 = 'Stock Crashed'

if price5_2 < 1:
    price5_2 = 'Stock Crashed'

# Couple seconds break
sleep(2)

# Print day 2 stocks
print('Day 2:')
print("Ticker", ticker1, 'Price : ', price1_2)
print("Ticker", ticker2, 'Price : ', price2_2)
print("Ticker", ticker3, 'Price : ', price3_2)
print("Ticker", ticker4, 'Price : ', price4_2)
print("Ticker", ticker5, 'Price : ', price5_2)
print('')

# Adjust variables for day 3
if price1_2 == 'Stock Crashed':
    price1_3 = 'Stock Crashed'
else:
    price1_3 = price1_2 + randint(-50,50)

if price2_2 == 'Stock Crashed':
    price2_3 = 'Stock Crashed'
else:
    price2_3 = price2_2 + randint(-50,50)

if price3_2 == 'Stock Crashed':
    price3_3 = 'Stock Crashed'
else:
    price3_3 = price3_2 + randint(-50,50)

if price4_2 == 'Stock Crashed':
    price4_3 = 'Stock Crashed'
else:
    price4_3 = price4_2 + randint(-50,50)

if price5_2 == 'Stock Crashed':
    price5_3 = 'Stock Crashed'
else:
    price5_3 = price5_2 + randint(-50,50)

# Negative price checker
if price1_3 == 'Stock Crashed':
    price1_3 = 'Stock Crashed'
elif price1_3 < 1:
    price1_3 = 'Stock Crashed'

if price2_3 == 'Stock Crashed':
    price2_3 = 'Stock Crashed'
elif price2_3 < 1:
    price2_3 = 'Stock Crashed'

if price3_3 == 'Stock Crashed':
    price3_3 = 'Stock Crashed'
elif price3_3 < 1:
    price3_3 = 'Stock Crashed'

if price4_3 == 'Stock Crashed':
    price4_3 = 'Stock Crashed'
elif price4_3 < 1:
    price4_3 = 'Stock Crashed'

if price5_3 == 'Stock Crashed':
    price5_3 = 'Stock Crashed'
elif price5_3 < 1:
    price5_3 = 'Stock Crashed'

# Couple seconds break
sleep(2)

# Print day 3 stocks
print('Day 3:')
print("Ticker", ticker1, 'Price : ', price1_3)
print("Ticker", ticker2, 'Price : ', price2_3)
print("Ticker", ticker3, 'Price : ', price3_3)
print("Ticker", ticker4, 'Price : ', price4_3)
print("Ticker", ticker5, 'Price : ', price5_3)
print('')

# Adjust variables for day 4
if price1_3 == 'Stock Crashed':
    price1_4 = 'Stock Crashed'
else:
    price1_4 = price1_3 + randint(-50,50)

if price2_3 == 'Stock Crashed':
    price2_4 = 'Stock Crashed'
else:
    price2_4 = price2_3 + randint(-50,50)

if price3_3 == 'Stock Crashed':
    price3_4 = 'Stock Crashed'
else:
    price3_4 = price3_3 + randint(-50,50)

if price4_3 == 'Stock Crashed':
    price4_4 = 'Stock Crashed'
else:
    price4_4 = price4_3 + randint(-50,50)

if price5_3 == 'Stock Crashed':
    price5_4 = 'Stock Crashed'
else:
    price5_4 = price5_3 + randint(-50,50)

# Negative price checker
if price1_4 == 'Stock Crashed':
    price1_4 = 'Stock Crashed'
elif price1_4 < 1:
    price1_4 = 'Stock Crashed'

if price2_4 == 'Stock Crashed':
    price2_4 = 'Stock Crashed'
elif price2_4 < 1:
    price2_4 = 'Stock Crashed'

if price3_4 == 'Stock Crashed':
    price3_4 = 'Stock Crashed'
elif price3_4 < 1:
    price3_4 = 'Stock Crashed'

if price4_4 == 'Stock Crashed':
    price4_4 = 'Stock Crashed'
elif price4_4 < 1:
    price4_4 = 'Stock Crashed'

if price5_4 == 'Stock Crashed':
    price5_4 = 'Stock Crashed'
elif price5_4 < 1:
    price5_4 = 'Stock Crashed'

# Couple seconds break
sleep(2)

# Print day 4 stocks
print('Day 4:')
print("Ticker", ticker1, 'Price : ', price1_4)
print("Ticker", ticker2, 'Price : ', price2_4)
print("Ticker", ticker3, 'Price : ', price3_4)
print("Ticker", ticker4, 'Price : ', price4_4)
print("Ticker", ticker5, 'Price : ', price5_4)
print('')

# Adjust variables for day 5
if price1_4 == 'Stock Crashed':
    price1_5 = 'Stock Crashed'
else:
    price1_5 = price1_4 + randint(-50,50)

if price2_4 == 'Stock Crashed':
    price2_5 = 'Stock Crashed'
else:
    price2_5 = price2_4 + randint(-50,50)

if price3_4 == 'Stock Crashed':
    price3_5 = 'Stock Crashed'
else:
    price3_5 = price3_4 + randint(-50,50)

if price4_4 == 'Stock Crashed':
    price4_5 = 'Stock Crashed'
else:
    price4_5 = price4_4 + randint(-50,50)

if price5_4 == 'Stock Crashed':
    price5_5 = 'Stock Crashed'
else:
    price5_5 = price5_4 + randint(-50,50)

# Negative price checker
if price1_5 == 'Stock Crashed':
    price1_5 = 'Stock Crashed'
elif price1_5 < 1:
    price1_5 = 'Stock Crashed'

if price2_5 == 'Stock Crashed':
    price2_5 = 'Stock Crashed'
elif price2_5 < 1:
    price2_5 = 'Stock Crashed'

if price3_5 == 'Stock Crashed':
    price3_5 = 'Stock Crashed'
elif price3_5 < 1:
    price3_5 = 'Stock Crashed'

if price4_5 == 'Stock Crashed':
    price4_5 = 'Stock Crashed'
elif price4_5 < 1:
    price4_5 = 'Stock Crashed'

if price5_5 == 'Stock Crashed':
    price5_5 = 'Stock Crashed'
elif price5_5 < 1:
    price5_5 = 'Stock Crashed'

# Couple seconds break
sleep(2)

# Print day 5 stocks
print('Day 5:')
print("Ticker", ticker1, 'Price : ', price1_5)
print("Ticker", ticker2, 'Price : ', price2_5)
print("Ticker", ticker3, 'Price : ', price3_5)
print("Ticker", ticker4, 'Price : ', price4_5)
print("Ticker", ticker5, 'Price : ', price5_5)
print('')

# Find biggest week 1 biggest winner
if price1_5 == 'Stock Crashed':
    price1week1 = -100
else:
    price1week1 = price1_5 - price1

if price2_5 == 'Stock Crashed':
    price2week1 = -100
else:
    price2week1 = price2_5 - price2

if price3_5 == 'Stock Crashed':
    price3week1 = -100
else:
    price3week1 = price3_5 - price3

if price4_5 == 'Stock Crashed':
    price4week1 = -100
else:
    price4week1 = price4_5 - price4

if price5_5 == 'Stock Crashed':
    price5week1 = -100
else:
    price5week1 = price5_5 - price5

week1list = [price1week1, price2week1, price3week1, price4week1, price5week1]

if max(week1list) == price1week1:
    week1winner = ticker1 + ' with a total gain of ' + str(price1week1)
elif max(week1list) == price2week1:
    week1winner = ticker2 + ' with a total gain of ' + str(price2week1)
elif max(week1list) == price3week1:
    week1winner = ticker3 + ' with a total gain of ' + str(price3week1)
elif max(week1list) == price4week1:
    week1winner = ticker4 + ' with a total gain of ' + str(price4week1)
elif max(week1list) == price5week1:
    week1winner = ticker5 + ' with a total gain of ' + str(price5week1)

print('Week 1 biggest gainer is: ' + week1winner)