from prettytable import PrettyTable

if __name__ == '__main__':
    table = PrettyTable()
    table.add_column("Pokémon name", ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"])
    table.add_column("Type", ["Electric", "Fire", "Water", "Grass"])
    print(table)