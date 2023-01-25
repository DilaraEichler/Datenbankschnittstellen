from checker import handleInputInteger
from logicNiederlassung import getNiederlassung
from logicMitarbeiter import getMitarbeiter
from logicErsatzteil import getErsatzteil
from logicMontage import getMontage, bMontage
from logicAuftrag import getAuftrag, anlegenAuftrag, planenAuftrag, buchenAuftrag

# Aufruf der Ablauflogik
while True:
    print('')
    print('1 - Daten anzeigen')
    print('2 - Neuen Auftrag anlegen')
    print('3 - Auftrag planen')
    print('4 - Ersatzteil anzeigen')
    print('5 - Erledigung geplanter Auftrag buchen')
    wastun = handleInputInteger('Aktion wählen')
    print()
    
    if wastun == 1:
        nlnr = getNiederlassung()            # Niederlassung aus Niederlassungsliste auswählen
        while nlnr > 0:
            print()
            mitnr = getMitarbeiter(nlnr)     # Mitarbeiter aus Mitarbeiterliste auswählen
            while mitnr > 0:
                print()
                aufnr = getAuftrag(mitnr)            # Aufträge des Mitarbeiters anzeigen
                while aufnr > 0:
                    print()
                    getMontage(aufnr)
                    aufnr = getAuftrag(mitnr) 
                mitnr = getMitarbeiter(nlnr) # neuen Mitarbeiter aus Mitarbeiterliste auswählen
            nlnr = getNiederlassung()        # neue Niederlassung aus Niederlassungsliste auswählen

    elif wastun == 2:
        print('Daten einfügen')
        anlegenAuftrag()
        
    elif wastun == 3:
        print('Auftrag planen')
        planenAuftrag()
    
    elif wastun == 4:
        getErsatzteil()
    
    elif wastun == 5:
        aufnr1 = buchenAuftrag()
        while aufnr1 > 0:
            print()
            aufnr2 =getMontage(aufnr1)
            while aufnr2 > 0:
                print()
                bMontage(aufnr2)
                aufnr2 =getMontage(aufnr1)
            aufnr1 = buchenAuftrag()
    
    else:
        break