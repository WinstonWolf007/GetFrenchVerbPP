from FrenchVerb import get_pp_french_verb


while True:
    print("\n--------\n")
    verb = input("Verbe à l'infinitif: ")

    if verb == "exit":
        break

    print("Version Participe:")

    print("\t* " + "\n\t* ".join(get_pp_french_verb(verb)))

