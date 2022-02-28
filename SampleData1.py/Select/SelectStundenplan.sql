SELECT schueler.vorname, kurse.name, stunden.tag, stunden.vonS, stunden.bisS
FROM schueler 
    JOIN schuelerKurs
    ON schuelerKurs.SID = schueler.SID
    JOIN kurse 
    ON schuelerKurs.name = kurse.name AND schuelerKurs.stufe = kurse.stufe
    JOIN stundenKurs
    ON kurse.name = stundenKurs.name
    JOIN stunden
    ON stundenKurs.StId = stunden.StId
WHERE schueler.vorname = "Henry" ORDER BY stunden.tag;