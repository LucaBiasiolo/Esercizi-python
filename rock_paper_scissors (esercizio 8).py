print("Ciao, sono Python. Benvenuti al gioco Rock-Paper-Scissors");

while True:
    giocata1 = input("Giocatore 1, cosa vuoi giocare? Inserisci R-P-S: ");
    giocata2 = input("Giocatore 2, cosa vuoi giocare? inserisci R-P-S: ");

    if giocata1 not in ['R', 'P', 'S'] or giocata2 not in ['R', 'P', 'S']:
        print("Giocate non valide. Riprovare");
        continue;

    if giocata1 == giocata2: #tratto i 3 casi possibili di parità
        print("Parità");
    elif (giocata1 == 'R' and giocata2 == 'S') or (giocata1 == 'S' and giocata2 == 'P') or (giocata1 == 'P' and giocata2 == 'R'):
        #tratto i 3 casi in cui vince il giocatore 1
        print("Il giocatore 1 ha vinto. Complimenti!");
    else: #tratto i 3 casi in cui vince il giocatore 2
        print("Il giocatore 2 ha vinto. Complimenti!");

    giocareAncora = input("Volete giocare ancora? Y/N: ");
    if giocareAncora.upper() == 'N':
        break;
