def verification():
    import random
    print("Please confirm you're a human before continuing")
    n = random.choice(
        [
            "3467y59?",
            "8439r88",
            "739h930",
            "8e83002",
            "7299f9",
            "139j888",
            "6o0820",
            "i6980",
            "029s012",
            "92j012",
            "92u993",
            "8031w02",
        ]
    )
    try:
        I = str(input(f"What is the letter in {n} "))
        if n == "3467y59?":
            if I == "y":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        elif n == "8439r88":
            if I == "r":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        elif n == "739h930":
            if I == "h":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        elif n == "8e83002":
            if I == "e":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        elif n == "7299f9":
            if I == "f":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        elif n == "139j888":
            if I == "j":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        elif n == "6o0820":
            if I == "o":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        elif n == "i6980":
            if I == "i":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        elif n == "029s012":
            if I == "s":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        elif n == "92j012":
            if I == "j":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        elif n == "92u993":
            if I == "u":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        elif n == "8031w02":
            if I == "w":
                print("Verification completed")
            else:
                print("Verification failed. Try again later")
                verification()
        else:
            print("Error: Your choice not found")
            verification()
    except:
        print("Error: Your choice not found")
        verification()
