# Decorador para usar Cowsay con cualquier texto (a 1 línea)

from datetime import date, datetime

def cowsay(func):
    def wrapper(text):
        lenght = len(text)
        print(" _" + lenght*"_" + "_ ")
        print("< " + text + " > ")
        print(" -" + lenght*"-" + "- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print("            (__)\       )\/\ ")
        print("                ||----w | ")
        print("                ||     || ")
    return wrapper

@cowsay
def mytext(text):
        print(text)

mytext("No pares de aprender!")