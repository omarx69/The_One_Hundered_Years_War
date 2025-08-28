import random
class NPC:
    def __init__(self, gender, name):
        self.gender = gender
        self.name = gender


# Female medieval names
female_names = [
    "Adelaide", "Beatrice", "Cecilia", "Eleanor", "Isolde",
    "Matilda", "Rosalind", "Margery", "Clarissa", "Sibyl",
    "Christiana", "Aveline", "Emmeline", "Isabella", "Joan",
    "Agnes", "Alice", "Amice", "Constance", "Gisela",
    "Helena", "Juliana", "Lucia", "Melisende", "Philippa",
    "Rowena", "Seraphina", "Theodora", "Yolande", "Brunhild"
]

# Male medieval names
male_names = [
    "Alaric", "Baldwin", "Cedric", "Godfrey", "Leofric",
    "Oswald", "Roland", "Geoffrey", "Hugh", "William",
    "Richard", "Robert", "Edmund", "Harold", "Thomas",
    "Anselm", "Bartholomew", "Berengar", "Charles", "Eustace",
    "Frederick", "Gerard", "Hubert", "Lambert", "Louis",
    "Odo", "Percival", "Ranulf", "Simon", "Walter"
]


characters = [NPC(random.choice(["male", "female"]), random.choice(["male", "female"])) for _ in range(69)]

