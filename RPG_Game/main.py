import random, time, os, sys

# ----- Cinematic Functions -----
def delay(text, sec=0.8):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()
    time.sleep(sec)

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def cinematic(text):
    border = "="*len(text)
    delay(border,0.2)
    delay(text,0.5)
    delay(border,0.2)

def animated_attack(attacker, target, dmg):
    delay(f"\n💥 {attacker} strikes {target} for {dmg} damage!",0.5)

# ----- Player Setup -----
clear_screen()
cinematic("🌌 WELCOME TO THE CINEMATIC HAUNTED FOREST RPG 🌌")
name = input("Enter your hero's name: ")
player = {
    "name": name,
    "health": 150,
    "attack": 15,
    "defense": 7,
    "luck": 7,
    "mana": 30,
    "inventory": [],
    "gold": 0,
    "level": 1,
    "experience": 0
}

# ----- ASCII Bosses -----
dragon_phases = [
r"""
            __====-_  _-====___
          _--^^^#####//      \\
         -^##########// (    ) \\
        _/############//  |\^^/|  \\
       /#############((   \ 0 0 /))
       -###############\\  |--| //
      -#################\\  \/ //
     -###################\\   //
     _#/|##########/\######(  /
     |/ |#/\#/\#/\/  \#/\##\//
     `  |/  V  V  `   V  \#|
        `   `  `      `   `
""",
r"""
           __====-_  _-====___
         _--^^^#####//      \\
        -^##########// (o  o) \\
       _/############//  |\_O_/| \\
      /#############((   \  ^  /))
      -###############\\  |==| //
     -#################\\  \/ //
     _#/|##########/\######(  /
     |/ |#/\#/\#/\/  \#/\##\//
     `  |/  V  V  `   V  \#|
        `   `  `      `   `
""",
r"""
          __====-_  _-====___
        _--^^^#####//      \\
       -^##########// (X X) \\
      _/############//  |\_^_/| \\
     /#############((   \  °  /))
     -###############\\  |==| //
    -#################\\  \/ //
    _#/|##########/\######(  /
    |/ |#/\#/\#/\/  \#/\##\//
    `  |/  V  V  `   V  \#|
       `   `  `      `   `
"""
]

# ----- Cinematic Story -----
delay(f"\nBrave {player['name']}, the Haunted Forest awaits...")
delay("You will face monsters, traps, hidden treasures, and the Ancient Dragon itself...\n")

forest_map = [
    {"name":"Whispering Glade","enemy":"Forest Goblin","health":40,"attack":7},
    {"name":"Dark Cave","enemy":"Shadow Spider","health":55,"attack":10},
    {"name":"Ancient Tree","enemy":"Treant Guardian","health":80,"attack":12},
    {"name":"Mystic River","enemy":"Water Serpent","health":70,"attack":11},
    {"name":"Dragon's Lair","enemy":"Ancient Dragon","health":150,"attack":20}
]

# ----- Battle System -----
def battle(enemy_name, enemy_health, enemy_attack, boss=False):
    delay(f"\n⚔️ {enemy_name} appears!",0.5)
    if boss:
        for phase, art in enumerate(dragon_phases,1):
            print(art)
            delay(f"The Dragon evolves into Phase {phase}!",1)
            enemy_health += phase*20
            enemy_attack += phase*5
    while enemy_health>0 and player["health"]>0:
        delay(f"\nYour Health: {player['health']} | Mana: {player['mana']} | Enemy Health: {enemy_health}")
        action = input("Choose: attack / defend / special / combo / run: ").lower()
        if action=="attack":
            dmg=random.randint(player["attack"]-2,player["attack"]+5)
            enemy_health -= dmg
            animated_attack(player["name"],enemy_name,dmg)
        elif action=="defend":
            block=random.randint(5,10)
            player["health"]+=block
            delay(f"You defend and gain {block} health!")
        elif action=="special":
            if player["mana"]>=5:
                dmg=player["attack"]*2
                enemy_health-=dmg
                player["mana"]-=5
                delay(f"🔥 Special attack hits for {dmg}! Mana left {player['mana']}")
            else: delay("Not enough mana!")
        elif action=="combo":
            if "Legendary Sword" in player["inventory"] and player["mana"]>=8:
                dmg=player["attack"]*3
                enemy_health-=dmg
                player["mana"]-=8
                delay(f"💥 Combo attack deals {dmg}! Mana left {player['mana']}")
            else: delay("Combo failed! Need Legendary Sword & 8 mana")
        elif action=="run":
            if random.randint(1,10)<=player["luck"]:
                delay("You escaped successfully!")
                return True
            else:
                delay("Failed to escape!")
        # Enemy attacks
        if enemy_health>0:
            edmg=max(random.randint(enemy_attack-3,enemy_attack+2)-player["defense"],1)
            player["health"]-=edmg
            delay(f"{enemy_name} strikes for {edmg}! Your health: {player['health']}")
            if player["health"]<=0:
                delay("You have been defeated... Game Over 😢")
                return False
    # Loot
    loot=random.choice(["gold coin","healing potion","Legendary Sword","dragon scale"])
    player["inventory"].append(loot)
    if loot=="gold coin":
        gold=random.randint(50,150)
        player["gold"]+=gold
        delay(f"You found {gold} gold!")
    else:
        delay(f"You found {loot}!")
    return True

# ----- Adventure Loop -----
alive=True
for stage in forest_map:
    if not alive or player["health"]<=0: break
    delay(f"\n🌲 Stage: {stage['name']}")
    if stage["name"]=="Dragon's Lair":
        alive=battle(stage["enemy"],stage["health"],stage["attack"],boss=True)
    else:
        alive=battle(stage["enemy"],stage["health"],stage["attack"])
    if alive and stage["name"]!="Dragon's Lair":
        choice=input("Continue deeper or exit? (continue/exit): ").lower()
        if choice=="exit":
            delay("You exit safely. Adventure ends early."); break

# ----- Final Treasure -----
if alive:
    cinematic("🏰 You reach the LEGENDARY TREASURE CHAMBER!")
    player["gold"]+=500
    player["inventory"].append("Legendary Treasure")
    delay("💰 You claim the Legendary Treasure!")

# ----- Final Stats -----
cinematic(f"🎉 Adventure Complete! Hero: {player['name']}")
delay(f"Health: {player['health']}")
delay(f"Attack: {player['attack']}")
delay(f"Defense: {player['defense']}")
delay(f"Mana: {player['mana']}")
delay(f"Luck: {player['luck']}")
delay(f"Gold: {player['gold']}")
delay(f"Inventory: {player['inventory']}")
cinematic("🏆 THANK YOU FOR PLAYING THE CINEMATIC HAUNTED FOREST RPG 🏆")
