from dbConnect import sessionLoader
from mapper import Ersatzteil
from mapper import Auftrag
from dbConn import getConn
from checker import handleInputInteger
#import datetime
from sqlalchemy import exc, or_

#conn=getConn()
#cursor=conn.cursor()

def getErsatzteile():
    session = sessionLoader() #Abruf der Daten

    ersatzteile = session.query(Ersatzteil).all()

  

    if len(ersatzteile)>0:
        for et in ersatzteile:
            print(f' {et.EtID}  -  {et.EtBezeichnung} - {et.EtPreis} - {et.EtAnzLager} - {et.EtHersteller}')     # Ausgabe Daten       
    else:
        print('Keine Ersatzteile vorhanden.')
        eingabe_EtID = 0
    print() 
    session.close()


