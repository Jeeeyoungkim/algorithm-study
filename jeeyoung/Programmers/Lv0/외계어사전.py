def solution(spell, dic):
    spell_num = 0
    
    for word in dic:    
        visited_spell = spell[:]
        for char in word:
            if char in visited_spell:
                visited_spell.remove(char)
        if len(visited_spell) == 0:
            spell_num += 1
    
    return 1 if spell_num > 0 else 2