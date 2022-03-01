SELECT schueler.vorname, schueler.nachname
FROM schueler
    JOIN schuelerKurs
    ON schueler.SID = schuelerKurs.SID
    JOIN kurse
    ON schuelerKurs.name = kurse.name AND schuelerKurs.stufe = kurse.stufe
WHERE kurse.name = "M-L2";