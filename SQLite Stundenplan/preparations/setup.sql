CREATE TABLE IF NOT EXISTS schueler (
    SID INT PRIMARY KEY  ,
    vorname VARCHAR (100) ,
    nachname VARCHAR (100) ,
    stufe VARCHAR (2)
);

CREATE TABLE IF NOT EXISTS stunden (
    StId INT  PRIMARY KEY ,
    vonS INT ,
    bisS INT ,
    tag INT ,
    oft INT
);

CREATE TABLE IF NOT EXISTS lehrer (
    short VARCHAR (3) PRIMARY KEY ,
    vorname VARCHAR (100) ,
    nachname VARCHAR (100)
);

CREATE TABLE IF NOT EXISTS kurse (
    name VARCHAR (10) ,
    stufe VARCHAR (2) ,
    fach VARCHAR (50) ,
    art VARCHAR (30) ,
    nummer INT ,
    raum VARCHAR (10) ,
    lShort VARCHAR (3) ,
    PRIMARY KEY ( name , stufe ) ,
    FOREIGN KEY ( lShort ) REFERENCES lehrer ( short )
);

CREATE TABLE IF NOT EXISTS stundenKurs (
    name VARCHAR (10) ,
    stufe VARCHAR (2) ,
    StId INT ,
    PRIMARY KEY ( name , stufe , StId ) ,
    FOREIGN KEY ( name , stufe ) REFERENCES kurse ( name , stufe ) ,
    FOREIGN KEY ( StId ) REFERENCES stunden ( StId )
);

CREATE TABLE IF NOT EXISTS schuelerKurs (
    SID INT ,
    name VARCHAR (10) ,
    stufe VARCHAR (2) ,
    PRIMARY KEY ( SID , name , stufe ) ,
    FOREIGN KEY ( name , stufe ) REFERENCES kurse ( name , stufe ) ,
    FOREIGN KEY ( SID ) REFERENCES schueler ( SID )
);