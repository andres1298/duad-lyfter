import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("pokedex.json")

def load_pokedex():
    """Load pokedex data from the bundled JSON file. Reference the JSON in the repo."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_evolution_chain(number, pokedex):
    """Return the evolution chain for the given Pokédex number."""
    for entry in pokedex:
        if entry["id"] == number:
            return entry["evolution_chain"]
    return None
