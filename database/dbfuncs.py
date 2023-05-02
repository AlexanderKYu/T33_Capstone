import psycopg2
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(path.dirname(__file__)))
load_dotenv(path.join(basedir, '.env'))

def db_connection():
    """Establishing a connection with the database.
    This will return a connection and a cursor variable"""
    conn = ""
    cursor = ""
    try:
        conn = psycopg2.connect(
            database=environ.get('DATABASE'),
            user=environ.get('DBUSER'),
            password=environ.get('PASSWORD'),
            host=environ.get('HOST'),
            port=environ.get('PORT'),
            connect_timeout=3,
        )
        cursor = conn.cursor()
        conn.autocommit = True
    except:
        print("Unable to connect to database.")
    return conn, cursor

def closeDBConnection(conn):
    """Given a connection this function 
    will close the connection"""
    try:
        conn.close()
    except:
        print("Unable to close database connection.")
        return False
    return True

def db_init(cursor):
    """A function that will initialize the database to ensure
    needed tables and data exist before executing functions"""
    db_query = """CREATE TABLE IF NOT EXISTS tblOrders (
    WIP INT NOT NULL,
    QTY INT NOT NULL,
    TagID VARCHAR(6),
    InProd BOOLEAN,
    t_start FLOAT,
    t_end FLOAT,
    time_on_floor FLOAT,
    build_time FLOAT,
    LastZone INT,
    ZoneName VARCHAR(50)
    )"""

    cursor.execute(db_query)


    db_query = """CREATE TABLE IF NOT EXISTS tblPaths (
    WIP INT NOT NULL,
    QTY INT NOT NULL,
    TagID VARCHAR(6),
    ZoneID INT,
    ZoneName VARCHAR(50),
    Time FLOAT
    )"""

    cursor.execute(db_query)


    db_query = """CREATE TABLE IF NOT EXISTS tblRawLocations (
    WIP INT NOT NULL,
    QTY INT NOT NULL,
    TagID VARCHAR(6),
    Timestamp FLOAT,
    x FLOAT,
    y FLOAT,
    ZoneID INT
    )"""
    
    cursor.execute(db_query)

    db_query = """CREATE TABLE IF NOT EXISTS tblZoneDef (
    ZoneID SERIAL PRIMARY KEY NOT NULL,
    ZoneName VARCHAR(50) NOT NULL,
    x_lower FLOAT NOT NULL,
    x_upper FLOAT NOT NULL,
    y_lower FLOAT NOT NULL,
    y_upper FLOAT NOT NULL,
    ActiveZone BOOLEAN NOT NULL
    );"""

    cursor.execute(db_query)

def define_hard_zones(cursor):
    """Initialized the hard coded initial zones of the production floor"""
    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('No Zone', 0, 0, 0 , 0,True);"""

    cursor.execute(db_query)
    
    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Repairs', 0, 24, 69, 100, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Missing Components', 1, 21, 34, 56, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Color Quarter Re-Order', 11, 32, 16, 26, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Special Assembly', 23, 44, 77, 100, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Special Assembly Stitching', 44.5, 59, 77, 100, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Assembly', 23, 44, 64, 77, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Final Assembly', 44, 59, 64, 77, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('On the Line 2', 25, 44, 26, 63, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Cleaning 2', 21, 34, 26, 37, True);"""
    
    cursor.execute(db_query)
    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Runners', 31, 59, 0, 16, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Lasting', 60, 76, 85, 100, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Tacking', 60, 76, 70, 85, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Outsole', 77, 89, 63, 100, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Liner', 60, 77, 49, 70, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Blade', 76, 89, 51, 63, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Tongue Assembly', 59, 75, 28, 49, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Cleaning 1', 76, 89, 40, 50, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Inspection', 76, 89, 29, 40, True);"""
    
    cursor.execute(db_query)

    db_query = """INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone)
    VALUES ('Pacing', 60, 89, 17, 28, True);"""
    
    cursor.execute(db_query)

