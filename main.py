from character import Character

print("OLÁ GUERREIRO, SEJA BEM VINDO AO NOSSO PRIMEIRO JOGO PROGRAMADO EM PYTHON, VAMOS COMEÇAR A CRIAR NOSSOS PERSONAGENS??")
print("ESPERO QUE SE DIVIRTA MUITO CRIANDO PERSONAGENS ÚNICOS!")

def main():
    name = input("ROLE OS DADOS E VAMOS VER QUAL SERÁ O NOME DE NOSSO PERSONAGEM: ")
    race = input("NOSSA ! LINDO NOME...AGORA VAMOS ESCOLHER A RAÇA (Dwarf, Hill Dwarf, Mountain Dwarf, Elf, High Elf, Wood Elf, Dark Elf, Barbarian, Lightfoot, Stout, Human, Dragonborn, Gnome, Forest Gnome, Rock Gnome, Tiefling): ")
    character = Character(name, race)
    print(character)

if __name__ == "__main__":
    main()