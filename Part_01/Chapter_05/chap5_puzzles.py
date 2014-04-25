
# Chapter 5 Programming Puzzels

# 1 Are you rich?

money = 2000
if money > 1000:
    print("I am rich!!")
else:
    print("I'm not rich!!")
    print("But I might be later...")

# 2 Twinkies!

twinkies = 600
if twinkies < 100:
    print("Too few twinkeies")
elif twinkies > 500:
    print("Too many twinkeies")

# Just the right number

money = 500
if money == 100 or money == 500 or money == 1000 or money == 5000:
    print("Money is " + str(money))

# I can fight those Ninjas

ninjas = 5
if ninjas < 10:
    print("I can fight those Ninjas!")
elif ninjas < 30:
    print("It'll be a struggle, but I can take'em ")
elif ninjas < 50:
    print("That's too many")