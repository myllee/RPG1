from attribute import Attribute

class Character:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.attributes = self._initiali_attributes()

    def _initiali_attributes(self):
        attributes = {
            'Força': Attribute('Força', 0),
            'Destreza': Attribute('Destreza', 0),
            'Constituição': Attribute('Constituição', 0),
            'Sabedoria': Attribute('Sabedoria', 0),
            'Inteligência': Attribute('Inteligência', 0),
            'Carisma': Attribute('Carisma', 0)
        }
        
        for attr in attributes.values():
            attr.value = Attribute.random_value()
        
        race_bonuses = {
            'Dwarf': {'Constituição': 2},
            'Hill Dwarf': {'Sabedoria': 1},
            'Mountain Dwarf': {'Força': 2},
            'Elf': {'Destreza': 2},
            'High Elf': {'Inteligência': 1},
            'Wood Elf': {'Sabedoria': 1},
            'Dark Elf': {'Carisma': 1},
            'Barbarian': {'Destreza': 2},
            'Lightfoot': {'Carisma': 1},
            'Stout': {'Constituição': 1},
            'Human': {attr: 1 for attr in attributes.keys()},
            'Dragonborn': {'Força': 2, 'Carisma': 1},
            'Gnome': {'Inteligência': 2},
            'Forest Gnome': {'Destreza': 1},
            'Rock Gnome': {'Constituição': 1},
            'Tiefling': {'Inteligência': 1, 'Carisma': 2}
        }
        
        if self.race in race_bonuses:
            for attr, bonus in race_bonuses[self.race].items():
                attributes[attr].value += bonus
        
        return attributes

    def get_attribute_status(self, attr_name):
        attr_value = self.attributes[attr_name].value

        status_mapping = {
            'Força': {
                0: 'Incorpóreo', 
                1: 'Incapaz',
                5: 'Incapaz',
                9: 'Fraco',
                11: 'Mediano',
                15: 'Forte',
                20: 'Super Poderoso',
                float('inf'): 'Imbatível'
            },
            'Destreza': {
                0: 'Desacordado',
                1: 'Abatido',
                5: 'Abatido',
                9: 'Desajeitado',
                11: 'Regular',
                15: 'Ágil',
                20: 'Ninja',
                float('inf'): 'Imperceptível'
            },
            'Constituição': {
                0: 'Espectro',
                1: 'Enfermo',
                5: 'Enfermo',
                9: 'Frágil',
                11: 'Saudável',
                15: 'Durão',
                20: 'Super resistente',
                float('inf'): 'Imortal'
            },
            'Sabedoria': {
                0: 'Inconsciente',
                1: 'Irracional',
                5: 'Irracional',
                9: 'Desatento',
                11: 'Simples',
                15: 'Perspicaz',
                20: 'Filósofo',
                float('inf'): 'Iluminado'
            },
            'Inteligência': {
                0: 'Inanimado',
                1: 'Incivilizado',
                5: 'Incivilizado',
                9: 'Parvo',
                11: 'Medíocre',
                15: 'Estuado',
                20: 'Gênio',
                float('inf'): 'Onisciente'
            },
            'Carisma': {
                0: 'Aberração',
                1: 'Inexpressivo',
                5: 'Inexpressivo',
                9: 'Rude',
                11: 'Sociável',
                15: 'Persuasivo',
                20: 'Influente',
                float('inf'): 'Ídolo'
            }
        }

        for threshold, status in status_mapping[attr_name].items():
            if attr_value <= threshold:
                return status

    def __str__(self):
        return f"{self.name} ({self.race}): {', '.join([f'{attr.name}: {attr.value} ({self.get_attribute_status(attr.name)})' for attr in self.attributes.values()])}"
