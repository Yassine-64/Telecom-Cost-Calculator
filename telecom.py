def calc_cout(duree):
    cout_abo = [200, 100, 50, 20, 0]
    min_gratuites = [float('inf'), 120, 60, 30, 0]
    cout_min = [0, 0.5, 1, 1.5, 2]

    couts_mensuels = []

    for i in range(5):
        min_supplement = max(duree - min_gratuites[i], 0)
        cout_total = cout_abo[i] + (min_supplement * cout_min[i])
        couts_mensuels.append(cout_total)

    return couts_mensuels

while True:
    print("Menu:")
    print("1- Afficher la liste des coûts mensuels par offre")
    print("2- Afficher l'offre la plus avantageuse (coût le plus bas)")
    print("3- Quitter le programme")

    choix = input("Choisissez une option: ")

    if choix == "1":
        duree = input("Entrez la durée de communication en minutes: ")
        if duree.isdigit():
            duree = int(duree)
            prix = calc_cout(duree)
            for i in range(len(prix)):
                print(f"Coût mensuel pour l'offre {i + 1}: {prix[i]} DH")

    elif choix == "2":
        duree = input("Entrez la durée de communication en minutes: ")
        if duree.isdigit():
            duree = int(duree)
            prix = calc_cout(duree)
            min_val = min(prix)
            offre_avant = prix.index(min_val) + 1
            print(f"L'offre la plus avantageuse est l'offre {offre_avant} avec un coût de {min_val} DH")

    elif choix == "3":
        print("Fin du programme.")
        break
