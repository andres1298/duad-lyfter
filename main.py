from pokedex import load_pokedex, get_evolution_chain

def show_menu():
    pokedex = load_pokedex()
    while True:
        print("\nPokémon Evolution Menu - 2025")
        print("1. List all Pokémon")
        print("2. Show evolution chain for a Pokémon number")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            for entry in pokedex:
                print(f"{entry['id']:3}: {entry['name']}")
        elif choice == "2":
            num_input = input("Enter Pokémon number (1-251): ").strip()
            if not num_input.isdigit():
                print("Please enter a valid number.")
                continue
            number = int(num_input)
            chain = get_evolution_chain(number, pokedex)
            if chain:
                print(" -> ".join(chain))
            else:
                print("Pokémon not found.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    show_menu()
