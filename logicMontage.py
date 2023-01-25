from dbConnect import sessionLoader
from mapper import Auftrag, Ersatzteil, Montage
from checker import handleInputInteger
from sqlalchemy import exc, or_

def getMontage(p_aufnr):

    session = sessionLoader()
    auftrag = session.query(Auftrag).get(p_aufnr)


    if isinstance(auftrag, type(None)):
        print(f'Auftrag mit der AufNr: {p_aufnr} existiert nicht in der Datenbank.')
        session.close()
        return 0
        
    if len(auftrag.ListeMontage) > 0:
        liste_mo = [0]    
        for mo in auftrag.ListeMontage:
            print(f' {mo.EtID} - {mo.Ersatzteil.EtBezeichnung} - {mo.Anzahl}')  
            liste_mo.append(mo.EtID)                    
        print()
                            
    else:
        print('Es gibt keine Ersatzteil in dieser Auftrag')
        # eingabe_EtID = 0

    print()
    P_Enter = handleInputInteger('Drücken Sie die Eingabetaste für weiter')

    session.close()
    return p_aufnr

def bMontage(p_aufnr):

    session = sessionLoader()
    menge_et = session.query(Ersatzteil).all()  
    
    print('Ersatzteil: ')
    if len(menge_et)>0:
        liste_et = [0] 
        for et in menge_et:
            print(f' {et.EtID}  -  {et.EtBezeichnung} - {et.EtPreis} - {et.EtAnzLager} - {et.EtHersteller}')
            liste_et.append(et.EtID)     
        print()

        eingabe_EtID = None
        while eingabe_EtID not in liste_et:
            eingabe_EtID = input('EtID:')
        
        eingabe_anzahl = handleInputInteger('Anzahl')
        montage = Montage(EtID = eingabe_EtID, AufNr = p_aufnr, Anzahl = eingabe_anzahl)
        try:
            session.add(montage)
            session.commit()
            print()
            print('Neuer Ersatzteil für diese Montage angelegt.')
            print(f'EtID: {eingabe_EtID} - AufNr: {p_aufnr} - Anzahl: {eingabe_anzahl} ')
            print()
        except exc.SQLAlchemyError():
            print('Fehler - Montage einfügen')
            session.close()
            return
    
    else:
        print('Keine Ersatzteil in der DB.')
        menge_et = 0
        
    session.close()