print("What's your favorite sport?")
sport = input()

if sport == "lacrosse":
    print("That's my favorite too!")
elif sport == "soccer" :
    print ("I'm not very good, but I'm practicing.")
elif sport == "field hockey":
    print ("I play mid-field.")
else:
    print (sport + "sounds fun.")
      

print ("What's your favorite TV show")
show = input().title()

if show == "90210":
       print ("It's so good right!")
elif show == "Gossip Girl":
       print ("That show is so good!")
elif show == "Riverdale":
       print ("I just finished Season 1!")
else:
       print ("i haven't watched " + show)

print ("What's your favorite book?")
book = input().title()
if "Harry Potter" in book:
    print ("JK Rowling is the best!")

print ("What's your favorite dessert?")
dessert = input ().title()
if "chocolate ice cream" in dessert:
    print ("I love chocolate, but mint chip is my favorite")

myrestaurants = {"Tengda", "Terra", "Meli Melo", "Garden Catering", "Pizza Post"}
myfavfoods = {"pizza", "spaghetti bolognese", "crepes", "chicken and cones"}

print ("What is your favorite restaurant?")
food = input ()

if food in myrestaurants:
    print ("I love eating at " + food)

    print ("What do you like to eat there?")
    favfood = input ()
if favfood in myfavfoods:
    print ("Delicious!")







    
