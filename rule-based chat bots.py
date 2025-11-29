import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Himalayas", "Swiss Alps", "Rocky Mountains"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = {
    "Why don't programmers like nature? Too many bugs!"
}