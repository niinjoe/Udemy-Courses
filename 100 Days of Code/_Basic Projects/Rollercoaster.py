print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?\n"))
bill=0
if height >=120:
  print("You can ride the rollercoaster!")
  age=int(input("What is your age?\n"))
  if age <12:
    bill=5
    print("Child tickets are $5.")
  elif age<=18:
    bill=7
    print("Teenagers tickets are $7.")
  elif age>=45 or age<=55:
    bill=0
  else:
    bill=12
    print("Adult tickets are $12.")
  photo=input("Do you want a photo taken? Type Y or N.\n")
  if photo=="Y":
    bill+=3
  print(f"You will have to pay a total of ${bill}.\nHave fun!")
else:
  print("Sorry, but you have to grow taller in order to ride.")