def delete_all(cursor):
    """THIS FUNCTION SHOULD NOT BE USED UNLESS NEEDED.
    Function to delete all the existing tables."""
    db_query = "DROP TABLE IF EXISTS tblOrders"

    cursor.execute(db_query)

    db_query = "DROP TABLE IF EXISTS tblPaths"

    cursor.execute(db_query)

    db_query = "DROP TABLE IF EXISTS tblRawLocations"

    cursor.execute(db_query)

    db_query = "DROP TABLE IF EXISTS tblZoneDef"

    cursor.execute(db_query)

def dbPushTblOrders(cursor, WIP, QTY, tagID, inProd, t_start, t_end, time_on_floor, build_time, lastZone, zoneName):
    """Function to insert data into the tblOrders table"""
    db_query = f"""INSERT INTO tblOrders (
    {WIP}, {QTY}, '{tagID},' {inProd}, {t_start}, {t_end}, {time_on_floor}, {build_time}, {lastZone}, {zoneName} 
    );"""
    cursor.execute(db_query)

def dbPushTblPaths(cursor, WIP, QTY, tagID, zoneID, zoneName, time):
    """Function to insert data into the tblPaths table"""
    db_query = f"""INSERT INTO tblPaths (
    {WIP}, {QTY}, '{tagID}', {zoneID}, '{zoneName}', {time}
    );"""

    cursor.execute(db_query)


def dbPushTblRawLocations(cursor, WIP, QTY, tagID, timestamp, x, y, zoneID):
    """Function to insert data into the tblRawLocations table"""
    db_query = f"""INSERT INTO tblRawLocations (WIP, QTY, tagID, timestamp, x, y, zoneID)
    VALUES ({WIP}, {QTY}, '{tagID}', {timestamp}, {x}, {y}, {zoneID});"""
    cursor.execute(db_query)

# def getActiveTimes(cursor):
#    """Function to get all the entires where sample movement is over 9.8.
#    This function is deprecated and is not needed in production"""
#    db_query = """SELECT loctime FROM tag_threshold
#                  WHERE overallx > 9.8 OR overally > 9.8 OR overallz > 9.8;"""
#    cursor.execute(db_query)

#    data = cursor.fetchall()
#    return data

def getActiveZones(cursor):
    """Function to get all the active zones that are being used"""
    db_query = """SELECT * FROM tblzonedef WHERE activezone = true;"""

    cursor.execute(db_query)

    data = cursor.fetchall()
    
    return data

def getActiveTagZones(cursor, x, y):
    """Function to determine which zone a tag is in based on its coordinates"""
    db_query = f"""SELECT * FROM tblzonedef 
    WHERE activezone = true AND tblzonedef.x_lower <= {x} AND tblzonedef.x_upper >= {x} 
    AND tblzonedef.y_lower <= {y} AND tblzonedef.y_upper >= {y};"""
    
    cursor.execute(db_query)

    data = cursor.fetchall()
    if len(data) == 1:
        return data[0]
    else:
        return (1, 'No Zone', 0, 0, 0, 0)


def dbPushZoneDef(cursor, ZoneName, x_lower, x_upper, y_lower, y_upper):
    """Function to 'upsert' zoning information"""
    db_update_query = f"""UPDATE tblZoneDef SET ActiveZone = False WHERE ZoneName = '{ZoneName}'"""
    cursor.execute(db_update_query)

    db_insert_query = f"""INSERT INTO tblZoneDef (ZoneName, x_lower, x_upper, y_lower, y_upper, ActiveZone) 
    VALUES ('{ZoneName}', {x_lower}, {x_upper}, {y_lower}, {y_upper}, True)"""
    cursor.execute(db_insert_query)


def disableZoneDef(cursor, ZoneName):
    """Function to disable a zone definition"""
    db_update_query = f"""UPDATE tblZoneDef SET ActiveZone = False WHERE ZoneName = '{ZoneName}'"""
    cursor.execute(db_update_query)
