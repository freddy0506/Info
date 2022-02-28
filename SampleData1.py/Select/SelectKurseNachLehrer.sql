SELECT kurse.name 
FROM lehrer
    JOIN kurse
    ON lehrer.short = kurse.lShort
WHERE lehrer.vorname = "Paula";