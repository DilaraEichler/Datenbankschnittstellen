from dbConnect import sessionLoader
from mapper import Ersatzteile
from dbConn import getConn
#from checker import handleInputInteger, handleInputDatum
#import datetime
from sqlalchemy import exc, or_

conn=getConn()
cursor=conn.cursor()

try:
    cursor.execute('SELECT EtID, EtBezeichnung, EtAnzLager FROM Ersatzteil')