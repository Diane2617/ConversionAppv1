import imp
import random

if __name__=="__main__":

  def f_to_c(f_temp):
    c_temp = round((f_temp - 32) * 5/9, 2)
    print(f"{f_temp} is equivalent to {c_temp} in celcius.")

  #f100_in_celsius = f_to_c(100)

  def c_to_f(c_temp):
    f_temp = round(c_temp * (9/5) + 32, 2)
    print(f"{c_temp} is equivalent to {f_temp} in fahrenheit")

  #Function for converting cups to tablespoons

  def cup_to_tbsp(cup):
    tbsp = cup * 16
    print(f"{cup} is equivalent to {tbsp} in tablespoons.")

  # Function for converting tablespoons to cups

  def tbsp_to_cups(tbsp):
    cup = tbsp / 16
    print(f"{tbsp} is equivalent to {cup} in cups.")

  # Convert lbs to kg

  def lbs_to_kg(lbs):
    kilogram = round(lbs / 2.205, 2)
    print(f"{lbs} is equivalent to {kilogram} in kilograms.") 

  # Convert kg to lbs

  def kg_to_lbs(kg):
    pounds = round(kg * 2.205, 2)
    print(f"{kg} is equivalent to {pounds} in pounds.")

  # Convert metre squared to square foot

  def metresq_to_sqft(mtre):
    sqft = mtre * 10.764
    print(f"{mtre} is equivalent to {sqft} in sq ft.")

  # Convert square foot to metre squared

  def sqft_to_metresq(sqft):
    metresq = sqft / 10.764
    print(f"{sqft} is equivalent to {metresq} in metre squared.")

# Random Jokes

random_jokes = ["I'm not cold, just chilli", "Why was the math teacher suspicious of all the prime numbers? Because they were all odd.", "How does a mathematician plow a field? He uses a pro-tractor."]

conversion_selections = {"A": "Fahrenheit to celcius", "B": "Celcius to fahrenheit", "C": "Cups to tablespoons", "D" : "Tablespoons to cups",
  "E": "Pounds to kilograms", "F": "Kilograms to pounds", "G": "Metre squared to square foot", "H":"Square foot to metre squared"}

def conversion_function():
   # Ask user to select what type of conversion would like to
  #have done
  conversion_selection = input(f""" 
  Hi {name}. Type in the letter that corresponds with
  the conversion you would like to do? {conversion_selections.items()}""" ).upper()

# Message requesting value to be converted

  conver_value = int(input("Please input the value to be converted" ))

  if conversion_selection == "A":
    f_to_c(conver_value)
  elif conversion_selection == "B":
    c_to_f(conver_value) 
  elif conversion_selection == "C":
    cup_to_tbsp(conver_value)
  elif conversion_selection == "D":
    tbsp_to_cups(conver_value)
  elif conversion_selection == "E":
    lbs_to_kg(conver_value)
  elif conversion_selection == "F":
    kg_to_lbs(conver_value)
  elif conversion_selection == "G":
    metresq_to_sqft(conver_value)
  elif conversion_selection == "H":
    sqft_to_metresq(conver_value)
  else:
    print("Error: Letter not in list. Please enter a letter that corresponds with the conversion you wish.")
    conversion_function()

#Message to ask user if that is all they would like
def end_message_function():
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
    end_message_function()


#Ask user name
name = input("Welcome to the Conversion. What is your name? ")

conversion_function()

end_message_function()





