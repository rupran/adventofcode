import copy

class Spell:
    def __init__(self, name, mana = 0, damage = 0, heal = 0, mana_restore = 0, armor = 0, turns = 0):
        self.name = name
        self.mana = mana
        self.damage = damage
        self.heal = heal
        self.mana_restore = mana_restore
        self.armor = armor
        self.turns = turns

    def __str__(self):
        return "%s: %d turns" % (self.name, self.turns)

    def __repr__(self):
        return self.__str__()

missile = Spell("missile", mana = 53, damage = 4)
drain = Spell("drain", mana = 73, damage = 2, heal = 2)
shield = Spell("shield", mana = 113, turns = 6, armor = 7)
poison = Spell("poison", mana = 173, turns = 6, damage = 3)
recharge = Spell("recharge", mana = 229, turns = 5, mana_restore = 101)

spells = [missile, drain, shield, poison, recharge]

boss_hp_in = 71
boss_dmg = 10
my_hp_in = 50
my_mana_in = 500
min_mana = 9999999

active_spells = []

def sim_step(my_hp, my_mana, boss_hp, mana_spent, active_spells, my_turn, depth = 0):
    global min_mana, boss_dmg

    # Hard mode
    #if my_turn:
    #    my_hp -= 1

    new_active_spells = copy.deepcopy(active_spells)
    for spell in new_active_spells[:]:
        my_hp += spell.heal
        my_mana += spell.mana_restore
        boss_hp -= spell.damage
        spell.turns -= 1
        if spell.turns == 0:
            new_active_spells.remove(spell)

    if boss_hp <= 0:
        if min_mana > mana_spent:
            min_mana = mana_spent
            print "Current min: " + str(min_mana)
        return

    if my_hp <= 0:
        return

    if mana_spent > min_mana:
        return

    if my_turn:
        for spell in spells:
            cur_active_spells = copy.deepcopy(new_active_spells)
            my_mana_cur = my_mana
            my_hp_cur = my_hp
            boss_hp_cur = boss_hp
            if my_mana_cur < spell.mana:
                continue
            if spell.name in [x.name for x in cur_active_spells]:
                continue
            if spell.name == "missile":
                boss_hp_cur -= spell.damage
            elif spell.name == "drain":
                boss_hp_cur -= spell.damage
                my_hp_cur += spell.heal
            else:
                 cur_active_spells.append(copy.deepcopy(spell))

            my_mana_cur -= spell.mana

            sim_step(my_hp_cur, my_mana_cur, boss_hp_cur, mana_spent + spell.mana, cur_active_spells, False, depth + 1)

    else:
        boss_damage = boss_dmg
        for spell in new_active_spells:
            boss_damage -= spell.armor
        if boss_damage < 0:
            boss_damage = 1

        new_hp = my_hp - boss_damage
        sim_step(new_hp, my_mana, boss_hp, mana_spent, new_active_spells, True, depth)
        

sim_step(my_hp_in, my_mana_in, boss_hp_in, 0, [], True) 
print min_mana
