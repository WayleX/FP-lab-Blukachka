import new_game
# creating locations
levandivka = new_game.Room("Levandivka")
levandivka.set_description("Dirty and dangerous. Shouldn't be visited in a nighttime")
syhiv = new_game.Room("Syhiv")
syhiv.set_description("A lot of people and Shuvar nearby")

center = new_game.Room("City center")
center.set_description("Nice and pretty. A lot of abilities")
# linking locations
syhiv.link_room(levandivka, "by 18 bus")
levandivka.link_room(syhiv, "by 18 bus")
center.link_room(syhiv, "by 4 tram")
syhiv.link_room(center, "by 4 tram")
# creating characters

misha = new_game.Enemy("Misha", "Regular bully, should be avoided")
misha.set_conversation("What's up, dude")
misha.set_weakness("Vodka")
levandivka.set_character(misha)

nazar = new_game.Allie('Nazar', 'Your school friend. Was always nice to you and helped every time')
nazar.set_conversation('Hi, haven`t seen you for ages')
syhiv.set_character(nazar)

roman = new_game.Allie('Roman', 'Your college who was at party and owes you a lot of money')
roman.set_conversation('Oh, good morning, I guess')
center.set_character(roman)
# creating items
ploskivska = new_game.Item("Ploskivska")
ploskivska.set_description("An aqua vitae itself")
nazar.set_item(ploskivska)

vodka = new_game.Item("Vodka")
vodka.set_description("A good bottle of Nemiroff")
roman.set_item(vodka)

current_location = levandivka
backpack = []
# beginning condition
lose = False
drunk = True
keys = False
print('You were partying all night and now you ended up on Levandovka')
print('You have a huge hangover and lost your keys')
print('Try to get rid of hangover and find your keys to go home')
print(
    '//Possible interactions: ["by 4 tram","by 18 bus", "ask for help", "fight","negotiate","talk" ]//')
while lose == False:
    print("\n")\
        # win condition
    if drunk == False and keys == True:
        print('You won')
        print('Now you can sleep peacefully')
        break
    # current information
    current_location.get_details()
    if drunk:
        print('You still have hangover')
    inhabitant = current_location.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    item = None
    if inhabitant is not misha:
        item = inhabitant.get_item()
    command = input("> ")
    # check for input
    if command in ['by 4 tram', 'by 18 bus']:
        # Move in the given direction
        current_location = current_location.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        # force a fight
        if current_location != levandivka:
            print("There is no one here to fight with")
        else:
            print('Misha knocked out you')
            print('You ended up in a hospital')
            lose = True
            print('Game over')
    elif command == "negotiate":
        # try to negotiate
        if current_location != levandivka:
            print("Better ask for help")
        else:
            if vodka in backpack:
                print('[Misha says] One bottle of vodka and it will be a deal')
                print('You traded bottle of vodka for keys')
                keys = True
            else:
                print('If only you had vodka')
                print('Misha knocked out you')
                print('You ended up in a hospital')
                lose = True
                print('Game over')
    elif command == "ask for help":
        # asking for help interaction
        if item is not None:
            print("You politely asked for help")
            item.describe()
            obj = inhabitant.get_item()
            if obj.name == 'Vodka':
                backpack.append(vodka)
                print('You have vodka in your backpack')
            if obj.name == 'Ploskivska':
                print('Unbelievable taste. Now you feel much better')
                drunk = False
            inhabitant.set_item(None)
        else:
            print("There's nothing more to ask!")
    else:
        print("I don't know how to " + command)
