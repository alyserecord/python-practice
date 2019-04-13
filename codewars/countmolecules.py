def parse_molecule (formula):
    formula.split('(',')','{','}','[',']')
    return formula


def equals_atomically (obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for k in obj1:
        if obj1[k] != obj2[k]:
            return False
    return True
                
#(equals_atomically(parse_molecule("H2O"), {'H': 2, 'O' : 1}), "Should parse water")
#(equals_atomically(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O' : 2, 'H': 2}), "Should parse magnesium hydroxide: Mg(OH)2")
#(equals_atomically(parse_molecule("K4[ON(SO3)2]2"), {'K': 4,  'O': 14,  'N': 2,  'S': 4}), "Should parse Fremy's salt: K4[ON(SO3)2]2")