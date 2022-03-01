Datenbank zur Schulkursbelegung - README.txt

Es sollten sich 3 weitere Dateien in diesem Ordner:
	schueler.db
	select.py
	requirements.txt
	
schueler.db
	Dies ist die Datenbank in der die Schulkursbelegung gespeichert wird. Diese kann mit Hilfe des scriptes setup.py in preparations wiederhergestellt werden.

select.py
	Um diese Script auszuführen und die UI zu starten ist es nötig die Programmiertsprache Python3 und die in requirements.txt aufgelisteten Bibeljotheken für diese Version zu installiern.
	Dies funktioniert mit dem Befehl:	pip3 install -r requirements.txt
	Dieser muss in diesem Ordner ausgeführt werden.

	Alternativ ist es natürlich auch möglich die Bibeljotheken einzeln zu installieren:	pip3 install <Bibeljotheksname>

	Wenn die Bibeljotheken installiert sind kann man das Script über die Console (python3 setup.py) oder mit doppelklick starten
