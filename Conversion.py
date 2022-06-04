import imp


def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

#f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#c0_in_fahrenheit = c_to_f(0)

#Function for converting cups to tablespoons

def cup_to_tbsp(cup):
  tbsp = cup * 16
  return tbsp

# Function for converting tablespoons to cups

def tbsp_to_cups(tbsp):
  cup = tbsp / 16
  return cup

# Convert lbs to kg

def lbs_to_kg(lbs):
  kilogram = lbs / 2.205
  return kilogram

# Convert kg to lbs

def kg_to_lbs(kg):
  pounds = kg * 2.205
  return pounds

# Convert metre squared to square foot

def metresq_to_sqft(mtre):
  sqft = mtre * 10.764
  return sqft

# Convert square foot to metre squared

def sqft_to_metresq(sqft):
  metresq = sqft / 10.764
  return metresq

# Random Jokes

random_jokes = ["I'm not cold, just chilli", "Why was the math teacher suspicious of all the prime numbers? Because they were all odd.", "How does a mathematician plow a field? He uses a pro-tractor."]

def conversion_function():
   # Ask user to select what type of conversion would like to
  #have done
  conversion_selection = input(f""" 
  Hi {name}. Type in the letter that corresponds with
  the conversion you would like to do?
  A - Fahrenheit to celcius
  B - Celcius to fahrenheit
  c - Cups to tablespoons
  D - Tablespoons to cups
  E - Pounds to kilograms
  F - Kilograms to pounds
  G - Metre squared to square foot
  H - Square foot to metre squared
  """ ).upper()

  if conversion_selection == "A":
    conver_input = int(input("Please input the value to be converted." ))
    conversion = round(f_to_c(conver_input), 2)
    print(f"{conver_input} is equivalent to {conversion} in celcius.")
  elif conversion_selection == "B":
    conver_input = int(input("Please input the value to be converted." ))
    conversion = round(c_to_f(conver_input), 2)
    print(f"{conver_input} is equivalent to {conversion} in fahrenheit.")
  elif conversion_selection == "C":
    conver_input = int(input("Please input the value to be converted." ))
    conversion = round(cup_to_tbsp(conver_input))
    print(f"{conver_input} is equivalent to {conversion} in tablespoons.")
  elif conversion_selection == "D":
    conver_input = int(input("Please input the value to be converted." ))
    conversion = round(tbsp_to_cups(conver_input))
    print(f"{conver_input} is equivalent to {conversion} in cups.")
  elif conversion_selection == "E":
    conver_input = int(input("Please input the value to be converted." ))
    conversion = round(lbs_to_kg(conver_input), 2)
    print(f"{conver_input} is equivalent to {conversion} in kilograms.")
  elif conversion_selection == "F":
    conver_input = int(input("Please input the value to be converted." ))
    conversion = round(kg_to_lbs(conver_input), 2)
    print(f"{conver_input} is equivalent to {conversion} in pounds.")
  elif conversion_selection == "G":
    conver_input = int(input("Please input the value to be converted." ))
    conversion = round(metresq_to_sqft(conver_input), 2)
    print(f"{conver_input} is equivalent to {conversion} in sq ft.")
  elif conversion_selection == "H":
    conver_input = int(input("Please input the value to be converted." ))
    conversion = round(sqft_to_metresq(conver_input), 2)
    print(f"{conver_input} is equivalent to {conversion} in metre squared.")
  else:
    print("Error: Letter not in list. Please enter a letter that corresponds with the conversion you wish.")
    conversion_function()


#Ask user name
name = input("Welcome to the Conversion. What is your name? ")

conversion_function()

import random

#Message to ask user if that is all they would like
is_all = input("Is this all you would like? Y for yes, N for a joke ").upper()

# Ending message
end_mesg = "Thanks for using Conversion!"

if is_all == "Y":
  print(end_mesg)
elif is_all == "N":
  print(random.choice(random_jokes))
  print(end_mesg)
else:
  print("Error: Letter not recognised")
  print(is_all)