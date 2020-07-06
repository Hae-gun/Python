# 12.1.1
lux = {'health':490, 'mana':334, 'melle':550,'armor':18.72}
print(lux)
lux = {'health': 490, 'mana': 334, 'melle': 550, 'armor': 18.72, 'health':800}
lux['health']
x = {100:'hundred', False:0,3.5:[3.5,3.5]}
# 12.1.2
x = {[10,20]:100}
x = {{'a':10}:10}
# 12.1.3
x = {}
y = dict()

# 12.1.4
lux1 = dict(health=490, mana=334, melle=550, armor=18.72)
lux2 = dict(zip(['health','mana','melee', 'armor'],[490,334,550,18.72]))
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})

# 12.2
lux['health']

# 12.2.1
lux = {'health': 490, 'mana': 334, 'melle': 550, 'armor': 18.72, 'health':800}
lux['health'] = 2037
lux['mana'] = 1184
lux['asdf']

# 12.2.2
'health' in lux
'attack_speed' not in lux

# 12.2.3
lux = {'health': 490, 'mana': 334, 'melle': 550, 'armor': 18.72, 'health':800}
len(lux)
